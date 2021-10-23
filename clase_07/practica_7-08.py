sumatoria = 0
indice = 1

import random

numero = random.randint(1,20)
print (numero)

multiplicado = numero * 2
print(multiplicado)

while indice < numero:
    sumatoria += indice
    indice += 1
print(f'El total es {sumatoria}')

