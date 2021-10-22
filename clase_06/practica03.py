import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

dia = 20
mes = 8
anio = 2025

def edadPersona(anio,current_year):
    if anio >= 1920 and anio <= current_year:
        edad = current_year - anio
        print(f'La persona tiene {edad} año(s)')
        if anio == current_year:
            generacion(anio,current_year)
        else:
            cumplioAños(mes,current_month)
            generacion(anio,current_year)
    else:
        print(f'Ingrese una fecha de nacimiento mayor a 1920 y menor o igual a {current_year}')


def cumplioAños(mes,current_month):
    if  current_month >= mes:
        print('La persona ya cumplio años este año')
    else:
        print('La persona aun no cumple años este año')

def generacion(anio,current_year):
    if anio >= 1920 and anio <= 1939:
        print('Pertenece a la \"Generacion silenciosa\"')
    elif anio >= 1940 and anio <= 1959:
        print('Pertenece a la generacion de los \"Baby boomer\"')
    elif anio >= 1960 and anio <= 1979:
        print('Pertenece a la \"Generacion X\"')
    elif anio >= 1980 and anio <= 1989:
        print('Pertenece a la \"Generacion Y (Millenial)\"')
    elif anio >= 1990 and anio <= current_year:
        print('Pertenece a la \"Generacion Z')


edadPersona(anio,current_year)