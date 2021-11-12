#Condicionales: Desarrollar un script que basado a un número de mes pueda detectar en qué temporada se encuentra el mes, siendo que las temporadas se dividen en: 
#Primavera = Marzo, Abril, Mayo
#Verano = Junio, Julio, Agosto
#Otoño = Septiembre, Octubre, Noviembre
#Invierno = Diciembre, Enero, Febrero
#Es importante validar que el número del mes sea correcto y en el caso de que el número no sea correcto, deberán informar el siguiente mensaje:
#El mes ingresado no existe
#Por favor verifique e intente de nuevo
#'La Gerencia'

mes = 11

def temporada_actual(mes):
    if mes >=3 and mes <=5:
        print('Temporada de Primavera')
    elif mes >=6 and mes <=8:
        print('Temporada de Verano')
    elif mes >=9 and mes <=11:
        print('Temporada de Otoño')
    else:
        print('Temporada de Invierno')
    
def anualidad(mes):
    if mes >=1 and mes <=12:
        return True
    else:
        return False

def mensaje_error():
    print("""El mes ingresado no existe
Por favor verifique e intente de nuevo
'La Gerencia'""")

if anualidad(mes):
    temporada_actual(mes)
else:
    mensaje_error()