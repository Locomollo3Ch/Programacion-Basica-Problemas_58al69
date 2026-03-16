# Problema 66

def obtener_reprobados(alumnos):
    nombres_reprobados = []
    for alumno in alumnos:
        if alumno[1] < 70:
            nombres_reprobados.append(alumno[0])
    return nombres_reprobados

lista_grupo = []
while True:
    nombre = input("Ingresa el nombre del alumno (o 'fin' para terminar):\n")
    if nombre.lower() == 'fin':
        break
    try:
        calificacion = float(input(f"Ingresa la calificación de {nombre}:\n"))
        lista_grupo.append((nombre, calificacion))
    except ValueError:
        print("La calificación debe ser un número.")

if len(lista_grupo) > 0:
    reprobados = obtener_reprobados(lista_grupo)
    print(f"\nAlumnos evaluados: {len(lista_grupo)}")
    print(f"Lista de alumnos reprobados: {reprobados}")