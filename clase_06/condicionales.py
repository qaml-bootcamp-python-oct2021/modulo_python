def get_temporada (numero_mes):
    if numero_mes >=3 and numero_mes<=5: 
     print('Temporada es primavera')

    elif numero_mes >=6 and numero_mes <=8:
     print('Temporada es verano')

    elif numero_mes >=8 and numero_mes<= 11:
     print('Temporada es otoño')

    else:
     print('Temporada es invierno')

def valida_mes(num_mes):
    if num_mes>=1 and num_mes<=12:
        return True
    else:
        print ("""El mes ingresado no existe
        Por favor verifique e intente de nuevo
        'La Gerencia' """)

num_mes= 20
if valida_mes(num_mes):
      get_temporada(num_mes)