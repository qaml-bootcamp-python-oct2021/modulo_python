#Ejercicio 6.03 - Tony De La Torre

import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

print(f"El día de hoy es {current_day} - {current_month} - {current_year}")

birth_day=22
birth_month=10
birth_year=1984

print(f"Tu cumpleaños es {birth_day} - {birth_month} - {birth_year}")


#validando generacion
def validar_generacion(year):
    if year < 1920:
        print("Año de nacimiento anterior a 1920, fuera de la clasificación.")
    elif year >= 1920 and year <=1939:
        print("Eres parte de la generación silenciosa.")
    elif year >= 1940 and year <=1959:
        print("Eres un Baby Boomer.")
    elif year >= 1960 and year <=1979:
        print("Eres parte de la generación X.")
    elif year >= 1980 and year <=1989:
        print("Eres Millenial.")
    else:
        print("Eres parte de la generación Z.")

#validando cumpleaños
def validar_cumple(b_day,b_month,c_day,c_month):
   
    if (b_day == c_day) and (b_month == c_month):
        print("¡Feliz Cumpleaños!")
        return True
    elif (c_month < b_month) or ((c_day < b_day) and (c_month == b_month)):
            print("Aun no es tu cumpleaños")
            return False
    else:
            print("Ya pasó tu cumpleaños")
            return True

#validar edad
def validar_edad(b_year,c_year,flag):
    edad= c_year - b_year
    if flag :
        print(f"Tu edad es {edad}")
    else:
        print(f"Tu edad es {edad-1}")

validar_generacion(birth_year)
cumple = validar_cumple(birth_day,birth_month,current_day,current_month)
validar_edad(birth_year,current_year,cumple)
