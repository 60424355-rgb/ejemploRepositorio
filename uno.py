from transformers import pipeline

# 1. Creamos un pipeline especificado para "clasificación de sentimiento"
clasificador = pipeline(
    task="text-classification",
    model="pysentimiento/robertuito-sentiment-analysis"
)

# 2. Solicitamos el texto al usuario mediante un input
texto_usuario = input("Ingresa el texto a analizar: ")

# 3. Pasamos el texto ingresado al clasificador
resultado = clasificador(texto_usuario)

print(resultado)