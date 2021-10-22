import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year


day = 29
month = 7
year = 1990

def get_age():
    edad = 2021 - year
    if birthday_yet == True:
        return edad
    else:
        return edad - 1
    
        

def birthday_yet():
    return current_month >= month and current_day >= day


def get_generation():
    if year >= 1920 and year <= 1939:
        return "Generación silenciosa"
    elif year >= 1940 and year <= 1959:
        return "Generación Baby Boomers"
    elif year >= 1960 and year <= 1979:
        return "Generación X"
    elif year >= 1980 and year <= 1989:
        return "Generación Y"
    elif year >= 1990:
        return "Generación Z"

def get_data():
    print(f'This person is {get_age()} years old')  
    if birthday_yet:
        print("This person already has a birthday party this year")     
    else:
        print("This person hasn't had a birthday party this year")    
    print(f'This person is from {get_generation()}')  

get_data()

print(birthday_yet())