import numpy as np
import ollama


MODEL = "llama3.2"

BASE_DE_CONOCIMIENTO = [
    "Horario del examen final de Álgebra: lunes y miércoles de 10:00 a 12:00, aula 301.",
    "El profesor de Cálculo Diferencial es el Dr. García, cubículo: edificio 2, piso 3.",
    "La fecha del examen final de Programación es el 15 de julio de 2025.",
    "Para inscribirse a materias usa el sistema de control escolar: control.universidad.mx",
    "El laboratorio de computación está abierto de 8:00 a 22:00, edificio 5, planta baja.",
    "Beca universitaria: plazo de inscripción hasta el 30 de junio de 2025.",
    "La biblioteca tiene horario extendido en época de exámenes: 8:00 a 24:00.",
    "El correo de soporte técnico es soporte@universidad.mx.",
    "Programación II exige haber aprobado Programación I con nota mínima de 6.",
    "El centro de estudiantes está en el edificio 1, primer piso, oficina 108.",
]


def obtener_embedding(texto):
    return ollama.embeddings(model=MODEL, prompt=texto)["embedding"]


def similitud_coseno(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def buscar_contexto(pregunta, embeddings_base, top_k=3):
    embedding_pregunta = obtener_embedding(pregunta)
    resultados = []

    for texto, embedding in zip(BASE_DE_CONOCIMIENTO, embeddings_base):
        similitud = similitud_coseno(embedding_pregunta, embedding)
        resultados.append((similitud, texto))

    return sorted(resultados, reverse=True)[:top_k]


def responder_con_rag(pregunta, embeddings_base):
    resultados = buscar_contexto(pregunta, embeddings_base)
    contexto = "\n".join(texto for _, texto in resultados)
    prompt = f"""Contesta la pregunta usando SOLO la información del contexto.
Si la información no está en el contexto, di "No tengo esa información".

Contexto:
{contexto}

Pregunta: {pregunta}
Respuesta:"""
    return ollama.generate(model=MODEL, prompt=prompt)["response"].strip()


def main():
    print("Creando embeddings de la base de conocimiento...")
    embeddings_base = [obtener_embedding(texto) for texto in BASE_DE_CONOCIMIENTO]

    preguntas = [
        "¿Cuándo es el examen de Programación?",
        "¿Cómo me inscribo a materias?",
        "¿Dónde está el centro de estudiantes?",
        "¿Cuándo juega México?",
    ]

    for pregunta in preguntas:
        print(f"\nPregunta: {pregunta}")
        print(f"Respuesta: {responder_con_rag(pregunta, embeddings_base)}")


if __name__ == "__main__":
    main()
