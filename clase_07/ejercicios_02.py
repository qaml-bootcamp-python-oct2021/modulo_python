#Define una lista de 9 registros con valores aleatorios del 1 al 9. Recorre la lista en búsqueda de números repetidos. 
#Si existe un número repetido cancela el proceso y manda un mensaje indicando cuál número está repetido.
#De lo contrario, muestra un mensaje que indique que no existen números repetidos

import random
def nueva_lista():
    lista = []
    for numero in range(9):
        numero_aleatorio = random.randint(1,9)
        lista.append(numero_aleatorio)
    print(lista)
    return lista

def datos_repetidos(lista):
    indice = 0
    numero_repetido = False
    while indice < len(lista):
        if lista.count(lista[indice])>1:
            numero_repetido = True
            print(f'El número repetido es:{lista[indice]}')
            break
        indice+=1
    return numero_repetido

def buscar_repetidos():
    buscar_numero = nueva_lista()
    if(not datos_repetidos(buscar_numero)):
        print('No existen números repetidos')

buscar_repetidos()