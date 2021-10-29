tuplaNum = (1,2,3,4,5)
longitudTupla = len(tuplaNum)
print(f'La longitud de la tupla es de: {longitudTupla}')

from operator import index
import random
numAleatorio = random.randint(1,5)
print(f'El numero aleatorio es: {numAleatorio}')
index = 0

while numAleatorio != tuplaNum[index]:
    print(tuplaNum[index])
    index += 1