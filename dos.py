import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Modelo BERT especializado en español
MODEL_NAME = "pysentimiento/robertuito-sentiment-analysis"

# 1. Cargamos el Tokenizer y el Modelo específicos
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

texto = "no me gusta el color de la caja"

# paso A: TOKENIZACIÓN
# 'return_tensors="pt"' devuelve tensores de PyTorch
inputs = tokenizer(texto, return_tensors="pt")
print("Input IDs (representación numérica):", inputs["input_ids"])

# paso B: EJECUCIÓN DEL MODELO (Inferencia)
with torch.no_grad():
    outputs = model(**inputs)

# paso C: POSPROCESAMIENTO
# Los logits son las salidas brutas antes de convertirlas a probabilidades
logits = outputs.logits
probabilidades = torch.softmax(logits, dim=-1)

# Obtener la clase predicha
prediccion_id = torch.argmax(probabilidades).item()
etiqueta = model.config.id2label[prediccion_id]

print(f"Predicción: {etiqueta} con confianza de {probabilidades[0][prediccion_id]:.4f}")