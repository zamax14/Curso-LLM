# 01 - Generación básica

## Problema

Un LLM local recibe un texto de entrada y devuelve texto generado. El primer objetivo del taller es ver esa idea sin agregar conversación, memoria, herramientas ni documentos externos.

## Idea clave

El modelo no ejecuta reglas programadas por nosotros. Predice una continuación probable del prompt. Cambiar el prompt o parámetros como `temperature` cambia la respuesta.

## Archivos

- `notebook.ipynb`: versión guiada para clase, con pasos separados y explicaciones.
- `ejemplo.py`: versión directa para correr desde terminal.

## Ejecutar

```bash
python3 ejemplo.py
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
