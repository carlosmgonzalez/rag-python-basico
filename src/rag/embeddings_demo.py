import math

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )

    return response.data[0].embedding


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    magnitude_a = math.sqrt(sum(a**2 for a in vector_a))
    magnitude_b = math.sqrt(sum(b**2 for b in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def demonstrate_semantic_similarity():
    base_phrase = "¿Cómo puedo reiniciar el servidor?"

    candidates = [
        "Para reiniciar el servidor ejecuta: sudo systemctl restart nginx",
        "Puedes reboot el proceso con el comando service stop/start",
        "The server restart procedure is documented in section 4.2",
        "La pizza margarita lleva tomate, mozzarella y albahaca",
        "Los gatos domésticos duermen un promedio de 16 horas al día",
        "Para apagar el servidor usa: sudo shutdown -h now",
    ]

    vector_base_phrase = get_embedding(base_phrase)
    highest_similarity = float("-inf")

    result = ""

    for candidate in candidates:
        vector_candidate = get_embedding(candidate)
        similarity = cosine_similarity(vector_base_phrase, vector_candidate)

        if similarity > highest_similarity:
            highest_similarity = similarity
            result = candidate

    return result
