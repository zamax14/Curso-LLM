<div align="center">

# 02 - Chat conversacional

**Convertir llamadas aisladas al modelo en una conversación con contexto.**

[![Módulo](https://img.shields.io/badge/modulo-02-16a34a)](./)
[![Concepto](https://img.shields.io/badge/concepto-mensajes%20%2B%20memoria-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Mostrar que el modelo no recuerda un nombre sin historial y luego sí puede usarlo cuando se le reenvía el contexto.

## Problema

Un llamado aislado al modelo no sabe qué se dijo antes. Si queremos una conversación, la aplicación debe guardar y reenviar el historial relevante.

## Idea clave

La memoria del chat vive en la lista de mensajes. Los roles `system`, `user` y `assistant` le dan estructura al contexto que recibe el modelo.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Enviar mensajes sueltos | Comprobar que cada llamada es independiente. |
| 2 | Crear un historial | Guardar instrucciones y mensajes previos. |
| 3 | Agregar respuestas del modelo | Mantener la conversación completa. |
| 4 | Probar modo interactivo | Chatear desde terminal o notebook. |

## Archivos del módulo

| Archivo | Uso recomendado |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | Seguir la explicación en clase, ejecutar celda por celda y modificar parámetros. |
| [`ejemplo.py`](ejemplo.py) | Correr la demo completa desde terminal, sin la explicación extendida. |
| [`README.md`](README.md) | Tener a la mano el objetivo, comandos y experimentos sugeridos. |

## Ejecutar

```bash
python3 ejemplo.py
python3 ejemplo.py --interactive
```

> [!NOTE]
> Requiere que Ollama esté corriendo y que el modelo `llama3.2` esté descargado. Si usas otro modelo, cambia la constante `MODEL` en el notebook o en el script.

## Experimentos rápidos

- Cambia el mensaje `system` para hacerlo más formal, breve o técnico.
- Borra parte del historial y observa qué deja de recordar.
- Ejecuta `python3 ejemplo.py --interactive` para probar una conversación libre.

## Siguiente módulo

Continúa con [`03_salida_estructurada`](../03_salida_estructurada) para ver **Salida estructurada**.
