import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo liviano multilingüe con excelente soporte para español
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

prompt = "El futuro de la inteligencia artificial en la educación es"

# 1. Aplicamos formato para instruir al modelo a responder en español
mensajes = [
    {"role": "system", "content": "Completa la frase redactando en español correcto y fluido."},
    {"role": "user", "content": prompt}
]
formatted_prompt = tokenizer.apply_chat_template(mensajes, tokenize=False, add_generation_prompt=True)

# 2. Tokenización
inputs = tokenizer(formatted_prompt, return_tensors="pt")

# 3. Generación
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        temperature=0.7,
        do_sample=True,
        repetition_penalty=1.2
    )

# 4. Decodificación de los nuevos tokens
texto_generado = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

print("--- Texto Generado en Español ---")
print(texto_generado)