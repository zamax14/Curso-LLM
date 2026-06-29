import ollama


MODEL = "llama3.2"


def generar(prompt, options=None):
    respuesta = ollama.generate(
        model=MODEL,
        prompt=prompt,
        options=options or {},
    )
    return respuesta["response"].strip()


def main():
    print("Generación simple")
    print(generar("Explica qué es un modelo de lenguaje en una sola oración."))

    print("\nTemperature baja")
    for intento in range(1, 4):
        texto = generar(
            "Nombra un lenguaje de programación.",
            options={"temperature": 0.0},
        )
        print(f"{intento}. {texto}")

    print("\nTemperature alta")
    for intento in range(1, 4):
        texto = generar(
            "Nombra un lenguaje de programación.",
            options={"temperature": 1.5},
        )
        print(f"{intento}. {texto}")

    prompt = """Eres un asistente para estudiantes de ingeniería en computación.
Explica qué es la recursividad usando analogías de la vida real.
Sé breve, usa no más de 3 oraciones."""

    print("\nPrompt mejorado")
    print(generar(prompt))


if __name__ == "__main__":
    main()
