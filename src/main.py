from src.rag.embeddings_demo import (
    cosine_similarity,
    demonstrate_semantic_similarity,
    get_embedding,
)


def main():
    result = demonstrate_semantic_similarity()
    print(result)

    # value_a = "Hombre"
    # value_b = "Hombre"
    # vector_a = get_embedding(value_a)
    # vector_b = get_embedding(value_b)

    # similarity = cosine_similarity(vector_a, vector_b)

    # print(f"Similitud entre {value_a} y {value_b} = {similarity}")


if __name__ == "__main__":
    main()
