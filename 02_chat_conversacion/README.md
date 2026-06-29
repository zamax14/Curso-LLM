# 02 - Chat conversacional

## Problema

Un llamado aislado al modelo no tiene memoria de lo que se dijo antes. Para construir un chat, la aplicación debe enviar el historial completo de mensajes relevantes.

## Idea clave

La memoria conversacional no aparece sola dentro del modelo. Se representa como una lista de mensajes con roles: `system`, `user` y `assistant`.

## Archivos

- `notebook.ipynb`: muestra la diferencia entre llamar al modelo sin historial y con historial.
- `ejemplo.py`: ejecuta una demostración corta; también puede abrir un chat interactivo.

## Ejecutar

```bash
python3 ejemplo.py
python3 ejemplo.py --interactive
```

Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado.
