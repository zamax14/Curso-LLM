<div align="center">

# Local-LLM

**Taller práctico de modelos de lenguaje locales con Python, Ollama y notebooks guiados**

[![Curso](https://img.shields.io/badge/curso-IA%20aplicada-2563eb)](#local-llm)
[![Duración](https://img.shields.io/badge/duracion-2%20horas-16a34a)](#ruta-del-taller)
[![Runtime](https://img.shields.io/badge/runtime-local%20LLM-7c3aed)](#herramientas-necesarias)
[![Python](https://img.shields.io/badge/python-3.8%2B-111827)](#herramientas-necesarias)

</div>

---

## Vista rápida

Este repositorio acompaña un curso de verano sobre temas de IA. Esta sesión se enfoca en una pregunta concreta: **¿qué podemos construir cuando ejecutamos un LLM en nuestra propia computadora?**

> [!IMPORTANT]
> La idea central del taller es que un LLM solo genera texto. Las capacidades útiles aparecen cuando lo conectamos con código: memoria, JSON, búsqueda semántica, documentos y herramientas.

| En clase se ve | Se practica con | Resultado esperado |
|---|---|---|
| Modelos locales | Ollama + `llama3.2` | Ejecutar prompts sin APIs externas |
| Conversación | Historial de mensajes | Simular memoria de chat |
| Datos estructurados | JSON validado en Python | Respuestas listas para una app |
| Búsqueda semántica | Embeddings + similitud coseno | Encontrar texto por significado |
| RAG | Contexto recuperado + generación | Responder sobre datos propios |
| Agentes | Tool calling + funciones Python | Darle acciones reales al modelo |

## Ruta del taller

| Módulo | Tema | Pregunta que responde | Notebook | Script |
|---:|---|---|---|---|
| 01 | Generación básica | ¿Cómo responde un LLM a un prompt? | [`notebook.ipynb`](01_generacion_basica/notebook.ipynb) | [`ejemplo.py`](01_generacion_basica/ejemplo.py) |
| 02 | Chat conversacional | ¿De dónde sale la memoria de un chat? | [`notebook.ipynb`](02_chat_conversacion/notebook.ipynb) | [`ejemplo.py`](02_chat_conversacion/ejemplo.py) |
| 03 | Salida estructurada | ¿Cómo convierto texto en datos útiles? | [`notebook.ipynb`](03_salida_estructurada/notebook.ipynb) | [`ejemplo.py`](03_salida_estructurada/ejemplo.py) |
| 04 | Embeddings y similitud | ¿Cómo busco por significado? | [`notebook.ipynb`](04_embeddings_similitud/notebook.ipynb) | [`ejemplo.py`](04_embeddings_similitud/ejemplo.py) |
| 05 | RAG simple | ¿Cómo hago que responda sobre mis documentos? | [`notebook.ipynb`](05_rag_simple/notebook.ipynb) | [`ejemplo.py`](05_rag_simple/ejemplo.py) |
| 06 | Agente con herramientas | ¿Cómo hago que el LLM use funciones? | [`notebook.ipynb`](06_agente_con_herramientas/notebook.ipynb) | [`ejemplo.py`](06_agente_con_herramientas/ejemplo.py) |

```mermaid
flowchart LR
    A[Prompt] --> B[Chat]
    B --> C[JSON]
    C --> D[Embeddings]
    D --> E[RAG]
    E --> F[Agentes]
```

## Herramientas necesarias

| Herramienta | Para qué se usa | Comando de verificación |
|---|---|---|
| Ollama | Ejecutar el modelo local | `ollama list` |
| Modelo local | Generar texto y embeddings | `ollama run llama3.2 "Hola"` |
| Python 3.8+ | Correr scripts y notebooks | `python3 --version` |
| JupyterLab | Explorar las prácticas paso a paso | `jupyter lab` |

### Instalar Ollama

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh
```

En macOS y Windows, descargar desde <https://ollama.com/download>.

### Descargar un modelo

```bash
# Modelo principal del taller (~2GB, corre en 4GB+ RAM)
ollama pull llama3.2

# Alternativa más ligera (~1GB, corre en 2GB+ RAM)
ollama pull qwen2.5:1.5b
```

### Instalar dependencias Python

```bash
pip install -r requirements.txt
```

## Cómo usar el repositorio

> [!TIP]
> Para clase, abre primero los notebooks. Para repetir la demo rápido, ejecuta los scripts.

| Quiero... | Entonces uso... |
|---|---|
| Entender el paso a paso | `notebook.ipynb` |
| Probar una celda y cambiar parámetros | `jupyter lab` |
| Correr la demo completa sin explicación | `ejemplo.py` |
| Preparar una presentación | Las carpetas numeradas en orden |

```bash
jupyter lab
```

```bash
python3 01_generacion_basica/ejemplo.py
python3 02_chat_conversacion/ejemplo.py
python3 03_salida_estructurada/ejemplo.py
python3 04_embeddings_similitud/ejemplo.py
python3 05_rag_simple/ejemplo.py
python3 06_agente_con_herramientas/ejemplo.py
```

## Estructura de cada módulo

```text
0x_nombre_del_modulo/
├── README.md       # ficha visual del problema y la práctica
├── ejemplo.py      # versión directa para terminal
└── notebook.ipynb  # explicación guiada para clase
```

## Requisitos de hardware

| Modelo | RAM mínima | RAM recomendada | Uso sugerido |
|---|---:|---:|---|
| `qwen2.5:0.5b` | 2 GB | 4 GB | Computadoras limitadas |
| `qwen2.5:1.5b` | 2 GB | 4 GB | Alternativa rápida |
| `llama3.2:1b` | 2 GB | 4 GB | Taller ligero |
| `llama3.2:3b` | 4 GB | 8 GB | Modelo principal |
| `mistral:7b` | 8 GB | 16 GB | Equipos con más memoria |

> [!NOTE]
> Si tu computadora tiene 8 GB de RAM o menos, usa `qwen2.5:1.5b` o `llama3.2:1b`.

## Ideas para proyectos posteriores

| Proyecto | Módulos que reutiliza |
|---|---|
| Clasificador automático de correos o tickets | 03 + 06 |
| Asistente de estudio con apuntes propios | 04 + 05 |
| Generador de datos sintéticos para pruebas | 01 + 03 |
| Chatbot con APIs externas | 02 + 06 |
| Extractor de información desde texto libre | 03 |
