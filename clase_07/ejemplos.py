# ''' Suma de numaeors pares '''
# def calcula_suma_pares(numero):
#     suma = 0
#     contador = 1
#     while contador < numero:
#         if es_par(contador):
#             suma += contador
#         contador +=1
#     return suma

# def es_par(numero):
#     if numero%2 ==0:
#         return True
#     return False

# print(f'La sumatoria de los numero es: {calcula_suma_pares(5)}')


# ''' Ejercicio de impresion entre numeros'''
# num_min = 5
# num_max = 8
# numeros = ''

# num_min += 1

# while num_min < num_max:
#     numeros += f'{num_min}, '
#     num_min += 1
    
# print(numeros)


''' Ejemplo Input y Random'''
# import random
# numero = random.randint(1,10)
# print(numero)

# dato = input('ingrese numero del 1 al 10\n')
# print('el numero inrgesado por el usuario es: {}'.format(dato)

# ''' Ejercicicio: Adivinanza de numero'''
# import random
# num = random.randint(1,10)
# intentos= 0
# mi_numero = 0

# while num != mi_numero:
#     mi_numero = int(input('Engrese numero del 1 al 10 \n'))
#     intentos += 1
#     print(f'Intentos {intentos}')
# print(f'El numero era: {num}')


# ''' Ejemplo For '''
# for number in range(5):
#     print(number)

# print('------------------------')

# for number in range(1,10,2):
#     print(number)


# ''' Continue'''
# result = 0
# for numero in range(1,10):
#     if es_par(numero) :
#         print(f'Este numero es par: {numero} y los numeros pares no se procesan')
#         break
#     result += numero
# print(result)


''' Ejercicio Iteracion 2 '''
import random

numero = random.randint(1,20)
numero *= 2
numero = 4
print(numero)

total = 0
indice = 1

while indice < numero:
    total += indice
    indice+=1
print(f'el total es: {total}')