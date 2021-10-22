import datetime
current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year
current_date = datetime.date.today().year
def get_age(birthday_year):
     return current_year -birthday_year

def is_birthday( day, month):
    return  month<=current_month and day<=current_day

def get_generation( year):
    if year>=1990 and year <=1939:
        print("Generación silenciosa")
    elif year>=1940 and year <=1959:
        print("Generación Baby boomers")
    elif year>=1960 and year <=1979:
        print("Generación X")
    elif year>=1980 and year <=1989:
        print("Generación Y")
    elif year>=1900:
        print("Generación Z")
    
def calc_age(day, month, year):
    age= get_age(year)
    if  is_birthday(day, month):
       print('Has cumplido años') 
    else: 
        print('No Has cumplido años') 
        age=age-1
    
    print(f'Su edad es {age}')

param_year= 1939
param_month= 12
param_day= 1
calc_age(param_day, param_month, param_year)
get_generation(param_year)
