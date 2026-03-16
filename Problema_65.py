# Problema 65

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numeros_leidos = 0
while True:
    entrada = input("Ingresa un número entero positivo (o 'fin' para salir):\n")
    if entrada.lower() == 'fin':
        break
    try:
        numero = int(entrada)
        if numero < 0:
            print("El factorial no está definido para números negativos.")
        else:
            print(f"El factorial de {numero} es: {calcular_factorial(numero)}")
            numeros_leidos += 1
    except ValueError:
        print("Ingresa solo números enteros.")
        
print(f"\nTotal de números válidos procesados: {numeros_leidos}")