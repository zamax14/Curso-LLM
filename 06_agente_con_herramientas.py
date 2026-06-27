"""
06 - Agente con Herramientas (¡Superpoderes!)
===============================================
Concepto: Un LLM solo genera texto. No puede hacer cálculos exactos,
          acceder a internet, ni ejecutar código. Pero nosotros podemos
          darle "herramientas" (funciones Python) y dejar que él decida
          cuándo usarlas. Esto convierte al LLM en un AGENTE que puede
          actuar sobre el mundo real.
          Esto es lo que hace que la "IA moderna" parezca inteligente:
          el modelo elige qué herramienta usar, y nuestro código la ejecuta.
"""

import ollama
import json

# -----------------------------------------------------------
# Definir las herramientas (funciones Python que el LLM puede usar)
# -----------------------------------------------------------

def obtener_clima(ciudad):
    """Simula obtener el clima de una ciudad (en la vida real llamaría a una API)."""
    clima_ficticio = {
        "Buenos Aires": {"temperatura": 22, "condicion": "parcialmente nublado"},
        "Córdoba": {"temperatura": 25, "condicion": "soleado"},
        "Mendoza": {"temperatura": 18, "condicion": "ventoso"},
        "Bariloche": {"temperatura": 8, "condicion": "nevando"},
    }
    return json.dumps(clima_ficticio.get(ciudad, {"temperatura": 20, "condicion": "desconocido"}))

def calcular(expresion):
    """Evalúa una expresión matemática de forma segura."""
    try:
        # Solo permitir números y operaciones básicas por seguridad
        permitidos = set("0123456789+-*/().% ")
        if all(c in permitidos for c in expresion):
            return json.dumps({"resultado": eval(expresion)})
        return json.dumps({"error": "Expresión no permitida"})
    except Exception as e:
        return json.dumps({"error": str(e)})

def buscar_producto(producto):
    """Simula buscar un producto en una base de datos."""
    productos = {
        "notebook": {"nombre": "Notebook 15\"", "precio": 450000, "stock": 12},
        "mouse": {"nombre": "Mouse inalámbrico", "precio": 15000, "stock": 50},
        "teclado": {"nombre": "Teclado mecánico", "precio": 35000, "stock": 25},
        "monitor": {"nombre": "Monitor 24\"", "precio": 180000, "stock": 8},
    }
    return json.dumps(productos.get(producto.lower(), {"error": "Producto no encontrado"}))

# Diccionario que mapea nombres de herramientas a funciones
HERRAMIENTAS = {
    "obtener_clima": obtener_clima,
    "calcular": calcular,
    "buscar_producto": buscar_producto,
}

# Definición de herramientas para que Ollama sepa cuáles tiene disponibles
DEFINICION_HERRAMIENTAS = [
    {
        "type": "function",
        "function": {
            "name": "obtener_clima",
            "description": "Obtiene el clima actual de una ciudad argentina",
            "parameters": {
                "type": "object",
                "properties": {
                    "ciudad": {
                        "type": "string",
                        "description": "Nombre de la ciudad (ej: Buenos Aires, Córdoba)"
                    }
                },
                "required": ["ciudad"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calcular",
            "description": "Calcula una expresión matemática",
            "parameters": {
                "type": "object",
                "properties": {
                    "expresion": {
                        "type": "string",
                        "description": "Expresión matemática (ej: 2+2, 15*3.5)"
                    }
                },
                "required": ["expresion"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_producto",
            "description": "Busca un producto en el inventario de la tienda",
            "parameters": {
                "type": "object",
                "properties": {
                    "producto": {
                        "type": "string",
                        "description": "Nombre del producto (ej: notebook, mouse, teclado, monitor)"
                    }
                },
                "required": ["producto"]
            }
        }
    }
]

# -----------------------------------------------------------
# Bucle de agente: el LLM decide si usa herramientas o responde directo
# -----------------------------------------------------------
def ejecutar_agente(mensaje_usuario):
    """Ejecuta el agente que puede usar herramientas para responder."""
    mensajes = [
        {"role": "system", "content": "Sos un asistente útil que puede usar herramientas. Siempre respondé en español."},
        {"role": "user", "content": mensaje_usuario}
    ]

    iteracion = 0
    max_iteraciones = 5  # Evitar bucles infinitos

    while iteracion < max_iteraciones:
        iteracion += 1

        # Llamar al modelo con las herramientas disponibles
        respuesta = ollama.chat(
            model="llama3.2",
            messages=mensajes,
            tools=DEFINICION_HERRAMIENTAS
        )

        mensaje = respuesta["message"]

        # Si el modelo quiere usar una herramienta
        if mensaje.get("tool_calls"):
            # Agregar la respuesta del modelo al historial
            mensajes.append(mensaje)

            # Ejecutar cada herramienta que el modelo pidió
            for llamada in mensaje["tool_calls"]:
                nombre = llamada["function"]["name"]
                argumentos = llamada["function"]["arguments"]

                print(f"  🔧 Usando herramienta: {nombre}({argumentos})")

                # Ejecutar la función Python correspondiente
                funcion = HERRAMIENTAS[nombre]
                resultado = funcion(**argumentos)

                # Agregar el resultado al historial para que el modelo lo use
                mensajes.append({
                    "role": "tool",
                    "name": nombre,
                    "content": resultado
                })

        # Si el modelo ya no quiere usar herramientas, devolver la respuesta
        elif mensaje.get("content"):
            return mensaje["content"]

    return "El agente no pudo completar la tarea (máximo de iteraciones alcanzado)."

# -----------------------------------------------------------
# Probar el agente con distintas consultas
# -----------------------------------------------------------
consultas = [
    "¿Qué clima hace en Córdoba?",
    "¿Cuánto es 347 * 29?",
    "¿Tienen teclados en la tienda?",
    "Si un mouse sale 15000 y compro 3, ¿cuánto gasto?",  # Combina herramienta + cálculo
]

for consulta in consultas:
    print(f"\n👤 Consulta: {consulta}")
    respuesta = ejecutar_agente(consulta)
    print(f"🤖 Respuesta: {respuesta.strip()}")
    print("-" * 60)