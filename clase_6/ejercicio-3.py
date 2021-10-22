import datetime

current_day = datetime.date.today().day
current_month = datetime.date.today().month
current_year = datetime.date.today().year

def get_age(birth_year):
    return current_year - birth_year

def if_it_was_already_birthday(birth_day, birth_month):
    month_cal =  current_month - birth_month
    day_cal = current_day - birth_day
    if month_cal < 0:  return False
    elif month_cal == 0: 
      if day_cal < 0: return False
      else: return True
    else: return True

def to_determine_generation(birth_year):
    if birth_year >= 1920 and  birth_year <= 1939:
       msg = 'Generacion Silenciosa'
    elif birth_year >= 1940 and birth_year <= 1959:
       msg = 'Generacion Baby Boomers'
    elif birth_year >= 1960 and birth_year <= 1979:
       msg = 'Generacion X'
    elif birth_year >=1980 and birth_year <= 1989:
       msg = 'Generacion Y o millennials'
    elif birth_year >= 1990:
       msg = 'Generacion Z'
    return msg

def get_information_person(birth_day_f, birth_month_f, birth_year_f):
    birthday = if_it_was_already_birthday(birth_day_f, birth_month_f)
    age = get_age(birth_year_f)
    msg_age = 'Su edad es:'

    if birthday: 
       print(f'{msg_age} {age}')
       print('Ya cumplio anios')
    else: 
       print(f'{msg_age} {age-1}')
       print('No cumplio anios')

    generation = to_determine_generation(birth_year_f)
    print(f'Pertenece a la: {generation}')
    
  
get_information_person(21,10,1994)
print('------------------------')
get_information_person(27,5,1938)
print('------------------------')
get_information_person(29,11,1940)
print('------------------------')
get_information_person(22,11,1961)
print('------------------------')
get_information_person(21,11,1989)
print('------------------------')
get_information_person(22,10,1990)

