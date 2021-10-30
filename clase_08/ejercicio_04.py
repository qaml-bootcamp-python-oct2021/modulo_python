#Ejercicio 04 Tuplas 
import random
puntos=(25,18,15,12,10,8,6,4,2,1)

def obtener_pares():
    pares=0
    for punto in puntos:
        if punto %2 ==0:
            pares+=1
    return pares

def obtener_puntos(cantidad_posiciones):
    indice=0
    suma= 0
    while indice< cantidad_posiciones:
        suma+= puntos [indice]
        indice+=1
    return suma

print(f'Cantidad de números pares: {obtener_pares()}')
print(f'Suma de los 3 primeros: {obtener_puntos(3)}')
print(f'Suma total:  {obtener_puntos(len(puntos))}')
