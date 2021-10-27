import random


numero_aleatorio=random.randint(1,10)
def imprimir_tabla():
    for number in range (1,10,1):
        print( f'{numero_aleatorio} x {number} = {multiplicar_numero(numero_aleatorio,number)}')

def multiplicar_numero(numero_a, numero_b):
    return numero_a * numero_b

def imprimir_escalera():
    print(numero_aleatorio)
    for number in range (numero_aleatorio):
        print('*' * number)

imprimir_tabla()
imprimir_escalera()