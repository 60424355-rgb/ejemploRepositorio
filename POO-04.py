class Personaje:
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        self.vida_maxima = vida_maxima
        self.__vida = vida_maxima  # Atributo privado (encapsulado)

    def recibir_dano(self, cantidad):
        self.__vida -= cantidad
        if self.__vida < 0:
            self.__vida = 0
        print(f"{self.nombre} recibió {cantidad} de daño. Vida: {self.__vida}/{self.vida_maxima}")

    def curar(self, cantidad):
        if self.__vida > 0:
            self.__vida = min(self.vida_maxima, self.__vida + cantidad)
            print(f"{self.nombre} se curó. Vida: {self.__vida}/{self.vida_maxima}")
        else:
            print(f"{self.nombre} está derrotado y no se puede curar.")

    # Getter para consultar el estado sin modificarlo directamente
    def obtener_vida(self):
        return self.__vida

# Pruebas de control de estado
p1 = Personaje("Aragorn", 100)
p1.recibir_dano(150)  # La vida no bajará de 0
p1.curar(20)          # No se puede curar porque ya fue derrotado