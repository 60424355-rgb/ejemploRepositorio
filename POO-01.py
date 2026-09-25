# Variables independientes para un personaje de videojuego
nombre_p1 = "Aragorn"
vida_p1 = 100

nombre_p2 = "Legolas"
vida_p2 = 80

# Función externa para aplicar daño
def recibir_dano(vida_actual, cantidad):
    return vida_actual - cantidad

# Modificar el estado requiere reasignar variables manualmente
vida_p1 = recibir_dano(vida_p1, 30)
print(f"{nombre_p1} tiene {vida_p1} de vida.")

# Si agregamos 50 personajes o más atributos (fuerza, mana, nivel), 
# mantener el código con variables sueltas se vuelve inmanejable.