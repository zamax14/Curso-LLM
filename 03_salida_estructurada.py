"""
03 - Salida Estructurada (JSON)
================================
Concepto: Un LLM genera texto libre, pero muchas veces necesitamos
          datos estructurados (ej: un diccionario con campos específicos).
          Podemos forzar al modelo a responder en JSON usando prompts
          bien diseñados y el parámetro format="json" de Ollama.
"""

import ollama
import json

# -----------------------------------------------------------
# Ejemplo 1: Sin formato definido → respuesta impredecible
# -----------------------------------------------------------
print("=== Sin formato: el modelo responde como quiere ===")
r = ollama.generate(
    model="llama3.2",
    prompt="Dame datos de Python: año de creación, creador y paradigma principal."
)
print(r["response"][:200])
print("...\n")

# -----------------------------------------------------------
# Ejemplo 2: Pedir JSON con un prompt explícito
# -----------------------------------------------------------
print("=== Con prompt explícito pidiendo JSON ===")
r = ollama.generate(
    model="llama3.2",
    prompt="""Dame información del lenguaje Python como un objeto JSON con estas claves:
- "nombre": nombre del lenguaje
- "anio_creacion": año de creación (número)
- "creador": nombre del creador
- "paradigma": paradigma principal
Responde SOLO con JSON válido, sin texto adicional."""
)
try:
    datos = json.loads(r["response"])
    print(json.dumps(datos, indent=2, ensure_ascii=False))
except json.JSONDecodeError:
    print("El modelo no generó JSON válido (puede pasar)")
    print(r["response"][:200])
print()

# -----------------------------------------------------------
# Ejemplo 3: Usar format="json" de Ollama (más confiable)
# Esto fuerza al modelo a generar JSON válido siempre.
# -----------------------------------------------------------
print("=== Con format='json' (forzado por Ollama) ===")
r = ollama.generate(
    model="llama3.2",
    prompt="""Extrae información del siguiente texto y responde en JSON:
"JavaScript fue creado por Brendan Eich en 1995. Es multiparadigma y es el lenguaje de la web."

Usa estas claves: "nombre", "anio_creacion", "creador", "paradigma".""",
    format="json"
)
datos = json.loads(r["response"])
print(json.dumps(datos, indent=2, ensure_ascii=False))
print()

# -----------------------------------------------------------
# Ejemplo 4: Clasificación de sentimiento (caso de uso real)
# -----------------------------------------------------------
print("=== Clasificador de sentimiento ===")

resenas = [
    "La pizza estaba buenísima, volvería mil veces",
    "Tardó una hora y llegó fría, pésimo servicio",
    "Normal, nada del otro mundo"
]

for resena in resenas:
    r = ollama.generate(
        model="llama3.2",
        prompt=f"""Clasifica el sentimiento de esta reseña como "positivo", "negativo" o "neutro".
Responde en JSON con claves "sentimiento" y "confianza" (0 a 1).

Reseña: "{resena}" """,
        format="json"
    )
    resultado = json.loads(r["response"])
    print(f"  '{resena[:40]}...' → {resultado}")
