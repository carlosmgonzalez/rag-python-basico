import os
from typing import cast
from uuid import uuid4

import chromadb
from chromadb.api.types import Embeddable, EmbeddingFunction, OneOrMany
from chromadb.types import Metadata
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

from src.rag.knowledge_base import INVESTOR_DATA

load_dotenv()


class RAGPipeline:
    def __init__(self, collection_name: str, db_path: str = "./data/chromadb"):
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
        base_metadata: dict | None = None,
    ):
        chunk_chars_size = chunk_size * 4

        chunks = []
        start = 0

        while start < len(long_text):
            end = start + chunk_chars_size
            chunk = long_text[start:end]

            if chunk.strip():
                chunks.append(chunk)

            start = end - (overlap * 4)

        metadatas = []

        for i, _ in enumerate(chunks):
            meta = (base_metadata or {}).copy()
            meta["chunk_number"] = i
            meta["chunk_total"] = len(chunks)
            metadatas.append(meta)

        self.index_text(text=chunks, metadatas=metadatas)

        return len(chunks)

    def retrieve_context(
        self, question: str, n_fragments: int = 3
    ) -> list[dict] | None:
        results = self.collection.query(
            query_texts=[question],
            n_results=min(n_fragments, self.collection.count()),
            include=["documents", "metadatas", "distances"],
        )

        fragments = []

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


if __name__ == "__main__":
    rag = RAGPipeline("investors_knowledge_base")

    # rag.index_chunks(long_text=INVESTOR_DATA)

    retrieve_data = rag.retrieve_context(
        "Que datos necesito de un aplicante para poder saber si puede pedir un prestamo hipotecario?"
    )

    print(retrieve_data)
