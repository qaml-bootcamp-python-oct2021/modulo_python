#Define una lista con los valores [1,2,3,4,5] e imprime el tamaño de la misma. Luego dado un número aleatorio entre el 1 y 10 agregar el nuevo valor en la lista.
#Si el valor ya existe eliminalo de la lista, de lo contrario elimina el primer registro de la lista y vuelve a imprimir el tamaño de la lista.

import random

lista_numeros = [1,2,3,4,5]
numero_aleatorio = random.randint(1,10)
print(numero_aleatorio)
print(len(lista_numeros))

if lista_numeros.count(numero_aleatorio)>0:
    lista_numeros.pop(numero_aleatorio-1)
else: 
    lista_numeros.pop(0)

lista_numeros.append(numero_aleatorio)
print(lista_numeros)
print(len(lista_numeros))