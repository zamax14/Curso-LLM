"""
04 - Embeddings y Similitud
===========================
Concepto: Un embedding es una lista de números (vector) que representa
          el significado de un texto. Textos con significado similar tienen
          vectores similares (numéricamente cercanos).
          Esto permite buscar, comparar y agrupar textos por significado,
          no solo por palabras exactas.
"""

import ollama
import numpy as np

# -----------------------------------------------------------
# Ejemplo 1: Qué es un embedding
# Un embedding convierte texto en un vector de números.
# -----------------------------------------------------------
print("=== ¿Qué es un embedding? ===")
r = ollama.embeddings(model="llama3.2", prompt="Hola mundo")
vector = r["embedding"]

print(f"Dimensiones del vector: {len(vector)}")
print(f"Primeros 5 valores: {vector[:5]}")
print("Cada número captura un aspecto del significado del texto.\n")

# -----------------------------------------------------------
# Ejemplo 2: Similitud coseno
# Mide qué tan parecidos son dos vectores (va de -1 a 1).
# 1 = idénticos, 0 = sin relación, -1 = opuestos.
# -----------------------------------------------------------
def similitud_coseno(v1, v2):
    """Calcula la similitud coseno entre dos vectores."""
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("=== Similitud entre textos ===")

frases = [
    "El perro juega en el parque",
    "Un canino se divierte al aire libre",
    "La bolsa de valores subió un 5%",
    "El gato duerme en el sofá"
]

# Obtener embeddings de todas las frases
embeddings = []
for frase in frases:
    r = ollama.embeddings(model="llama3.2", prompt=frase)
    embeddings.append(r["embedding"])

# Comparar todas contra todas
print("\nMatriz de similitud:")
print(f"{'':>35}", end="")
for i in range(len(frases)):
    print(f"  F{i+1}", end="")
print()

for i in range(len(frases)):
    print(f"F{i+1}: {frases[i][:30]:>30}  ", end="")
    for j in range(len(frases)):
        sim = similitud_coseno(embeddings[i], embeddings[j])
        print(f"{sim:.2f}", end="  ")
    print()

print()
print("F1 y F2 dicen lo mismo con palabras distintas → alta similitud")
print("F1 y F3 hablan de temas distintos → baja similitud\n")

# -----------------------------------------------------------
# Ejemplo 3: Buscador semántico simple
# Dada una consulta, encontrar el texto más parecido por significado.
# -----------------------------------------------------------
print("=== Buscador semántico simple ===")

base_de_conocimiento = [
    "Python fue creado por Guido van Rossum en 1991",
    "JavaScript fue creado por Brendan Eich en 1995",
    "Los arrays en Python se llaman listas",
    "El machine learning es una rama de la inteligencia artificial",
    "Git fue creado por Linus Torvalds en 2005",
    "Las redes neuronales se inspiran en el cerebro humano",
]

# Precomputar embeddings de la base de conocimiento
embeddings_base = []
for texto in base_de_conocimiento:
    r = ollama.embeddings(model="llama3.2", prompt=texto)
    embeddings_base.append(r["embedding"])

def buscar(consulta, top_k=3):
    """Busca los textos más parecidos a la consulta por significado."""
    r = ollama.embeddings(model="llama3.2", prompt=consulta)
    embedding_consulta = r["embedding"]

    similitudes = []
    for i, emb in enumerate(embeddings_base):
        sim = similitud_coseno(embedding_consulta, emb)
        similitudes.append((sim, base_de_conocimiento[i]))

    similitudes.sort(reverse=True)
    return similitudes[:top_k]

resultados = buscar("¿quién inventó un lenguaje de programación?")
for sim, texto in resultados:
    print(f"  [{sim:.3f}] {texto}")

print()
resultados = buscar("¿cómo funciona la IA?")
for sim, texto in resultados:
    print(f"  [{sim:.3f}] {texto}")