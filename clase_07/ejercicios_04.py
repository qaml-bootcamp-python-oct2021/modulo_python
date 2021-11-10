#Dada una tupla de distribución de puntos para la Fórmula 1 (25,18,15,12,10,8,6,4,2,1) indique:
#Cuantos de estos números son pares
#Cuantos numeros se le entregan a los 3 primeros
#Cual seria la sumatoria de todos los puntos

import random
puntos=(25,18,15,12,10,8,6,4,2,1)

def numeros_pares():
    pares=0
    for punto in puntos:
        if punto %2 ==0:
            pares+=1
    return pares

def sumar_puntos(primeros_tres):
    indice=0
    suma= 0
    while indice < primeros_tres:
        suma+= puntos [indice]
        indice+=1
    return suma

print(f'Número de pares: {numeros_pares()}')
print(f'Suma de los 3 primeros números: {sumar_puntos(3)}')
print(f'Total de Puntos:  {sumar_puntos(len(puntos))}')