#Ejercicio 7.03 - Tony De La Torre

numero_a = 1
numero_b = 4

#validar numeros de entrada
def validar_numeros(num_a, num_b):
    if (num_a == num_b):
        print(f"Ambos numeros son iguales: {num_a}, {num_b}")
        return False
    elif (num_a > num_b):
        print(f"Primer número es mayor al segundo: {num_a}, {num_b}")
        return False
    else:
        return True

#imprimiendo numeros entre A y B
def imprimir_numeros(num_a, num_b):
    if (validar_numeros(num_a,num_b)):
        print(f"Los siguientes numeros se encuentran entre {num_a} y {num_b}:")
        num_a += 1
        while (num_a < num_b):
            print(f"* {num_a}")
            num_a += 1
        

imprimir_numeros(numero_a,numero_b)
