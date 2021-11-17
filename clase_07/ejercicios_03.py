#Define una tupla con los valores [1,2,3,4,5] e imprime el tamaño de la mismo.
#Luego dado un número aleatorio entre el 1 y 5 recorrer la tupla e imprimir todos los numeros hasta que coincida el número generado.
import random

def size_tupla(mi_tupla):
    print(f'Tamaño de la tupla es: {len(mi_tupla)}')

mi_tupla = (1,2,3,4,5)
size_tupla(mi_tupla)
numero = random.randint(1,5)

index = 0
while index < len(mi_tupla):
    print(mi_tupla[index])
    if numero == mi_tupla[index]:
        break
    index += 1
