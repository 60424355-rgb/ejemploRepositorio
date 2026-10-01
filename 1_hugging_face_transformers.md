# Manual Práctico de Hugging Face (`transformers`)

Este manual contiene una guía paso a paso para comenzar a utilizar modelos de Inteligencia Artificial mediante la librería `transformers` de Hugging Face en Python.

---

## Prerrequisitos e Instalación

Antes de iniciar, instala la librería base y un motor de aprendizaje profundo como PyTorch.

```bash
pip install transformers torch
```

---

## Nivel 1: El camino fácil con `pipeline`

### Concepto
El objeto **`pipeline`** es la abstracción de más alto nivel de la librería. Oculta la complejidad del preprocesamiento de datos, la inferencia de la red neuronal y el posprocesamiento de la respuesta en una sola función.

### Ejemplo de Código
```python
from transformers import pipeline

# 1. Crear el pipeline indicando la tarea deseada
# Por defecto descargará un modelo liviano preconfigurado para clasificación de sentimiento
clasificador = pipeline("text-classification")

# 2. Pasar el texto a evaluar
texto = "¡Me encanta aprender sobre inteligencia artificial!"
resultado = clasificador(texto)

# 3. Mostrar el resultado
print("Resultado:", resultado)
```

### Explicación del Resultado
La salida será una lista con un diccionario que indica:
* **`label`**: La etiqueta asignada (`POSITIVE` o `NEGATIVE`).
* **`score`**: La confianza del modelo en la respuesta (valor entre 0 y 1).

---

## Nivel 2: Control Explícito con `Tokenizer` y `Model` (`AutoClasses`)

### Concepto
En producciones más complejas es necesario controlar cada etapa de la ejecución. Bajo el capó, todo proceso requiere 3 pasos:

1. **Tokenización (Preprocesamiento):** Convierte el texto plano en números (*token IDs*) que la red neuronal entiende.
2. **Modelo (Inferencia):** Procesa los números para generar *logits* (puntuaciones numéricas brutas).
3. **Posprocesamiento:** Convierte los *logits* en probabilidades entendibles utilizando funciones matemáticas (como *Softmax*).

### Ejemplo de Código
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Definir el identificador del modelo en Hugging Face Hub
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# 2. Cargar el Tokenizer y el Modelo usando AutoClasses
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

texto = "Hugging Face makes using NLP models extremely easy."

# Paso A: TOKENIZACIÓN
# 'return_tensors="pt"' especifica que la salida sea un Tensor de PyTorch
inputs = tokenizer(texto, return_tensors="pt")
print("Tokens convertidos a IDs numéricos:", inputs["input_ids"])

# Paso B: INFERENCIA
with torch.no_grad():
    outputs = model(**inputs)

# Paso C: POSPROCESAMIENTO
logits = outputs.logits
probabilidades = torch.softmax(logits, dim=-1)

# Determinar la clase con mayor probabilidad
prediccion_id = torch.argmax(probabilidades).item()
etiqueta = model.config.id2label[prediccion_id]

print(f"Predicción final: {etiqueta} (Confianza: {probabilidades[0][prediccion_id]:.4f})")
```

---

## Nivel 3: Generación de Texto con LLMs (`AutoModelForCausalLM`)

### Concepto
Para tareas de Modelos de Lenguaje Grandes (LLMs) como GPT o Qwen, la tarea cambia a **Modelado Causal del Lenguaje** (*Causal Language Modeling*). El modelo predice de forma autorregresiva el token más probable que sigue a una secuencia de texto.

### Ejemplo de Código
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

# Usamos GPT-2 como modelo liviano de generación
MODEL_NAME = "gpt2"

# 1. Cargar el Tokenizer y el Modelo Causal
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

prompt = "In the future, artificial intelligence will"

# 2. Convertir el texto de entrada a IDs de tokens
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 3. Generar texto
output_ids = model.generate(
    input_ids,
    max_length=40,          # Longitud máxima total (entrada + salida)
    num_return_sequences=1,  # Cantidad de respuestas a generar
    no_repeat_ngram_size=2   # Evita repetición exacta de secuencias de palabras
)

# 4. Decodificar de tokens numéricos a texto legible
texto_generado = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("--- Texto Generado ---")
print(texto_generado)
```

---

## Resumen de Términos Fundamentales

* **Hugging Face Hub:** El repositorio web público (`huggingface.co/models`) donde se alojan pesos y configuraciones de modelos.
* **`from_pretrained()`:** Método universal utilizado para descargar e inicializar clases (`AutoModel`, `AutoTokenizer`, etc.).
* **Tokenizer:** El puente entre el texto de los humanos y la representación numérica que consumen las redes neuronales.
* **Logits:** Las puntuaciones numéricas brutas producidas por la última capa de un modelo antes de pasar por una función de activación.