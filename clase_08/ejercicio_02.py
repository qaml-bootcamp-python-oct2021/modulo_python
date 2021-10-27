#Ejercicio 02 Listas
import random
def crear_lista():
    lista=[]
    for num in range(9):
        numero_aleatorio=random.randint(1,9)
        lista.append(numero_aleatorio)
    print(lista)
    return lista

def validar_datos_repetidos(lista):
    indice=0
    repetido=False
    while indice< len(lista):
        if lista.count(lista[indice])>1:
            repetido=True
            print(f'Núm repetido::{lista[indice]}')
            break
        indice+=1
    return repetido

def evaluar_lista():
    lista_evaluar= crear_lista()
    if(not validar_datos_repetidos(lista_evaluar)):
        print('No existen números repetidos')

evaluar_lista()