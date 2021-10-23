import random
aleatorio = random.randint(1,20)
aleatorio *=2
print(f'Numero aleatorio multiplicado por 2 {aleatorio}')

total = 0
indice =1
while indice < aleatorio:
    total += indice
    indice += 1
print(total)