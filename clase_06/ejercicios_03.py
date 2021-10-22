import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

dia = 21
mes = 10
anio = 1919

def ya_cumplio_anios(mes, dia):
    return mes <= current_month and dia <= current_day

def calcular_edad(dia, mes, anio):
    edad = current_year - anio
    if ya_cumplio_anios(mes, dia):
        message = 'ya cumplio años este año'
    else:
        edad -= 1
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
    elif anio >=1990:
        print('Generacion Z')
    else:
        print('Año fuera de rango')

calcular_edad(dia, mes, anio)
saber_generacion(anio)