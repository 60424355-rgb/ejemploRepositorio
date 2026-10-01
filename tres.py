from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo liviano para pruebas de generación
MODEL_NAME = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

prompt = "In the future, artificial intelligence will"

# 1. Convertir texto a tokens
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# 2. Generar texto adicional
output_ids = model.generate(
    input_ids, 
    max_length=40,        # Longitud máxima del texto generado
    num_return_sequences=1,
    no_repeat_ngram_size=2 # Evita repeticiones continuas
)

# 3. Decodificar tokens a texto
texto_generado = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("--- Resultado Generado ---")
print(texto_generado)