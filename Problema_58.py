# Problema 58

def lista_numeros():
    try:
        inicio = int(input("Ingrese el número inicial:\n"))
        fin = int(input("Ingrese el número final:\n"))
        
        if inicio > fin:
            print("El número inicial debe ser menor o igual al final.")
            return []
        lista = []
        
        for i in range(inicio, fin + 1):
            lista.append(i)
        return lista

    except ValueError:
        print("Error: Debes ingresar números enteros.")
        return []

mi_lista = lista_numeros()
print("\nResultado final:", mi_lista)