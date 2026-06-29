import numpy as np
import ollama


MODEL = "llama3.2"


def obtener_embedding(texto):
    return ollama.embeddings(model=MODEL, prompt=texto)["embedding"]


def similitud_coseno(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def buscar(consulta, documentos, embeddings_documentos, top_k=3):
    embedding_consulta = obtener_embedding(consulta)
    resultados = []

    for documento, embedding in zip(documentos, embeddings_documentos):
        similitud = similitud_coseno(embedding_consulta, embedding)
        resultados.append((similitud, documento))

    return sorted(resultados, reverse=True)[:top_k]


def main():
    vector = obtener_embedding("Hola mundo")
    print(f"Dimensiones del embedding: {len(vector)}")
    print(f"Primeros 5 valores: {vector[:5]}")

    frases = [
        "El perro juega en el parque",
        "Un canino se divierte al aire libre",
        "La bolsa de valores subió un 5%",
        "El gato duerme en el sofá",
    ]
    embeddings = [obtener_embedding(frase) for frase in frases]

    print("\nMatriz de similitud")
    print(f"{'':>35}", end="")
    for indice in range(len(frases)):
        print(f"  F{indice + 1}", end="")
    print()

    for i, frase in enumerate(frases):
        print(f"F{i + 1}: {frase[:30]:>30}  ", end="")
        for embedding in embeddings:
            print(f"{similitud_coseno(embeddings[i], embedding):.2f}", end="  ")
        print()

    base = [
        "Python fue creado por Guido van Rossum en 1991",
        "JavaScript fue creado por Brendan Eich en 1995",
        "Los arrays en Python se llaman listas",
        "El machine learning es una rama de la inteligencia artificial",
        "Git fue creado por Linus Torvalds en 2005",
        "Las redes neuronales se inspiran en el cerebro humano",
    ]
    embeddings_base = [obtener_embedding(texto) for texto in base]

    print("\nBúsqueda: ¿quién inventó un lenguaje de programación?")
    for similitud, texto in buscar("quién inventó un lenguaje de programación?", base, embeddings_base):
        print(f"[{similitud:.3f}] {texto}")

    print("\nBúsqueda: ¿cómo funciona la IA?")
    for similitud, texto in buscar("cómo funciona la IA?", base, embeddings_base):
        print(f"[{similitud:.3f}] {texto}")


if __name__ == "__main__":
    main()
