import datetime

current_date = datetime.date.today().day
print(current_date)

#today = datetime.date.today().day
#print(today)
today = 15

if today <= 10:
    print('Estamos comenzando el mes')
elif today > 10 and today < 15:
    print('Estamos a casi mitad de mes')
elif today == 15 or today == 16:
    print('Estamos a mitad del mes')
elif today > 16 and today <= 25:
    print('Falta poco para terminar el mes')
else:
    print('Estamos terminando el mes')


