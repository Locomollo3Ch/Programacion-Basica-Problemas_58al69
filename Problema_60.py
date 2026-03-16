# Problema 60

def funcion_sumatoria(lista_numeros):
    total = 0
    for numero in lista_numeros:
        total += numero
    return total

def funcion_promedio(lista_numeros):
    if len(lista_numeros) == 0:
        return 0
    suma_total = funcion_sumatoria(lista_numeros)
    cantidad_elementos = len(lista_numeros)
    return suma_total / cantidad_elementos

datos_usuario = []

print("=== Calculadora de Promedios ===")
print("Ingresa los números uno por uno. Escribe la palabra 'fin' cuando hayas terminado.\n")

while True:
    entrada = input("Ingresa un número (o 'fin' para calcular): ")
    
    if entrada.lower() == 'fin':
        break 
    
    try:
        numero_convertido = float(entrada)
        datos_usuario.append(numero_convertido)
    except ValueError:
        print("Por favor, ingresa solo números o la palabra 'fin'.")

print("\n=== Resultados ===")
if len(datos_usuario) > 0:
    mi_promedio = funcion_promedio(datos_usuario)
    print(f"Tus datos ingresados: {datos_usuario}")
    print(f"La sumatoria total es: {funcion_sumatoria(datos_usuario)}")
    print(f"El promedio calculado es: {mi_promedio}")
else:
    print("No ingresaste ningún número para calcular.")