import random

valor_aleatorio = 5
total = 0
cadena = ""

#imprimiendo suma de todos los numeros pares desde cero hasta antes de numero aleatorio
def imprimir_suma(random_no, suma, cad):

    incremento = 1

    while incremento < random_no:
        
        if incremento % 2 == 0:        
            suma += incremento
            cad += f"{incremento}"
        
            if(incremento < random_no):
                cad += ", "

        incremento += 1


    print(f"Serie: {cad}")
    print(f"Suma: {suma}")
        

imprimir_suma(valor_aleatorio,total, cadena)