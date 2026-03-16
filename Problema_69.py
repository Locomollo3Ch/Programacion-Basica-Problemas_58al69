# Problema 69

def email(email):
    return "@" in email

direccion = input("Por favor, ingresa tu dirección de email:\n")
if email(direccion):
    print("La dirección es válida.")
else:
    print("La dirección no es válida (le falta el símbolo '@').")