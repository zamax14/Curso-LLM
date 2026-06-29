# 04 - Embeddings y similitud

## Problema

Buscar por palabras exactas falla cuando dos textos dicen lo mismo con vocabulario distinto. Los embeddings permiten comparar significado de forma numérica.

## Idea clave

Un embedding convierte texto en un vector. Si dos textos tienen significado parecido, sus vectores suelen quedar cerca. La similitud coseno mide esa cercanía.

## Archivos

- `notebook.ipynb`: inspecciona un vector, calcula similitudes y arma un buscador semántico pequeño.
- `ejemplo.py`: corre la demostración completa desde terminal.

## Ejecutar

```bash
python3 ejemplo.py
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
