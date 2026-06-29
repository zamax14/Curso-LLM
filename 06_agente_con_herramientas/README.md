<div align="center">

# 06 - Agente con herramientas

**Pasar de generar texto a ejecutar acciones controladas desde Python.**

[![Módulo](https://img.shields.io/badge/modulo-06-dc2626)](./)
[![Concepto](https://img.shields.io/badge/concepto-LLM%20%2B%20funciones-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Exponer herramientas de clima, cálculo e inventario, y dejar que el modelo las invoque según la consulta.

## Problema

Un LLM no calcula con precisión ni consulta inventarios reales por sí solo. Para actuar, necesita herramientas que la aplicación sí pueda ejecutar.

## Idea clave

El modelo decide qué función necesita, el programa la ejecuta y el resultado vuelve al historial para que el modelo construya la respuesta final.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Definir funciones | Crear herramientas normales de Python. |
| 2 | Describir herramientas | Decirle al modelo nombres, parámetros y propósito. |
| 3 | Detectar tool calls | Leer qué función pidió el modelo. |
| 4 | Ejecutar y responder | Devolver el resultado al modelo para cerrar la tarea. |

## Archivos del módulo

| Archivo | Uso recomendado |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | Seguir la explicación en clase, ejecutar celda por celda y modificar parámetros. |
| [`ejemplo.py`](ejemplo.py) | Correr la demo completa desde terminal, sin la explicación extendida. |
| [`README.md`](README.md) | Tener a la mano el objetivo, comandos y experimentos sugeridos. |

## Ejecutar

```bash
python3 ejemplo.py
```

> [!NOTE]
> Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado. Si usas otro modelo, cambia la constante `MODEL` en el notebook o en el script.

## Experimentos rápidos

- Agrega una herramienta nueva, por ejemplo convertir monedas ficticias.
- Pregunta algo que combine inventario y cálculo.
- Prueba qué pasa si el usuario pide una operación no permitida.

## Siguiente módulo

Este es el cierre del recorrido: aquí se conectan prompts, memoria, JSON, búsqueda y herramientas.
