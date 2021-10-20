#Ejercicio 5.02 - Tony De La Torre

a = 12.5
b = 34

def suma(num1,num2):
    res = num1 + num2
    return res

def resta(num1,num2):
    res = num1 - num2
    return res

def mult(num1,num2):
    res = num1 * num2
    return res

def div(num1,num2):
    res = num1 / num2
    return res

def modulo(num1,num2):
    res = num1 % num2
    return res

def entero_a_flotante(num1):
    res = float(num1)
    return res

resultado = suma(a,b)
print(f"Suma de {a} y {b} es {resultado}")

resultado = resta(a,b)
print(f"Resta de {a} y {b} es {resultado}")

resultado = mult(a,b)
print(f"Multiplicación de {a} por {b} es {resultado}")

resultado = div(a,b)
print(f"División de {a} entre {b} es {resultado}")

resultado = modulo(a,b)
print(f"Módulo de {a} entre {b} es {resultado}")

resultado = entero_a_flotante(b)
print(f"Convirtiendo entero {b} a flotante {resultado}")
