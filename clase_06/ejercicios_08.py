# Dado un número aleatorio del 1 al 20 multiplicado por 2, imprime el valor del mismo y dado una iteración del 1 al 99 cuando consiga el número aleatorio, que deje de iterar y muestre la suma de todos los numeros iterados

import random
numero = random.randint(1,20)
numero *= 2
print(numero)

total = 0
indice = 1

while indice < numero:
    total += indice
    indice += 1
print(f'EL total es: {total}')