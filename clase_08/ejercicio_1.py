
import random

numero_random = random.randint(1,10)
lista = [1,2,3,4,5]

print(f'El tamaño de la lista es: {len(lista)}')
print(f'El numero aleatorio es: {numero_random}')

lista.append(numero_random)
print(lista)

if lista.count(numero_random) > 1:
    print('El valor ya existe')
    index = 0
    result = False
    while index < len(lista) and not result:
        if numero_random == lista[index]:
            lista.pop(index)
            result = True
        index += 1
    print(f'La lista queda asi: {lista}')
else:
    print('El elemento NO existe en la lista')
    lista.pop(0)
    print(f'El tamaño queda en: {len(lista)}')
    print(f'La nueva lista es: {lista}')