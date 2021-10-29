import random

my_list = []

def llenar_lista(lista):
    for indice in range(9):
        lista.append(random.randint(1,9))
        ##return lista


def encontrar_repetido_en_lista(lista):
    indice = 0

    while indice < len(lista):

        if lista.count(lista[indice]) > 1:
            return lista[indice]

        indice += 1
    
    return 0
            
 
llenar_lista(my_list)

print(my_list)

valor = encontrar_repetido_en_lista(my_list)

if (valor == 0):
    print("No hay numeros repetidos en la lista...")
else:    
    print(f"El primer numero repetido de la lista es {valor}")

