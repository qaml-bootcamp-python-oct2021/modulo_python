#Escribe un script que dado un número aleatorio permita generar una tabla de multiplicar donde podamos visualizar los resultados

import random
numero_aleatorio = random.randint(1,10)

def tabla_multiplicar(numero_random):
    for numero in range(1,10,1):
        print(f'{numero_random} x {numero} = {numero_random * numero}')

tabla_multiplicar(numero_aleatorio)