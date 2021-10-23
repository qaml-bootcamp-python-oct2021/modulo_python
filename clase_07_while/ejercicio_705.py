#Ejercicio 7.05 - Tony De La Torre

import random

valor_aleatorio = random.randint(1,10)


#imprimiendo tabla de multiplicar
def imprimir_tabla(random_no):
    
    for number in range(1,10,1):
        print(f"{random_no} x {number} = {random_no * number}")

imprimir_tabla(valor_aleatorio)

