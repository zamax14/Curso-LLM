import json

import ollama


MODEL = "llama3.2"


def generar(prompt, formato=None):
    argumentos = {"model": MODEL, "prompt": prompt}
    if formato:
        argumentos["format"] = formato
    return ollama.generate(**argumentos)["response"].strip()


def imprimir_json(texto):
    datos = json.loads(texto)
    print(json.dumps(datos, indent=2, ensure_ascii=False))


def main():
    print("Respuesta libre")
    texto = generar(
        "Dame datos de Python: año de creación, creador y paradigma principal."
    )
    print(texto[:300])

    print("\nJSON solicitado en el prompt")
    texto = generar(
        """Dame información del lenguaje Python como un objeto JSON con estas claves:
- "nombre": nombre del lenguaje
- "anio_creacion": año de creación como número
- "creador": nombre del creador
- "paradigma": paradigma principal
Responde SOLO con JSON válido, sin texto adicional."""
    )
    try:
        imprimir_json(texto)
    except json.JSONDecodeError:
        print(texto[:300])

    print("\nJSON forzado por Ollama")
    texto = generar(
        """Extrae información del siguiente texto y responde en JSON:
"JavaScript fue creado por Brendan Eich en 1995. Es multiparadigma y es el lenguaje de la web."

Usa estas claves: "nombre", "anio_creacion", "creador", "paradigma".""",
        formato="json",
    )
    imprimir_json(texto)

    print("\nClasificador de sentimiento")
    resenas = [
        "La pizza estaba buenísima, volvería mil veces",
        "Tardó una hora y llegó fría, pésimo servicio",
        "Normal, nada del otro mundo",
    ]

    for resena in resenas:
        texto = generar(
            f"""Clasifica el sentimiento de esta reseña como "positivo", "negativo" o "neutro".
Responde en JSON con claves "sentimiento" y "confianza" de 0 a 1.

Reseña: "{resena}" """,
            formato="json",
        )
        print(json.loads(texto))


if __name__ == "__main__":
    main()
