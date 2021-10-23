import datetime
current_day=datetime.date.today().day
day=1
dias_transcurridos=0
print(current_day)
while day< current_day:
    print(day)
    dias_transcurridos+=1
    day+=1
print(f'Dias trans{dias_transcurridos}')