from huggingface_hub import InferenceClient

HF_TOKEN = "hf_tu_token_aqui"

client = InferenceClient(token=HF_TOKEN)

# Formato de mensajes para modelos conversacionales
mensajes = [
    {"role": "system", "content": "Eres un asistente experto en programación Python y muy conciso."},
    {"role": "user", "content": "¿Cuál es la diferencia entre una lista y una tupla?"}
]

# Llamada a un modelo open-source alojado en la Inference API
respuesta = client.chat_completion(
    messages=mensajes,
    model="Qwen/Qwen2.5-Coder-32B-Instruct", # Modelo ejecutable en la API gratuita
    max_tokens=200,
    temperature=0.7
)

print(respuesta.choices[0].message.content)