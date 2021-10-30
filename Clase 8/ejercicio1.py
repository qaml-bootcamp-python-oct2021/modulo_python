import random

def list_size(lista):
    print(f'el tamaño de la lista es: {len(list)}')
    
    
    
list = [1,2,3,4,5]
list_size(list)
num_aleatorio = random.randint(1, 10)
list.append(num_aleatorio)
print(list)

if list.count(num_aleatorio) > 1:
    
    index = 0
    while index < len(list):
        if num_aleatorio == list[index]:
            list.pop(index)
            break
        index +=1
    else:
        print('El elemento NO existe en la lista')
        list.pop(0)

list_size(list)
print(list)