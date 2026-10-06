import keyboard
import time

porcentaje = 0

print("¡Robot encendido! Presiona la tecla ESC para detenerlo.\n")

while True:
    porcentaje += 25
    print(f"CARGANDO... {porcentaje}%")
    time.sleep(5)

    # Si el robot siente que presionaste 'esc', se rompe el bucle
    if keyboard.is_pressed('esc'):
        print("\n¡Tocaste la tecla ESC! El robot se detuvo.")
        break

print("Fin del juego.")   