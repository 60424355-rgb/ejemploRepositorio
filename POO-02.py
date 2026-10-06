class Personaje:
    # El método __init__ es el constructor: define los atributos iniciales
    def __init__(self, nombre, vida):
        self.nombre = nombre  # Atributo
        self.vida = vida      # Atributo

# Creación de objetos (Instanciación)
p1 = Personaje("Aragorn", 100)
p2 = Personaje("Legolas", 80)

# Acceso directo a los atributos
print(f"Personaje 1: {p1.nombre} | Vida: {p1.vida}")
print(f"Personaje 2: {p2.nombre} | Vida: {p2.vida}")

# 'p1' y 'p2' son independientes; modificar 'p1' no altera a 'p2'.