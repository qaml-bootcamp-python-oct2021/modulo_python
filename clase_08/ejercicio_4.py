puntos = (25,18,15,12,10,8,6,4,2,1)

pares = 0
total = 0
for punto in puntos:
    if punto % 2 == 0:
        pares+=1
    total += punto

indice = 0
suma_primeros_tres = 0
while indice < 3:
    suma_primeros_tres += puntos[indice]
    indice +=1

print(f'Hay {pares} numeros pares')
print(f'Los tres primeros lugares suman {suma_primeros_tres} puntos')
print(f'El total de puntos es de: {total}')