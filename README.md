# Local-LLM: Taller de Modelos de Lenguaje Locales

Taller práctico de 2 horas sobre fundamentos de LLMs y cómo ejecutarlos localmente con Ollama.

## Propósito

Este taller busca que estudiantes de ingeniería en computación e informática:

1. **Entiendan** cómo funcionan los modelos de lenguaje a nivel conceptual
2. **Ejecuten** modelos pequeños localmente sin depender de APIs de pago
3. **Desarrollen** aplicaciones que potencien al LLM con herramientas (¡superpoderes!)
4. **Comprendan** que un LLM solo genera texto — somos quienes le damos capacidades reales mediante programación

## Lo que aprenderán

| Ejemplo | Concepto | Notebook | Script |
|---------|----------|----------|--------|
| Generación básica | Qué es un LLM y cómo genera texto | `01_generacion_basica/notebook.ipynb` | `01_generacion_basica/ejemplo.py` |
| Chat conversacional | Cómo mantener contexto en una conversación | `02_chat_conversacion/notebook.ipynb` | `02_chat_conversacion/ejemplo.py` |
| Salida estructurada | Cómo forzar al modelo a responder en JSON | `03_salida_estructurada/notebook.ipynb` | `03_salida_estructurada/ejemplo.py` |
| Embeddings | Cómo los textos se convierten en vectores | `04_embeddings_similitud/notebook.ipynb` | `04_embeddings_similitud/ejemplo.py` |
| RAG simple | Cómo darle contexto propio al modelo | `05_rag_simple/notebook.ipynb` | `05_rag_simple/ejemplo.py` |
| Agente con herramientas | Cómo dotar al LLM de superpoderes | `06_agente_con_herramientas/notebook.ipynb` | `06_agente_con_herramientas/ejemplo.py` |

## Herramientas necesarias

### 1. Ollama (obligatorio)

Ollama es el motor que corre los modelos localmente.

```bash
# Instalar Ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# En macOS, descargar desde https://ollama.com/download
# En Windows, descargar desde https://ollama.com/download
```

### 2. Descargar un modelo

```bash
# Modelo principal del taller (~2GB, corre en 4GB+ RAM)
ollama pull llama3.2

# Alternativa más pequeña (~1GB, corre en 2GB+ RAM)
ollama pull qwen2.5:1.5b
```

### 3. Python 3.8+ (obligatorio)

Verificar que tengan Python instalado:

```bash
python3 --version
```

### 4. Bibliotecas Python

```bash
pip install -r requirements.txt
```

### 5. Verificar que todo funciona

```bash
# Verificar que Ollama está corriendo
ollama list

# Probar el modelo desde terminal
ollama run llama3.2 "Hola, ¿cómo estás?"
```

## Cómo usar este repositorio

1. Instalar las dependencias (Ollama + bibliotecas Python)
2. Abrir los notebooks en orden para ver el paso a paso de cada concepto
3. Ejecutar los scripts cuando solo quieras correr la versión directa
4. Modificar, experimentar y hacer pruebas — así se aprende

```bash
jupyter lab
```

Cada carpeta incluye:

- `README.md`: mini explicación del problema.
- `notebook.ipynb`: explicación guiada con celdas independientes.
- `ejemplo.py`: código compacto para ejecución directa.

```bash
python3 01_generacion_basica/ejemplo.py
python3 02_chat_conversacion/ejemplo.py
python3 03_salida_estructurada/ejemplo.py
python3 04_embeddings_similitud/ejemplo.py
python3 05_rag_simple/ejemplo.py
python3 06_agente_con_herramientas/ejemplo.py
```

## Requisitos de hardware

| Modelo | RAM mínima | RAM recomendada |
|--------|-----------|----------------|
| qwen2.5:0.5b | 2 GB | 4 GB |
| qwen2.5:1.5b | 2 GB | 4 GB |
| llama3.2:1b | 2 GB | 4 GB |
| llama3.2:3b | 4 GB | 8 GB |
| mistral:7b | 8 GB | 16 GB |

> **Nota:** Si tu computadora tiene 8GB de RAM o menos, usa `qwen2.5:1.5b` o `llama3.2:1b`.

## Ideas para proyectos posteriores

- Clasificador automático de correos o tickets de soporte
- Asistente de estudio que responda preguntas sobre tus notas (RAG)
- Generador de datos sintéticos para pruebas
- Chatbot con acceso a APIs externas (clima, calculadora, base de datos)
- Extractor de información estructurada desde texto libre
