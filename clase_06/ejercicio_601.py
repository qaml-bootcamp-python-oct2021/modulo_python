#Ejercicio 6.01 - Tony De La Torre

month = 2

def season(mes):
    if (mes <1) or (mes>12):
        print("""El mes ingresado no existe.
Por favor, verifique e intente de nuevo.
'La Gerencia'""")
    elif mes >=3 and mes <=5:
        print("Estamos en Primavera :)")
    elif mes >=6 and mes <=8:
        print("Estamos en Verano :)")
    elif mes >=9 and mes <=11:
        print("Estamos en Otoño :)")
    else:
        print("Estamos en Invierno :)")

season(month)
