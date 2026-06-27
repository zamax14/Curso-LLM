"""
02 - Chat Conversacional
========================
Concepto: Un LLM no tiene memoria por defecto. Cada llamado es independiente.
          Para "recordar", le pasamos el historial completo de la conversación.
          Así funciona ChatGPT, Gemini, etc.: cada mensaje incluye TODO lo anterior.
"""

import ollama

# -----------------------------------------------------------
# Ejemplo 1: Chat sin memoria (el modelo no recuerda nada)
# -----------------------------------------------------------
print("=== Sin memoria: cada llamado es independiente ===")

r1 = ollama.chat(model="llama3.2", messages=[
    {"role": "user", "content": "Me llamo Martín."}
])
print(f"Modelo: {r1['message']['content'].strip()}")

r2 = ollama.chat(model="llama3.2", messages=[
    {"role": "user", "content": "¿Cómo me llamo?"}
])
print(f"Modelo: {r2['message']['content'].strip()}")
print("(No recuerda el nombre porque no tiene el contexto)\n")

# -----------------------------------------------------------
# Ejemplo 2: Chat CON memoria (le pasamos el historial)
# El rol "system" define el comportamiento general del modelo.
# "user" es lo que dice la persona, "assistant" lo que respondió antes.
# -----------------------------------------------------------
print("=== Con memoria: pasamos el historial completo ===")

historial = [
    {"role": "system", "content": "Eres un asistente amable que recuerda datos del usuario."},
    {"role": "user", "content": "Me llamo Martín y estudio ingeniería en computación."},
]

r1 = ollama.chat(model="llama3.2", messages=historial)
print(f"Modelo: {r1['message']['content'].strip()}")

# Agregamos la respuesta del modelo y la nueva pregunta al historial
historial.append(r1["message"])
historial.append({"role": "user", "content": "¿Cómo me llamo y qué estudio?"})

r2 = ollama.chat(model="llama3.2", messages=historial)
print(f"Modelo: {r2['message']['content'].strip()}")
print("(Ahora sí recuerda porque tiene el contexto)\n")

# -----------------------------------------------------------
# Ejemplo 3: Chat interactivo en terminal (descomentar para probar)
# Esto crea un bucle donde puedes chatear con el modelo.
# -----------------------------------------------------------
def chat_interactivo():
    """Chat simple en terminal con memoria de conversación."""
    historial = [
        {"role": "system", "content": "Eres un asistente útil y conciso. Responde en español."}
    ]
    print("Chat interactivo (escribe 'salir' para terminar)\n")

    while True:
        usuario = input("Tú: ")
        if usuario.lower() == "salir":
            break

        historial.append({"role": "user", "content": usuario})
        respuesta = ollama.chat(model="llama3.2", messages=historial)
        contenido = respuesta["message"]["content"]
        historial.append(respuesta["message"])
        print(f"Modelo: {contenido}\n")

# Descomenta la siguiente línea para chatear interactivamente:
# chat_interactivo()
