#poker planning
my_list = [0,0.5,1,2,3,5,8,13,20,40,100]

cad_pares = ''
num_divisibles = ''
total = 0


for index in range(0,len(my_list),1):
    total += my_list[index]

    if ( my_list[index] % 2 == 0):
        cad_pares += f'{my_list[index]}, '


    if( index > 0 and my_list[index-1] != 0):
        if my_list[index]%my_list[index-1] == 0 and my_list[index]/my_list[index-1] > 0:
            num_divisibles += f'{my_list[index]}, '

print(f"Pocket planning: {my_list}")
print(f"Suma de todos los números: {total}")
print(f"Numeros pares dentro de la lista: {cad_pares}")
print(f"Numeros divisibles entre su antecesor cuyo resultado es un entero: {num_divisibles}")
