import random
num = random.randint(1,10)
intentos= 0
mi_numero = 0

while num != mi_numero:
    mi_numero = int(input('Engrese numero del 1 al 10 \n'))
    intentos += 1
    print(f'Intentos {intentos}')
print(f'El numero era: {num}')



