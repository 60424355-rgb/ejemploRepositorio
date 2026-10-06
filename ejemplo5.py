#MODIFICAR PARA LEER NUMERO POR TEECLADO.
#Y OPERAR: 1=> suma, 2=>resta, 3=> multiplicaciion
print ("calcular\n Ingresa: Ingresa 2 numeros")
numero1 = int(input("ingresa el primer numero:"))
numero2 = int(input("ingresa el segundo numero:"))
print ("Selecciona operaciones: 1=> suma, 2=>resta, 3=> multiplicaciion")
opcion= int(input("Ingresa una opcion"))
match opcion:
    case 1:   
     print (f"SUMA")
     print(f"Resultado: {numero1+numero2}")
    case 2:
     print (f"RESTA")
     print(f"Resultado: {numero1-numero2}")
    case 3:
     print (f"MULTIPLICACION")
     print(f"Resultado: {numero1*numero2}")
    case 5:
     print (f"SUMA")
     print(f"Resultado: {numero1+numero2}")
    case _:    
     print(f"Ninguna opcion {opcion}")
