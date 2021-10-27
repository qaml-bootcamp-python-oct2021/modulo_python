import random

list_2 = []

while len(list_2) < 9:
    list_2.append(random.randint(1,9))

#caso de prueba cuando no hay repetidos
#list_2 = [1,2,3,4,5,6,7,8,9]

print(list_2)

index = 0
while index < len(list_2):
    if list_2.count(list_2[index]) > 1:
        print (f'se repite el numero {list_2[index]}')
        break
    else:
        index += 1

    if index == len(list_2):
        print('no existen numeros repetidos')