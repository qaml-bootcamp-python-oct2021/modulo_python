#Escribir un script que dado el día, mes y año de nacimiento de una persona determine lo siguiente:
#Cuantos años tiene
#Si en lo que va del año ya cumplio o no.
#Determinar a que generación pertenece:
#La generación silenciosa: Nacidos entre 1920 y 1939.
#Los baby boomers: Nacidos entre 1940 y 1959.
#Generación X: Nacidos entre 1960 y 1979.
#Generación Y o Millenials: Nacidos entre 1980 y 1989.
#Generación Z: Nacidos entre 1990 en adelante.

import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

day = 21                                                                            
month = 1
year = 1992

def already_age(month,day):
    return month < current_month and day > current_day

def calculate_age(day,month,year):
    years = current_year - year
    if already_age(month,day):
        age = years + 1
        message = 'Ya fue su cumpleaños este año'
    else:
        message = 'Aun no es su cumpleaños este año'
    print(years)
    print(message)

def know_generation(year):
    if year >= 1920 and year <= 1939:
        print('Pertenece a la Generación Silenciosa')
    elif year >= 1940 and year <= 1959:
        print('Pertenece a la Generación Baby Boomers')   
    elif year >= 1960 and year <= 1979:
        print('Pertenece a la Generación X')  
    elif year >= 1980 and year <= 1989:
        print('Pertenece a la Generación Y o Millenials') 
    else:
        print('Pertenece a la Generación Z')
calculate_age(day,month,year)
know_generation(year)