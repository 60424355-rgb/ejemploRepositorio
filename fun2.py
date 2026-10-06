#   Reescribiendo el ejemplo1 con funciones DEF
#BLOQUE IF
def detectarTemperatura(lectura,consigna):
    if lectura == consigna:
        #Acciones si es verdadero.
        print("es verdad, estoy dentro de la estructura de control IF")
        lectura=lectura+3
        print(f"temperatura: {lectura}")
    
    else:
        #Acciones si es falso.
        print("la temperatura no es igual a 17")
        lectura=lectura-1
        print(f"temperatura: {lectura}")

detectarTemperatura(10,18)
detectarTemperatura(25,30)
detectarTemperatura(30,50)