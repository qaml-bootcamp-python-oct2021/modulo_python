#Escribe un script que dado un número permita calcular la sumatoria de todo los números que lo preceden desde cero.

numero = 6
indice = 0
suma = 0

while indice < numero:
    suma += indice
    indice += 1
print(f'La suma de los numeros es: {suma}')