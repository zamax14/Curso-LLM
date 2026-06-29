<div align="center">

# 04 - Embeddings y similitud

**Buscar por significado, no solamente por palabras exactas.**

[![Módulo](https://img.shields.io/badge/modulo-04-0891b2)](./)
[![Concepto](https://img.shields.io/badge/concepto-texto%20%E2%86%92%20vectores-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Inspeccionar un vector, construir una matriz de similitud y crear un buscador semántico pequeño.

## Problema

Dos textos pueden decir lo mismo con palabras distintas. La búsqueda literal falla en esos casos, pero los embeddings permiten comparar significado numéricamente.

## Idea clave

Un embedding representa un texto como vector. La similitud coseno compara vectores y ayuda a ordenar textos por cercanía semántica.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Generar un embedding | Ver tamaño y primeros valores del vector. |
| 2 | Comparar frases | Detectar frases similares aunque usen vocabulario distinto. |
| 3 | Crear una base simple | Guardar textos y sus embeddings. |
| 4 | Buscar por consulta | Recuperar los documentos más parecidos. |

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

- Agrega frases muy parecidas y frases completamente ajenas.
- Cambia `top_k` para recuperar más o menos resultados.
- Usa textos de una materia real para convertirlo en un mini buscador.

## Siguiente módulo

Continúa con [`05_rag_simple`](../05_rag_simple) para ver **RAG simple**.
