# ''' Ejercicio 01 '''
import random

def print_list_size(lista):
    print(f'El tamanio de la lista es {len(lista)}')

# lista = [1,2,3,4,5]
# print_list_size(lista)
# numero = random.randint(1,10)
# lista.append(numero)
# print(lista)

# if lista.count(numero) > 1:
#     index = 0
#     while index < len(lista):
#         if numero == lista[index]:
#             lista.pop(index)
#             break
#         index += 1
# else:
#     lista.pop(0)

# print_list_size(lista)
# print(lista)

# ''' Ejercicio 1 Tuplas'''

# mi_tupla = (1,2,3,4,5)
# print_list_size(mi_tupla)

# numero = random.randint(1,5)
# print(f'El numero aleatoria es: {numero}')
# index = 0
# while index < len(mi_tupla):
#     print(f'Numero: {mi_tupla[index]}')
#     if numero == mi_tupla[index]:
#         break
#     index +=1

''' Ejercicio 2 Tuplas'''
puntos = (25,18,15,12,10,8,6,4,2,1)

pares = 0
total = 0
for punto in puntos:
    if punto % 2 == 0:
        pares+=1
    total += punto

index = 0
top_3 = 0
while index < 3:
    top_3 += puntos[index]
    index +=1

print(f'Existen {pares} numeros pares')
print(f'Los tres primeros suman {top_3} puntos')
print(f'El total de puntos es de: {total}')
