import random

random_number = random.randint(1,20)
suma = 0
print(f'Random number is {random_number}')  


random_number *= 2
print(f'Random number * 2 is {random_number}')  


i = 1

for i in range(1,99):
    if i == random_number:
        break
    suma = suma + i

print(f'Random number is {random_number}')  



print (suma)