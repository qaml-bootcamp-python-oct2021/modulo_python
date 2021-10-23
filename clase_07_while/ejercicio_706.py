#Ejercicio 7.06 - Tony De La Torre

import random

valor_aleatorio = random.randint(1,10)


#imprimiendo escalera
def imprimir_escalera(random_no):
    print(f"Número de filas (aleatorio): {random_no}")
    for number in range(1,random_no+1,1):
        print(number * '*')

imprimir_escalera(valor_aleatorio)