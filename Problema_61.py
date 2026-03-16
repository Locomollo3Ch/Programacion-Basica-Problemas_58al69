# Problema 61

def calcular_perimetro_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    return perimetro

try:
    entrada_base =float(input("Ingresa el valor de la base:\n"))     
    entrada_altura = float(input("Ingresa el valor de la altura:\n"))

    resultado_perimetro = calcular_perimetro_rectangulo(entrada_base, entrada_altura)
    print(f"\nEl perímetro del rectángulo es: {resultado_perimetro}")

except ValueError:
    print("Ingresar únicamente números válidos.")