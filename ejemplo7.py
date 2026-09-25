nombre=input("ingresa un nombre de animal en plural")
archivo=open("mi_arvhivo.txt", "a")
archivo.write(f"Tres tigres {nombre}\n")
archivo.close()