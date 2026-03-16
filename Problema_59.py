# Problema 59

def sumatoria():
    try:
        inicio = int(input('Ingrese el número inicial:\n'))
        fin = int(input('Ingrese el número final:\n'))

        if inicio > fin:
            print("El número inicial debe ser menor al final.")
            return 0
        
        Suma = 0

        for i in range(inicio, fin + 1):
            Suma += i
        
        return Suma
        
    except ValueError:
        print("Error: Ingresar números enteros.")
        return 0

resultado = sumatoria()
print(f"El resultado es: {resultado}")