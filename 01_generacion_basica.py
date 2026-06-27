"""
01 - Generación Básica con LLM Local
=====================================
Concepto: Un LLM recibe texto de entrada (prompt) y genera texto de salida.
          No "piensa" ni "sabe" nada — predice qué palabra viene después.
          Aún así, esa predicción es tan buena que parece magia.
"""

import ollama

# -----------------------------------------------------------
# Ejemplo 1: Generación simple
# Le damos un prompt y el modelo genera una respuesta.
# -----------------------------------------------------------
respuesta = ollama.generate(
    model="llama3.2",
    prompt="Explica qué es un modelo de lenguaje en una sola oración."
)
print("=== Generación simple ===")
print(respuesta["response"])
print()

# -----------------------------------------------------------
# Ejemplo 2: Controlar la creatividad con temperature
# temperature=0.0 → respuestas predecibles, casi siempre igual
# temperature=1.5  → respuestas más creativas, más variadas
# -----------------------------------------------------------
print("=== Con temperature=0.0 (predecible) ===")
for i in range(3):
    r = ollama.generate(
        model="llama3.2",
        prompt="Nombra un lenguaje de programación.",
        options={"temperature": 0.0}
    )
    print(f"  Intento {i+1}: {r['response'].strip()}")

print()
print("=== Con temperature=1.5 (creativo) ===")
for i in range(3):
    r = ollama.generate(
        model="llama3.2",
        prompt="Nombra un lenguaje de programación.",
        options={"temperature": 1.5}
    )
    print(f"  Intento {i+1}: {r['response'].strip()}")
print()

# -----------------------------------------------------------
# Ejemplo 3: Prompts más útiles
# Un buen prompt es la clave para obtener buenas respuestas.
# -----------------------------------------------------------
prompt_ingenieria = """Eres un asistente para estudiantes de ingeniería en computación.
Explica qué es la recursividad usando analogías de la vida real.
Sé breve, usa no más de 3 oraciones."""

respuesta = ollama.generate(model="llama3.2", prompt=prompt_ingenieria)
print("=== Prompt mejorado ===")
print(respuesta["response"])
