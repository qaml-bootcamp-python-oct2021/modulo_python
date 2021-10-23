#Ejercicio 7.07 - Tony De La Torre


#imprimiendo serie de numeros entre 1 y 99 cuando el número no es par ni múltiplo de 3
def imprimir_serie():

    cad = ''

    for number in range(1,100,1):
        if not (number % 2 == 0 and number % 3 == 0):
            cad += f"{number}, "

    print(cad)

imprimir_serie()