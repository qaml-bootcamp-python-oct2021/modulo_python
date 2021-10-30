puntos = (25,18,15,12,10,8,6,4,2,1)

pares = 0
total = 0
for punto in puntos:
    if punto % 2 == 0:
        pares+=1
    total += punto

index = 0
top_3 = 0
while index < 3:
    top_3 += puntos[index]
    index +=1

print(f'Existen {pares} numeros pares')
print(f'Los tres primeros suman {top_3} puntos')
print(f'El total de puntos es de: {total}')