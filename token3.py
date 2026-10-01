import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

HF_TOKEN = "hf_tu_token_aqui"

# Modelo "Gated": Requiere aceptar términos en https://huggingface.co/google/gemma-2-2b-it
MODEL_NAME = "google/gemma-2-2b-it"

# 1. Cargamos el Tokenizer pasando el token de autorización
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)

# 2. Cargamos el Modelo verificando credenciales
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, 
    token=HF_TOKEN,
    torch_dtype=torch.float16, # Optimización de memoria
    device_map="auto"          # Asigna automáticamente GPU/CPU
)

prompt = "Explica qué es un API Key en dos oraciones."

# 3. Preparación de entradas e inferencia local
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=60)

respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(respuesta)