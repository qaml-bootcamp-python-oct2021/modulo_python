import random

num = random.randint(0, 10)
dato = int(input('Ingrese numero:'))
contador=1

while dato != num:
    print('intentos:' , contador)
    dato = int(input('Error vuelva a ingresar numero:'))
    contador += 1

print('intentos finales', contador)