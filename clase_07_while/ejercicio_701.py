import random

valor_aleatorio = 4
total = 0
cadena = ""

#imprimiendo suma de todos los numeros del 1 hasta numero aleatorio
def imprimir_suma(random_no, suma, cad):

    incremento = 1

    while incremento < random_no:
        suma += incremento
        cad += f"{incremento}"
        incremento += 1
        
        if(incremento < random_no):
            cad += ", "


    print(f"Serie: {cad}")
    print(f"Suma: {suma}")
        

imprimir_suma(valor_aleatorio,total, cadena)