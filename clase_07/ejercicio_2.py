def calcular_suma(num):
    suma = 0
    contador = 1
    while contador < num:
        if es_par(contador):
            suma += contador
        contador += 1
    return suma

def es_par(num):
    if num % 2 == 0:
        return True
    return False

print(f'La suma de los pares es: {calcular_suma(5)}')

