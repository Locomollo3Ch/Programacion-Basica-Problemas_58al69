# Problema 68

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

try:
    num_usuario = int(input("Ingresa un número entero para verificar si es primo:\n"))
    if es_primo(num_usuario):
        print(f"{num_usuario} SÍ es primo.")
    else:
        print(f"{num_usuario} NO es primo.")
except ValueError:
    print("Debes ingresar un número entero válido.")