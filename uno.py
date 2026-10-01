from transformers import pipeline

# 1. Creamos un pipeline especificado para "clasificación de sentimiento"
clasificador = pipeline("text-classification")

# 2. Pasamos el texto
resultado = clasificador("¡Me encanta aprender sobre inteligencia artificial!")

print(resultado)
# Salida esperada: [{'label': 'POSITIVE', 'score': 0.99...}]