#puntos
tuple_2 = (25,18,15,12,10,8,6,4,2,1)

count = 0
sum_tuple_2 = 0
for element in tuple_2:
    if element % 2 == 0:
        count += 1
    sum_tuple_2 += element
print(f'hay {count} numeros pares')

index = 0
top_3 = 0
while index < 3:
    top_3 += tuple_2[index]
    index += 1
print(f'los 3 primeros suman {top_3} puntos')

print(f'el total de puntos es {sum_tuple_2}')