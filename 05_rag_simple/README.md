<div align="center">

# 05 - RAG simple

**Responder con contexto propio en vez de depender solo de memoria del modelo.**

[![Módulo](https://img.shields.io/badge/modulo-05-ea580c)](./)
[![Concepto](https://img.shields.io/badge/concepto-buscar%20%2B%20generar-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Construir una base de conocimiento universitaria, recuperar fragmentos relevantes y responder preguntas con el contexto encontrado.

## Problema

Un LLM local no conoce tus notas, PDFs o información privada si no se la das. RAG permite recuperar fragmentos relevantes y ponerlos dentro del prompt.

## Idea clave

RAG tiene dos movimientos: recuperar contexto con embeddings y generar una respuesta limitada a ese contexto.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Crear la base | Usar una lista de fragmentos simulando documentos. |
| 2 | Precalcular embeddings | Preparar la base para búsquedas rápidas. |
| 3 | Buscar contexto | Elegir los fragmentos más cercanos a la pregunta. |
| 4 | Generar respuesta | Contestar usando solo el contexto recuperado. |

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

- Agrega fragmentos contradictorios y observa qué recupera el sistema.
- Cambia `top_k` para ver cómo afecta la respuesta final.
- Haz preguntas cuya respuesta no esté en la base para probar el límite del contexto.

## Siguiente módulo

Continúa con [`06_agente_con_herramientas`](../06_agente_con_herramientas) para ver **Agente con herramientas**.
