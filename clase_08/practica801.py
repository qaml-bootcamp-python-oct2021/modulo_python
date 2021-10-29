list_num = [1,2,3,4,5]
print(f'El tamaño de la lista es: {len(list_num)}')

import random

numero_random = random.randint(1,10)
print(f'El numero aleatorio es: {numero_random}')

list_num.append(numero_random)
print(list_num)

if list_num.count(numero_random) > 1:
    print('El valor ya existe en la lista')
    index = 0
    while index < len(list_num):
        if numero_random == list_num[index]:
            list_num.pop(index)
            break
        index += 1
    print(list_num)
else:
    list_num.pop(0)
    print(f'El valor no existe en la lista, el tamaño queda en: {len(list_num)}')
    print(list_num)