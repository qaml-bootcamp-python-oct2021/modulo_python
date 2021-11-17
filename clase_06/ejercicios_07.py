#Imprime todos los números del 0 al 99, de dos en dos y que no sean multiplos de 3

for numero in range(0,100,2):
    if (numero%3!=0):
        print(numero)    