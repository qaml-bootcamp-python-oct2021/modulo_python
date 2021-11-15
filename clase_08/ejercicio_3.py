
import random

tupla = (1,2,3,4,5)

print(f'El tamaño de la tupla es: {len(tupla)} ')  

num_ran = random.randint(1,5)

print(f'El numero random es: {num_ran}')  

indice = 0

while indice < len(tupla):
    if tupla[indice] != num_ran:
        print(f'Numero : {tupla[indice]}')
    else:
        break
    indice += 1