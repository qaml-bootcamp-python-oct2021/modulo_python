import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

def ya_cumplio(dia_nacimiento,mes_nacimiento):

    if mes_nacimiento <= current_month  and dia_nacimiento <= current_day:
        print('')






def generacion(year_nacimiento):
    if year_nacimiento >= 1920 and  year_nacimiento <=1939:
        print('Pertenece a la generacion silenciosa')
    elif year_nacimiento >= 1940 and year_nacimiento <=1959:
        print('Pertenice a la generacion de los baby bommer')
    elif year_nacimiento >= 1960 and year_nacimiento <=1979:
        print('Pertenece a la generacion X')
    elif year_nacimiento >= 1980 and year_nacimiento <= 1989:
        print('Pertenece a la generacion Y o millennials')
    elif year_nacimiento >= 1990:
        print('Pertenece a la generacion Z')
    else:
        print('Año de nacimiento sin nombre de generacion')