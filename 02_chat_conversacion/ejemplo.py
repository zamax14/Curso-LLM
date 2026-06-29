import sys

import ollama


MODEL = "llama3.2"


def responder(mensajes):
    respuesta = ollama.chat(model=MODEL, messages=mensajes)
    return respuesta["message"]


def demo_memoria():
    print("Sin memoria")
    r1 = responder([{"role": "user", "content": "Me llamo Martín."}])
    print(f"Modelo: {r1['content'].strip()}")

    r2 = responder([{"role": "user", "content": "¿Cómo me llamo?"}])
    print(f"Modelo: {r2['content'].strip()}")

    print("\nCon memoria")
    historial = [
        {
            "role": "system",
            "content": "Eres un asistente amable que recuerda datos del usuario.",
        },
        {
            "role": "user",
            "content": "Me llamo Martín y estudio ingeniería en computación.",
        },
    ]

    r1 = responder(historial)
    historial.append(r1)
    historial.append({"role": "user", "content": "¿Cómo me llamo y qué estudio?"})

    r2 = responder(historial)
    print(f"Modelo: {r2['content'].strip()}")


def chat_interactivo():
    historial = [
        {
            "role": "system",
            "content": "Eres un asistente útil y conciso. Responde en español.",
        }
    ]

    print("Chat interactivo. Escribe 'salir' para terminar.\n")
    while True:
        usuario = input("Tú: ")
        if usuario.lower() == "salir":
            break

        historial.append({"role": "user", "content": usuario})
        respuesta = responder(historial)
        historial.append(respuesta)
        print(f"Modelo: {respuesta['content'].strip()}\n")


def main():
    if "--interactive" in sys.argv:
        chat_interactivo()
    else:
        demo_memoria()


if __name__ == "__main__":
    main()
