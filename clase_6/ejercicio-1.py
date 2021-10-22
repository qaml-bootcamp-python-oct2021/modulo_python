# Operadores Logicos y Condicionales
numero = 5
def obtener_temporada(numero):
    if numero == 12 or numero == 1 or numero ==2:
       print("Invierno")
    elif numero > 2 and  numero <= 5:
       print("Verano")
    elif numero > 5 and  numero <= 8:
       print("Otonio")
    elif numero > 8 and  numero <= 11:
       print("Primavera")
    else:
        print("""El mes ingresado no existe.
        Por favor verifique e intente de nuevo
        'La Gerencia.'""")

obtener_temporada(numero)

