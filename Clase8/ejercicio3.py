import random

numero = random.randint(1, 5)
my_tuppla = (1,2,3,4,5)

print(len(my_tuppla))
index=0

print(numero)

while index < len(my_tuppla):
    print(my_tuppla[index])
    if numero == my_tuppla[index]:
        break
    index +=1