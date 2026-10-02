from transformers import pipeline

# 1. Creamos un pipeline especificado para "clasificación de sentimiento"
clasificador = pipeline(
    task="text-classification",
    model="pysentimiento/robertuito-sentiment-analysis"
)

# 2. Pasamos el texto
resultado = clasificador("me molesta que llamen tan seguido")

print(resultado)
# Salida esperada: [{'label': 'POSITIVE', 'score': 0.99...}]