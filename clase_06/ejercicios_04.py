#Escribe un script que dado un número aleatoriopermita encontrar su valor por medio de interacción con usuario, mostrando cuantos intentos le llevo encontrarlo al mismo

import random
numero = random.randint(1,10)
intentos = 0
valor = 0
print(numero)
while numero != valor:
    valor = int(input('Ingresa un valor entre 0 y 10:\n'))
    intentos += 1
    print(f'Número de intentos: {intentos}')
print(f'El valor ingresado es: {numero}')

