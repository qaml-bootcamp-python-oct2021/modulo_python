import random

valor_aleatorio  = random.randint(1,10)
my_tuple = (1,2,3,4,5)


indice = 0

def encontrar_elemento(tupla, valor):
    indice = 0

    while indice < len(tupla):

        if tupla[indice] == valor:
            return indice

        indice += 1
    
    return -1

def imprimir_tupla_subset(tupla,valor):

    for number in range(valor+1):
        print(tupla[number])


print(my_tuple)

valor_i = encontrar_elemento(my_tuple,valor_aleatorio)

if valor_i == -1:
    print(f"Valor aleatorio {valor_aleatorio} no presente en la tupla.")
else:
    print(f"Valor aleatorio: {valor_aleatorio}.")
    imprimir_tupla_subset(my_tuple,valor_i)

