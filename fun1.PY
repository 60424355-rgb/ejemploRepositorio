def saludo(nombre):
    for i in range(1, 10):
        print(f"HOLA {nombre}")

def sumar(a, b):
    suma = a + b
    return suma

print("PROGRAMA PRINCIPAL")
nombre = input("y tu como te llamas?")
saludo(nombre)
saludo("Tony")

resultado = sumar(4, 6)
print(f"RESULTADO: {resultado}")
print(f"otra suma 65 + 12: {65 + 12}")