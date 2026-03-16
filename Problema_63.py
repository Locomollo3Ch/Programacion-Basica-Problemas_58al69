# Problema 63

def cuadrados_de_lista(lista_original):
    lista_cuadrados = []
    for numero in lista_original:
        lista_cuadrados.append(numero ** 2)
    return lista_cuadrados

numeros_usuario = []

while True:
    entrada = input("Ingresa un número para tu lista (o 'fin' para terminar):\n")
    if entrada.lower() == 'fin':
        break
    try:
        numeros_usuario.append(float(entrada))
    except ValueError:
        print("Ingresa solo números válidos.")

if len(numeros_usuario) > 0:
    resultados = cuadrados_de_lista(numeros_usuario)
    print(f"\nTu lista original: {numeros_usuario}")
    print(f"La lista con sus cuadrados: {resultados}")
else:
    print("\nNo ingresaste ningún número.")