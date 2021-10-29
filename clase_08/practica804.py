formula1_pts = (25,18,15,12,10,8,6,4,2,1)

#1. CUALES NUMEROS SON PARES
#2. CUANTOS PUNTOS SE LE DAN A LOS 3 PRIMEROS
#3. CUAL SERIA LA SUMATORIA DE TODOS LOS NUMEROS

index = 0
sumatoria = 0
sumaTotal = 0

for pares in formula1_pts:

    sumaTotal += formula1_pts[index]

    if pares % 2 == 0:
        print(f'El indice {pares} es par')
    
    if index < 3:
        sumatoria += formula1_pts[index]
    index += 1

print(f'La sumatoria de los 3 primeros lugares es: {sumatoria}')
print(f'La sumatoria total de puntos es: {sumaTotal}')