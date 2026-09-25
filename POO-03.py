class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    # Método para modificar la vida del propio objeto (self)
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        print(f"{self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")

    def curar(self, cantidad):
        self.vida += cantidad
        print(f"{self.nombre} se curó {cantidad} puntos. Vida actual: {self.vida}")

# Uso
p1 = Personaje("Aragorn", 100)
p1.recibir_dano(30)  # El objeto maneja su propia lógica interna
p1.curar(15)