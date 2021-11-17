num_mes = 5

def detectar_temporada(numero_mes):
    if numero_mes >= 3 and numero_mes <= 5:
        print('El mes pertene a la Primavera')
    elif numero_mes >=6 and numero_mes <=8:
        print('El mes pertene a la Verano')
    elif numero_mes >=9 and numero_mes <=11:
        print('El mes pertene a la Otonio')
    else:
        print('El mes pertene a la Invierno')

def validar_mes(numero_mes):
    if numero_mes >=1 and numero_mes <= 12:
        return True
    else:
        return False

def print_mensaje_error():
    print("""El mes ingresado no existe
        Por favor verifique e intente de nuevo
        'La Gerencia'""")

if validar_mes(num_mes):
    detectar_temporada(num_mes)
else:
    print_mensaje_error()