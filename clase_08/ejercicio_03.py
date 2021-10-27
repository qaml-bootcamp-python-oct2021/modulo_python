#Ejercicio 03 Tuplas
import random
tupla=(1,2,3,4,5)
indice=0
numero_aleatorio=random.randint(1,5)

print(f'Tamaño::{len(tupla)}')
print(f'Num aleatorio::{numero_aleatorio}')
while indice< len(tupla):
    print(tupla [indice])
    if numero_aleatorio == tupla [indice]:
        break
    indice+=1