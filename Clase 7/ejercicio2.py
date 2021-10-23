def pares(numero):
    suma = 0
    contador = 1
    while contador < numero:
        if par(contador):
            suma += contador
        contador += 1 
    return suma

def par(numero):
    if numero%2 ==0:
        return True
    else:
        return False

print(f'La sumatoria de los numeros es: {pares(5)}')