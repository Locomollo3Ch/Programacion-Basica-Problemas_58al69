# Problema 62

def calificacion_final(calif1, calif2, calif3):
    promedio = (calif1 + calif2 + calif3) / 3
    if promedio < 70:
        print("\n¡Atención! Te vas a extra.")
    return promedio

try:
    c1 = float(input("Ingresa la calificación del primer parcial:\n"))
    c2 = float(input("Ingresa la calificación del segundo parcial:\n"))
    c3 = float(input("Ingresa la calificación del tercer parcial:\n"))
    promedio_obtenido = calificacion_final(c1, c2, c3)
    
    print(f"\nTu promedio final del semestre es: {promedio_obtenido:.2f}")

except ValueError:
    print("Error: ingresar únicamente números válidos.")