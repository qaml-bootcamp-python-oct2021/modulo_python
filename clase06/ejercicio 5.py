import random

lista = []
cantidad = 0

while cantidad <= 10:
    x = random.randrange(1, 26)
    if x not in lista:
        lista.append(x)
    cantidad += 1
print (lista)