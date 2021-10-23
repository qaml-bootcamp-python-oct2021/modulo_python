#Ejercicio 7.06 - Tony De La Torre

import random

valor_aleatorio = random.randint(1,20) * 2
total = 0
cadena = ""

#imprimiendo suma de todos los numeros del 1 hasta numero aleatorio
def imprimir_suma(random_no, suma, cad):
    print(f"Numero aleatorio: {random_no}")
    for number in range(1,100,1):
        if(number < random_no):
            suma += number
            cad += f"{number}"
        else:
            break
    
        cad += ", "


    print(f"Serie: {cad}")
    print(f"Suma: {suma}")
        

imprimir_suma(valor_aleatorio,total, cadena)