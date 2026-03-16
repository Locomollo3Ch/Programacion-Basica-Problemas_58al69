# Problema 64

def EsMultiplo(num1, num2):
    return num1 % num2 == 0

try:
    numero1 = int(input("Ingresa el primer número (entero):\n"))
    numero2 = int(input("Ingresa el segundo número (entero):\n"))
    
    if numero2 == 0:
        print("Error.")
    elif EsMultiplo(numero1, numero2):
        print(f"{numero1} es múltiplo de {numero2}.")
    else:
        print(f"{numero1} no es múltiplo de {numero2}.")
except ValueError:
    print("Debes ingresar números enteros.")