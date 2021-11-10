#Escribe un script que dado un numero permita calcular la sumatoria de todos los numeros pares que lo preceden desde cero

def suma_pares(numero):
    suma = 0
    contador = 1
    while contador < numero:
        if numero_par(contador):
            suma += contador
        contador += 1
    return suma

def numero_par(numero):
    if numero%2 ==0:
        return True
    return False

print(f'La suma es: {suma_pares(5)}')