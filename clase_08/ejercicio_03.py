import random

tuple_1 = (1,2,3,4,5)
print(len(tuple_1))

random_number = random.randint(1,5)
print(random_number)
index = 0
while index < len(tuple_1):
    print(f'numero {tuple_1[index]}')
    if tuple_1[index] == random_number:
        break
    index += 1
