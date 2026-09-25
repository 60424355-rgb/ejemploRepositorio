class Personaje:
    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza

    def recibir_dano(self, cantidad):
        self.vida = max(0, self.vida - cantidad)
        print(f"{self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}")

    # Un objeto recibe a OTRO objeto como parámetro
    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo.nombre} con fuerza de {self.fuerza}!")
        objetivo.recibir_dano(self.fuerza)

# Creación de instancias e interacción
guerrero = Personaje("Aragorn", 100, 25)
orco = Personaje("Orco", 50, 10)

# Simulación de combate
guerrero.atacar(orco)
orco.atacar(guerrero)