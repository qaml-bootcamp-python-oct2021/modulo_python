intentos = 0
my_value = 0

import random

numero = random.randint(1,10)
print(numero)

while numero != my_value:
    my_value = int(input('Ingresa un numero: '))
    intentos += 1
    print(intentos)
print(f'Correcto! Adivinaste el numero en {intentos} intentos.')