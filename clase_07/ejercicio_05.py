def imprimir_serie():
    for numero in range (0,100,2):
        if (numero%3!=0):
            print(numero)

import random
numero_aleatorio=random.randint(1,20)*2
print(f'Núm aleatorio::: {numero_aleatorio}')
def ejemplo_for():
    suma=0
    for numero in range(1,99,1):
        if numero==numero_aleatorio:
            break
        suma+=numero
    print(f'Suma ::: {suma}')

def ejemplo_while():
    indice=1  
    suma_while=0
    while indice <numero_aleatorio:
        suma_while+=indice
        indice+=1
    print(f'Suma while::: {suma_while}')