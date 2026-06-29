import json

import ollama


MODEL = "llama3.2"


def obtener_clima(ciudad):
    clima = {
        "Ciudad de México": {"temperatura": 22, "condicion": "parcialmente nublado"},
        "Guadalajara": {"temperatura": 28, "condicion": "soleado"},
        "Monterrey": {"temperatura": 31, "condicion": "caluroso"},
        "Puebla": {"temperatura": 20, "condicion": "lluvioso"},
    }
    return json.dumps(clima.get(ciudad, {"temperatura": 20, "condicion": "desconocido"}))


def calcular(expresion):
    permitidos = set("0123456789+-*/().% ")
    if not all(caracter in permitidos for caracter in expresion):
        return json.dumps({"error": "Expresión no permitida"})

    try:
        resultado = eval(expresion, {"__builtins__": {}})
        return json.dumps({"resultado": resultado})
    except Exception as error:
        return json.dumps({"error": str(error)})


def buscar_producto(producto):
    productos = {
        "laptop": {"nombre": "Laptop 15\"", "precio": 14500, "stock": 12},
        "mouse": {"nombre": "Mouse inalámbrico", "precio": 250, "stock": 50},
        "teclado": {"nombre": "Teclado mecánico", "precio": 1200, "stock": 25},
        "monitor": {"nombre": "Monitor 24\"", "precio": 3200, "stock": 8},
    }
    return json.dumps(productos.get(producto.lower(), {"error": "Producto no encontrado"}))


HERRAMIENTAS = {
    "obtener_clima": obtener_clima,
    "calcular": calcular,
    "buscar_producto": buscar_producto,
}

DEFINICION_HERRAMIENTAS = [
    {
        "type": "function",
        "function": {
            "name": "obtener_clima",
            "description": "Obtiene el clima actual de una ciudad mexicana",
            "parameters": {
                "type": "object",
                "properties": {
                    "ciudad": {
                        "type": "string",
                        "description": "Nombre de la ciudad",
                    }
                },
                "required": ["ciudad"],
            },
        },
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
                        "description": "Expresión matemática",
                    }
                },
                "required": ["expresion"],
            },
        },
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
                        "description": "Nombre del producto",
                    }
                },
                "required": ["producto"],
            },
        },
    },
]


def normalizar_argumentos(argumentos):
    if isinstance(argumentos, str):
        return json.loads(argumentos)
    return argumentos


def ejecutar_agente(mensaje_usuario, max_iteraciones=5):
    mensajes = [
        {
            "role": "system",
            "content": "Eres un asistente útil que puede usar herramientas. Siempre responde en español.",
        },
        {"role": "user", "content": mensaje_usuario},
    ]

    for _ in range(max_iteraciones):
        respuesta = ollama.chat(
            model=MODEL,
            messages=mensajes,
            tools=DEFINICION_HERRAMIENTAS,
        )
        mensaje = respuesta["message"]

        if mensaje.get("tool_calls"):
            mensajes.append(mensaje)
            for llamada in mensaje["tool_calls"]:
                nombre = llamada["function"]["name"]
                argumentos = normalizar_argumentos(llamada["function"]["arguments"])
                resultado = HERRAMIENTAS[nombre](**argumentos)
                mensajes.append({"role": "tool", "name": nombre, "content": resultado})
            continue

        if mensaje.get("content"):
            return mensaje["content"].strip()

    return "El agente no pudo completar la tarea."


def main():
    consultas = [
        "¿Qué clima hace en Guadalajara?",
        "¿Cuánto es 347 * 29?",
        "¿Tienen teclados en la tienda?",
        "Si un mouse cuesta 250 y compro 3, ¿cuánto gasto?",
    ]

    for consulta in consultas:
        print(f"\nConsulta: {consulta}")
        print(f"Respuesta: {ejecutar_agente(consulta)}")


if __name__ == "__main__":
    main()
