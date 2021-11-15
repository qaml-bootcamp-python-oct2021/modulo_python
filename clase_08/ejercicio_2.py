import random
lista = []

for num in range(9):
    num_ran = random.randint(1,9)
    lista.append(num_ran)

print(lista)

index = 0
while index < len(lista):
    if lista.count(lista[index]) > 1:
        print(f'Se encontro como primer numero repetido el: {lista[index]}')
        break
    index += 1
if index == len(lista):
    print('No existen numeros repetidos')