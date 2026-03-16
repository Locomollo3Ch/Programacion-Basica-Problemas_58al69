# Problema 67

def creciente(lista):
    lista_ord = lista.copy()
    lista_ord.sort()
    return lista_ord

def decreciente(lista):
    lista_ord = lista.copy()
    lista_ord.sort(reverse=True)
    return lista_ord

def por_indice(lista, indice):
    return lista.pop(indice)

def por_dato(lista, dato):
    if dato in lista:
        lista.remove(dato)
    return lista

def calcular_estadisticas(lista):
    return sum(lista) / len(lista), max(lista), min(lista)

mis_datos = []
print("Arma tu lista de números. Escribe 'fin' para terminar.")
while True:
    entrada = input("Ingresa un número:\n")
    if entrada.lower() == 'fin':
        break
    try:
        mis_datos.append(float(entrada))
    except ValueError:
        print("Ingresa solo números.")
if len(mis_datos) > 0:
    print(f"\nLista original: {mis_datos}")
    print(f"Orden creciente: {creciente(mis_datos)}")
    print(f"Orden decreciente: {decreciente(mis_datos)}")
    
    prom, val_max, val_min = calcular_estadisticas(mis_datos)
    print(f"Estadísticas -> Promedio: {prom:.2f}, Máximo: {val_max}, Mínimo: {val_min}")
    try:
        dato_a_borrar = float(input("Ingresa un número de tu lista que quieras eliminar (remove):\n"))
        mis_datos = por_dato(mis_datos, dato_a_borrar)
        print(f"Lista tras intentar borrar {dato_a_borrar}: {mis_datos}")
    except ValueError:
        print("Entrada inválida.")
        
    if len(mis_datos) > 0:
        try:
            indice_a_borrar = int(input(f"Ingresa un índice (0 a {len(mis_datos)-1}) para eliminar (pop):\n"))
            eliminado = por_indice(mis_datos, indice_a_borrar)
            print(f"Se eliminó el valor {eliminado}. Lista final: {mis_datos}")
        except (ValueError, IndexError):
            print("Índice inválido o fuera de rango.")