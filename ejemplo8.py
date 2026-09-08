import keyboard
import time

archivo = open("archivoreto.txt", "w")  
linea=0

while True:
    print("👺****\n")
    archivo.write(f"{linea} ---> *********\n")
    linea +=1

    if keyboard.is_pressed('esc'):
        print("\n¡Tocaste la tecla ESC! El robot se detuvo.")
        
        break
    # Logica de tu programa
    print("procesando...", end="\r")
    time.sleep(0.1)

archivo.close() 