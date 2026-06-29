# 06 - Agente con herramientas

## Problema

Un LLM genera texto, pero no calcula con precisión, no consulta inventarios reales y no obtiene datos externos por sí solo.

## Idea clave

Un agente conecta el modelo con funciones de Python. El modelo decide qué herramienta necesita, el programa ejecuta esa función y luego devuelve el resultado al modelo para que conteste.

## Archivos

- `notebook.ipynb`: separa definición de herramientas, llamada del modelo y ciclo de ejecución.
- `ejemplo.py`: corre una demostración completa del agente.

## Ejecutar

```bash
python3 ejemplo.py
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
