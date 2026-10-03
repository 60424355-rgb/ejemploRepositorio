from transformers import pipeline

# 1. Cargar el pipeline de clasificación de sentimiento en español
# (Especificamos el modelo explícitamente para evitar advertencias)
clasificador = pipeline(
    task="text-classification",
    model="pysentimiento/robertuito-sentiment-analysis"
)

# Datos de prueba para el bucle
comentarios = [
    "¡Excelente servicio y entrega muy rápida!",
    "SKIP",  # Texto comodín para probar 'continue'
    "El producto llegó dañado y no funciona.",
    "",      # Texto vacío para probar validaciones
    "Es un producto normal, cumple con su función.",
    "PARAR", # Texto comodín para probar 'break'
    "Me encantó todo de esta compra."
]

print("=== INICIO DE PROCESAMIENTO CON BUCLE FOR ===")

# ------------------------------------------------------------------
# BUCLE FOR: Recorre una lista finita de elementos
# ------------------------------------------------------------------
for indice, texto in enumerate(comentarios, start=1):

    # SENTENCIA DE CONTROL: Evitar cadenas vacías o sin texto válido
    if not texto.strip():
        print(f"[{indice}] Comentario vacío detectado -> Omitiendo...")
        continue  # CONTINUE: Salta inmediatamente a la siguiente iteración

    # SENTENCIA DE CONTROL: Detener la ejecución si se detecta la palabra clave 'PARAR'
    if texto == "PARAR":
        print(f"[{indice}] Se encontró la instrucción 'PARAR' -> Interrumpiendo el bucle.")
        break  # BREAK: Termina el bucle por completo

    # SENTENCIA DE CONTROL: Omitir elementos no deseados con 'SKIP'
    if texto == "SKIP":
        print(f"[{indice}] Marca 'SKIP' detectada -> Saltando elemento.")
        continue

    # Inferencia con la librería transformers
    resultado = clasificador(texto)[0]
    etiqueta = resultado["label"]
    confianza = resultado["score"]

    # --------------------------------------------------------------
    # SENTENCIAS CONDICIONALES: IF / ELIF / ELSE
    # Categorizamos la respuesta según la etiqueta del modelo
    # --------------------------------------------------------------
    if etiqueta == "POS":
        sentimiento = "Positivo"
    elif etiqueta == "NEG":
        sentimiento = "Negativo"
    else: # "NEU"
        sentimiento = "Neutro"

    print(f"[{indice}] Comentario: \"{texto}\" -> Sentimiento: {sentimiento} (Confianza: {confianza:.2%})")


print("\n=== PROCESAMIENTO INTERACTIVO CON BUCLE WHILE ===")

# ------------------------------------------------------------------
# BUCLE WHILE: Se ejecuta mientras una condición sea verdadera (True)
# ------------------------------------------------------------------
cola_de_espera = ["Atención pésima", "Servicio aceptable", "FIN"]

while len(cola_de_espera) > 0:
    comentario_actual = cola_de_espera.pop(0)

    if comentario_actual == "FIN":
        print("Finalizando el procesamiento con 'while'.")
        break

    prediccion = clasificador(comentario_actual)[0]
    print(f"Procesado de la cola: \"{comentario_actual}\" -> Etiqueta: {prediccion['label']}")