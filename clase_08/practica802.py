import random
list_num = list()

for num in range(1,10,1):
    num_ran = random.randint(1,9)
    list_num.append(num_ran)
print(list_num)

longitud_lista = len(list_num)
index = 0

while index < longitud_lista:
    if list_num.count(list_num[index]) > 1:
        print(f'Se encontro como numero repetido: {list_num[index]}')
        break
    index += 1

if index == longitud_lista:
    print('No existen numero repetidos')