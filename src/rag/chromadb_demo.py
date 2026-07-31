import os
from typing import cast

import chromadb
from chromadb import Collection
from chromadb.api import ClientAPI
from chromadb.api.types import Embeddable, EmbeddingFunction
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

from src.rag.knowledge_base import KNOWLEDGE_BASE

load_dotenv()


def create_chroma_client(persist: bool = True):
    if persist:
        return chromadb.PersistentClient(path="./data/chromadb")
    else:
        return chromadb.EphemeralClient()


def create_collection(client: ClientAPI, name: str):
    openai_em = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.environ["OPENAI_API_KEY"], model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name=name,
        embedding_function=cast(
            EmbeddingFunction[Embeddable],
            openai_em,
        ),
        metadata={"description": "Base de conocimiento del curso"},
    )

    return collection


def add_documents(collection: Collection, documents: list[dict]) -> None:
    collection.add(
        ids=[doc["id"] for doc in documents],
        documents=[doc["text"] for doc in documents],
        metadatas=[doc["metadata"] for doc in documents],
    )

    print("Documentos agregados a ChromaDB")


def search_similar(
    collection: Collection, question: str, n_results: int = 3
) -> list[dict]:
    results = collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    formatted_docs = []

    print(results)

    if results["documents"] and results["metadatas"] and results["distances"]:
        for i in range(len(results["documents"][0])):
            formatted_docs.append(
                {
                    "text": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "similitud": results["distances"][0][i],
                }
            )
    return formatted_docs


if __name__ == "__main__":
    chroma_client = create_chroma_client(True)
    collection = create_collection(chroma_client, "knowledge_base")

    if collection.count() == 0:
        print("Indexando documentos")
        add_documents(collection=collection, documents=KNOWLEDGE_BASE)

    test_questions = [
        "¿Cómo reinicio el servidor web?",
        "¿Dónde están las credenciales de la base de datos?",
        "¿Cómo hago deploy a producción?",
        "¿Qué pasa si hago demasiadas llamadas a la API?",
        "Mi web app dejó de responder",
        "Olvidé dónde guardamos los passwords",
        "Quiero publicar mi código en vivo",
    ]

    for question in test_questions:
        print(f"\n Pregunta: {question}")
        result = search_similar(collection=collection, question=question, n_results=2)
        # print(result)
