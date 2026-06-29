<div align="center">

# 01 - Generación básica

**La unidad mínima de un LLM local: enviar texto y recibir texto.**

[![Módulo](https://img.shields.io/badge/modulo-01-2563eb)](./)
[![Concepto](https://img.shields.io/badge/concepto-prompt%20%2B%20modelo-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Comparar generación simple, temperatura baja, temperatura alta y un prompt con rol de asistente educativo.

## Problema

Un LLM local recibe un `prompt` y devuelve una continuación. Antes de construir chats, RAG o agentes, conviene ver esta interacción sin capas extra.

## Idea clave

El modelo no ejecuta reglas escritas por nosotros. Predice una salida probable a partir del texto de entrada. Por eso el prompt y parámetros como `temperature` cambian tanto el resultado.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Configurar `MODEL` | Centralizar el modelo de Ollama que usará la práctica. |
| 2 | Enviar un prompt corto | Ver la forma más simple de generación. |
| 3 | Cambiar `temperature` | Observar respuestas más repetibles o más variadas. |
| 4 | Mejorar el prompt | Definir rol, público y longitud esperada. |

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

- Cambia `llama3.2` por `qwen2.5:1.5b` si necesitas un modelo más ligero.
- Pide la misma tarea con `temperature=0.0` y `temperature=1.5`.
- Agrega restricciones de formato, como responder en tres viñetas o en una sola oración.

## Siguiente módulo

Continúa con [`02_chat_conversacion`](../02_chat_conversacion) para ver **Chat conversacional**.
