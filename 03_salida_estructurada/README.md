<div align="center">

# 03 - Salida estructurada

**Hacer que una respuesta del modelo pueda entrar a una aplicación real.**

[![Módulo](https://img.shields.io/badge/modulo-03-7c3aed)](./)
[![Concepto](https://img.shields.io/badge/concepto-texto%20%E2%86%92%20JSON-111827)](./notebook.ipynb)
[![Formato](https://img.shields.io/badge/formato-notebook%20%2B%20script-16a34a)](./)

</div>

---

## En una frase

> Comparar respuesta libre, JSON pedido por prompt, JSON forzado por Ollama y un clasificador de sentimiento.

## Problema

El texto libre es útil para leer, pero incómodo para automatizar. Muchas aplicaciones necesitan campos, números, etiquetas y JSON válido.

## Idea clave

Pedir JSON en el prompt ayuda, pero `format="json"` reduce el riesgo de recibir texto mezclado con explicación. Aun así, Python debe validar la salida.

## Mapa de la práctica

| Paso | Qué se hace | Para qué sirve |
|---:|---|---|
| 1 | Generar texto libre | Ver por qué una respuesta natural no siempre sirve como dato. |
| 2 | Pedir JSON | Usar un prompt con claves esperadas. |
| 3 | Validar con `json.loads` | Confirmar que la salida es procesable. |
| 4 | Clasificar reseñas | Aplicar la técnica a un caso de uso. |

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

- Agrega nuevas claves como `razon` o `categoria`.
- Cambia las reseñas por correos, tickets o comentarios de clase.
- Prueba qué pasa si quitas `format="json"` en el clasificador.

## Siguiente módulo

Continúa con [`04_embeddings_similitud`](../04_embeddings_similitud) para ver **Embeddings y similitud**.
