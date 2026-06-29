# 03 - Salida estructurada

## Problema

El modelo genera texto libre, pero muchas aplicaciones necesitan datos con una forma estable: JSON, campos obligatorios, números y etiquetas.

## Idea clave

Un prompt puede pedir JSON, pero `format="json"` en Ollama aumenta la confiabilidad porque obliga al modelo a responder con JSON válido.

## Archivos

- `notebook.ipynb`: compara texto libre, prompt con JSON y JSON forzado por Ollama.
- `ejemplo.py`: ejecuta los casos principales de forma compacta.

## Ejecutar

```bash
python3 ejemplo.py
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
