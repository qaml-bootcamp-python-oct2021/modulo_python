import random

#imprimir el tamaño de una lista

list_1 = [1,2,3,4,5]
list_length = len(list_1)
print(list_length)

#second part
random_number = random.randint(1,10)
list_1.append(random_number)
print(list_1)

if list_1.count(random_number) > 1:
    print('el elemento ya existe')
    index = 0
    while index < len(list_1):
        if random_number == list_1[index]:
            list_1.pop(index)
            break
        index += 1
else:
    print('el elemento NO existe')
    list_1.pop(0)

print(list_1)
print(len(list_1))