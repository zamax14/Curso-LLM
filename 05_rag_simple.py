"""
05 - RAG Simple (Retrieval-Augmented Generation)
==================================================
Concepto: RAG combina búsqueda + generación. En lugar de pedirle al LLM
          que responda de memoria, le damos contexto relevante encontrado
          mediante embeddings, y luego dejamos que genere la respuesta.
          Así el modelo puede responder sobre datos que "no sabe" (ej: tus apuntes).
"""

import ollama
import numpy as np

# -----------------------------------------------------------
# Base de conocimiento simulada (podría ser un PDF, apuntes, etc.)
# -----------------------------------------------------------
base_de_conocimiento = [
    "Horario de final de Álgebra: lunes y miércoles de 10:00 a 12:00, aula 301.",
    "El profesor de Análisis Matemático es el Dr. García, oficina: edificio 2, piso 3.",
    "La fecha de examen final de Programación es el 15 de julio de 2025.",
    "Para inscribirse a materias usar el sistema Guaraní: guarani.universidad.edu.ar",
    "El laboratorio de computación está abierto de 8:00 a 22:00, edificio 5, planta baja.",
    "Beca universitaria: plazo de inscripción hasta el 30 de junio de 2025.",
    "La biblioteca tiene horario extendido en época de exámenes: 8:00 a 24:00.",
    "El email de soporte técnico es soporte@universidad.edu.ar.",
    "Programación II exige haber aprobado Programación I con nota mínima de 6.",
    "El centro de estudiantes está en el edificio 1, primer piso, oficina 108.",
]

# -----------------------------------------------------------
# Paso 1: Crear embeddings de toda la base de conocimiento
# -----------------------------------------------------------
def obtener_embedding(texto):
    r = ollama.embeddings(model="llama3.2", prompt=texto)
    return r["embedding"]

def similitud_coseno(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("Creando embeddings de la base de conocimiento...")
embeddings_base = [obtener_embedding(t) for t in base_de_conocimiento]
print("Listo.\n")

# -----------------------------------------------------------
# Paso 2: Función de búsqueda
# Dada una pregunta, encontrar los fragmentos más relevantes.
# -----------------------------------------------------------
def buscar_contexto(pregunta, top_k=3):
    embedding_pregunta = obtener_embedding(pregunta)
    similitudes = []
    for i, emb in enumerate(embeddings_base):
        sim = similitud_coseno(embedding_pregunta, emb)
        similitudes.append((sim, base_de_conocimiento[i]))
    similitudes.sort(reverse=True)
    return similitudes[:top_k]

# -----------------------------------------------------------
# Paso 3: RAG - Buscar contexto + Generar respuesta
# -----------------------------------------------------------
def rag(pregunta):
    """Busca contexto relevante y genera una respuesta informada."""

    # Buscar los fragmentos más relevantes
    resultados = buscar_contexto(pregunta)
    contexto = "\n".join([texto for _, texto in resultados])

    # Construir el prompt con el contexto encontrado
    prompt = f"""Contestá la pregunta usando SOLO la información del contexto de abajo.
Si la información no está en el contexto, decí "No tengo esa información".

Contexto:
{contexto}

Pregunta: {pregunta}
Respuesta:"""

    # Generar respuesta con el contexto incluido
    respuesta = ollama.generate(model="llama3.2", prompt=prompt)
    return respuesta["response"]

# -----------------------------------------------------------
# Probar el sistema RAG
# -----------------------------------------------------------
preguntas = [
    "¿Cuándo es el examen de Programación?",
    "¿Cómo me inscribo a materias?",
    "¿Dónde está el centro de estudiantes?",
    "¿Cuándo juega Argentina?",  # No está en la base → "No tengo esa información"
]

for pregunta in preguntas:
    print(f"❓ Pregunta: {pregunta}")
    print(f"💡 Respuesta: {rag(pregunta).strip()}")
    print()