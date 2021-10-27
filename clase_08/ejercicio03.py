from operator import index
import random

my_tuple = (1,2,3,4,5)

print(f'Tuple is {len(my_tuple)} items length')  

random_number = random.randint(1,5)

print(f'Random number is {random_number}')  

index = 0

while index < len(my_tuple):
    if my_tuple[index] != random_number:
        print(my_tuple[index])
    else:
        break
    index += 1
