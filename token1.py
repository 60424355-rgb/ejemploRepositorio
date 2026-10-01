from huggingface_hub import InferenceClient

# Reemplaza con tu token personal (HF_TOKEN)
HF_TOKEN = "hf_tu_token_aqui"

# Instanciamos el cliente
client = InferenceClient(token=HF_TOKEN)

# 1. Clasificación de sentimientos enviando la petición a la nube
resultado = client.text_classification(
    text="¡Esta herramienta facilita muchísimo el trabajo!",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print(resultado)
# Salida esperada: [{'label': 'POSITIVE', 'score': 0.99...}]