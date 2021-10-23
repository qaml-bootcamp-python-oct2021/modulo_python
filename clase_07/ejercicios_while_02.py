# script que dado un numero permita calcular la sumatoria de todos los numeros pares que lo preceden desde cero

def calcular_suma_pares(numero):
    suma = 0
    contador = 1
    while contador < numero:
        if es_par(contador):
            suma += contador
        contador +=1
    return suma

def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

print(f'la sumatoria de los numeros es: {calcular_suma_pares(6)}')