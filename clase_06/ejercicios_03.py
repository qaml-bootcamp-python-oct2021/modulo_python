import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

dia = 3
mes = 8
anio = 1987

def ya_cumplio_anios(mes, dia):
    return mes < current_month and dia < current_day

def calcular_edad(dia, mes, anio):
    edad = current_year - anio -1
    if ya_cumplio_anios(mes, dia):
        edad = edad + 1
        message = 'ya cumplio años este año'
    else:
        message = 'no cumplio años este año todavia'
    print(edad)
    print(message)

def saber_generacion(anio):
    if anio >=1920 and anio <= 1939:
        print('Generacion Silenciosa')
    elif anio >=1940 and anio <= 1959:
        print('Generacion Baby boomers')
    elif anio >=1960 and anio <= 1979:
        print('Generacion X')
    elif anio >=1980 and anio <= 1989:
        print('Generacion Y o millennials')
    else:
        print('Generacion Z')

calcular_edad(dia, mes, anio)
saber_generacion(anio)