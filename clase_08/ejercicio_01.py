#Ejercicio 01 Listas
import random
lista_numerica= [1,2,3,4,5]
numero_aleatorio=random.randint(1,10)
print(f'Num aleatorio::{numero_aleatorio}')


if lista_numerica.count(numero_aleatorio)>0:
    lista_numerica.pop(lista_numerica.index(numero_aleatorio))
else:
    lista_numerica.pop(0)

lista_numerica.append(numero_aleatorio)
print(lista_numerica)
print(f'Tamaño de la lista::{len(lista_numerica)}')


