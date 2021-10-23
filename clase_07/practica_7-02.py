#REVISAR

suma = 0
contador = 1
numero = 3

while contador < numero:
    if numero % 2 == 0:
        suma += contador
    contador += 1

print(f'La sumatoria de los numeros es: {suma}')