import os
from typing import TypedDict, cast
from uuid import uuid4

import chromadb
from chromadb.api.types import Embeddable, EmbeddingFunction, OneOrMany
from chromadb.types import Metadata
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

from src.ai.openai_client import openai_client
from src.rag.knowledge_base import INVESTOR_DATA

load_dotenv()


class RetrievedFragment(TypedDict):
    text: str
    metadata: Metadata
    similarity: float


class ResponseAnswer(TypedDict):
    response: str
    fragments_used: list[RetrievedFragment]
    are_there_context: bool


class RAGPipeline:
    def __init__(self, collection_name: str, db_path: str = "./data/chromadb") -> None:
        self.chroma_client = chromadb.PersistentClient(path=db_path)

        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.environ["OPENAI_API_KEY"], model_name="text-embedding-3-small"
        )

        self.collection = self.chroma_client.get_or_create_collection(
            name=collection_name,
            embedding_function=cast(
                EmbeddingFunction[Embeddable],
                self.embedding_function,
            ),
        )

    def index_text(
        self, text: list[str], metadatas: OneOrMany[Metadata] | None = None
    ) -> None:
        ids = [f"doc_{uuid4()}" for _ in text]

        if metadatas is None:
            metadatas = [{"fuente": "manuel"} for _ in text]

        self.collection.add(ids=ids, documents=text, metadatas=metadatas)

        print("Informacion indexada correctamente")

    def index_chunks(
        self,
        long_text: str,
        chunk_size: int = 500,
        overlap: int = 50,
        base_metadata: Metadata | None = None,
    ) -> int:
        chunk_chars_size = chunk_size * 4

        chunks: list[str] = []
        start = 0

        while start < len(long_text):
            end = start + chunk_chars_size
            chunk = long_text[start:end]

            if chunk.strip():
                chunks.append(chunk)

            start = end - (overlap * 4)

        metadatas: list[Metadata] = []

        for i, _ in enumerate(chunks):
            meta = dict(base_metadata or {})
            meta["chunk_number"] = i
            meta["chunk_total"] = len(chunks)
            metadatas.append(meta)

        self.index_text(text=chunks, metadatas=metadatas)

        return len(chunks)

    def retrieve_context(
        self, question: str, n_fragments: int = 3
    ) -> list[RetrievedFragment]:
        results = self.collection.query(
            query_texts=[question],
            n_results=min(n_fragments, self.collection.count()),
            include=["documents", "metadatas", "distances"],
        )

        fragments: list[RetrievedFragment] = []

        documents = results["documents"]
        distances = results["distances"]
        metadatas = results["metadatas"]

        if documents and distances and metadatas:
            for i in range(len(documents[0])):
                similarity = round(1 - distances[0][i], 3)

                if similarity > 0.3:
                    fragments.append(
                        {
                            "text": documents[0][i],
                            "metadata": metadatas[0][i],
                            "similarity": similarity,
                        }
                    )

        return fragments

    def answer(
        self, question: str, n_fragments: int = 3, verbose: bool = False
    ) -> ResponseAnswer | None:
        fragments = self.retrieve_context(question=question, n_fragments=n_fragments)

        if not fragments:
            return {
                "response": "There are not information about the question in this knowledge base",
                "fragments_used": [],
                "are_there_context": False,
            }

        if verbose:
            print("\nFragments founded:\n")
            for fragment in fragments:
                print(f"{fragment['similarity']}\n{fragment['text'][:80]}")

        context_text = "\n\n--\n\n".join(
            [
                f"Source: {fragment['metadata'].get('')}{fragment['text']}"
                for fragment in fragments
            ]
        )

        system_prompt = """Eres un asistente experto que responde preguntas
        basándote ÚNICAMENTE en el contexto proporcionado.
        Reglas:
        - Si la respuesta está en el contexto, respóndela directamente y con precisión.
        - Si el contexto no contiene suficiente información, dilo honestamente.
        - Cita la fuente cuando sea relevante.
        - No inventes información que no esté en el contexto.
        - Responde en el mismo idioma de la pregunta."""

        user_prompt = f"""Contexto disponible:
        {context_text}
        Pregunta: {question}"""

        response = openai_client.chat.completions.create(
            model="gpt-5.6-luna",
            reasoning_effort="low",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        return {
            "response": response.choices[0].message.content or "",
            "fragments_used": fragments,
            "are_there_context": True,
        }


if __name__ == "__main__":
    rag = RAGPipeline("investors_knowledge_base")

    # rag.index_chunks(long_text=INVESTOR_DATA)

    response = rag.answer(
        """Dime cual es el FICO minimo que debo tener, cuanto es el LTV maximo que ofrece el investor,
        para que tipo de propiedad puedo pedir el prestamo, aceptan la documentacion w2"""
    )

    if response:
        print(response["response"])
