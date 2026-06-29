# 05 - RAG simple

## Problema

Un LLM local puede responder con conocimiento general, pero no conoce documentos privados, notas de clase o datos recientes que no estén dentro del prompt.

## Idea clave

RAG combina dos pasos: primero busca fragmentos relevantes con embeddings y después genera una respuesta usando solo ese contexto.

## Archivos

- `notebook.ipynb`: construye el flujo de RAG paso a paso.
- `ejemplo.py`: ejecuta una versión compacta del sistema.

## Ejecutar

```bash
python3 ejemplo.py
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
