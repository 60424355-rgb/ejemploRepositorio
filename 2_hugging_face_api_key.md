# Manual Práctico: Uso de API Key en Hugging Face

Este manual explica cómo interactuar con el ecosistema de Hugging Face utilizando un **Token de Acceso (API Key)** gratuito. Cubre tanto la ejecución en la nube (*Serverless Inference*) como la autenticación para modelos con licencias restringidas (*Gated Models*).

---

## Configuración Inicial y Obtención de la API Key

1. Registra una cuenta gratuita en [huggingface.co](https://huggingface.co).
2. Ve a **Settings $\rightarrow$ Access Tokens**.
3. Haz clic en **Create new token**, asígnale un nombre y selecciona el rol **Read**.
4. Copia tu token (suele comenzar con `hf_...`).

### Instalación de Librerías

```bash
pip install huggingface_hub transformers torch
```

> **Consejo de Seguridad:** Se recomienda almacenar la clave como variable de entorno en tu sistema (`export HF_TOKEN="tu_token"`) en lugar de escribirla directamente dentro de tus scripts de Python.

---

## Nivel 1: Inferencia Serverless Sencilla (`InferenceClient`)

### Concepto
La **API de Inferencia Serverless** permite enviar solicitudes a los servidores de Hugging Face para procesar tareas comunes de PLN (clasificación, extracción, traducción) sin consumir GPU o memoria RAM local, y sin descargar archivos de modelos.

### Ejemplo de Código

```python
from huggingface_hub import InferenceClient

# 1. Definir el token de acceso
HF_TOKEN = "hf_tu_token_aqui"

# 2. Inicializar el cliente de inferencia
client = InferenceClient(token=HF_TOKEN)

# 3. Realizar la clasificación de texto en la nube
resultado = client.text_classification(
    text="¡Esta herramienta facilita muchísimo el trabajo!",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 4. Mostrar la salida devuelta por el servidor
print("Resultado desde la nube:", resultado)
```

### Conceptos Clave
* **`InferenceClient`**: Módulo ligero que gestiona las peticiones HTTP hacia la infraestructura de Hugging Face.
* **Serverless Execution**: Todo el procesamiento matemático ocurre en servidores externos de manera transparente.

---

## Nivel 2: Inferencia Serverless para LLMs y Chat (`chat_completion`)

### Concepto
Hugging Face estandariza el acceso a Modelos de Lenguaje Grandes (LLMs) públicos en la nube a través de una interfaz conversacional por roles, similar a las APIs estándar de la industria.

### Ejemplo de Código

```python
from huggingface_hub import InferenceClient

HF_TOKEN = "hf_tu_token_aqui"
client = InferenceClient(token=HF_TOKEN)

# 1. Definir la estructura de la conversación
mensajes = [
    {
        "role": "system",
        "content": "Eres un asistente experto en programación Python y muy conciso."
    },
    {
        "role": "user",
        "content": "¿Cuál es la diferencia principal entre una lista y una tupla?"
    }
]

# 2. Solicitar la generación al modelo en la nube
respuesta = client.chat_completion(
    messages=mensajes,
    model="Qwen/Qwen2.5-Coder-32B-Instruct",  # Modelo servido gratuitamente
    max_tokens=200,
    temperature=0.7
)

# 3. Imprimir el contenido de la respuesta
print("--- Respuesta del LLM ---")
print(respuesta.choices[0].message.content)
```

### Conceptos Clave
* **Roles (`system`, `user`, `assistant`)**: Estructura estándar para controlar el comportamiento y contexto del modelo.
* **`temperature`**: Parámetro de creatividad; valores más bajos dan respuestas más deterministas y precisas.

---

## Nivel 3: Carga Local de Modelos Restringidos (*Gated Models*)

### Concepto
Ciertos modelos de alto rendimiento (como Llama 3, Gemma o Mistral) requieren que el usuario acepte los términos de licencia en la página del modelo antes de poder descargarlos. Para autenticar esta autorización en tu código local con `transformers`, debes proveer tu API Key.

### Ejemplo de Código

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = "hf_tu_token_aqui"

# Nombre de un modelo con acceso restringido (Gated Model)
# NOTA: Debes hacer clic en 'Accept License' previamente en su página de Hugging Face
MODEL_NAME = "google/gemma-2-2b-it"

# 1. Cargar Tokenizer autenticado
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)

# 2. Cargar Modelo autenticado
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    token=HF_TOKEN,
    torch_dtype=torch.float16,  # Optimización de memoria
    device_map="auto"           # Asignación automática de hardware (CPU/GPU)
)

# 3. Preparar la entrada e inferir localmente
prompt = "Explica qué es un API Key en dos oraciones."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=60)

# 4. Decodificar la salida
respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("--- Generación Local ---")
print(respuesta)
```

### Conceptos Clave
* **Gated Models**: Modelos almacenados en el Hub que verifican los permisos de la cuenta del usuario mediante la API Key antes de autorizar la descarga.
* **`torch_dtype` / `device_map`**: Parámetros de optimización para manejar de forma eficiente la memoria RAM o VRAM al ejecutar modelos localmente.

---

## Resumen de Modos de Uso de la API Key

| Modo | ¿Descarga pesos? | ¿Usa CPU/GPU local? | Casos de uso ideales |
| :--- | :--- | :--- | :--- |
| **Serverless (`InferenceClient`)** | No | No | Pruebas rápidas, prototipos, entornos sin tarjeta gráfica. |
| **Gated Local (`transformers`)** | Sí | Sí | Producción local, fine-tuning, privacidad de datos estricta. |