#imprime la cadena: Bienvenidos a 'QA' "Minds"!!!
print("""Bienvenidos a 'QA' "Minds"!!!""")

#Imprime la cadena: "I Love
#                   Python
#                   <3"
print('''
    I Love
    Python
    <3 ''')

a = 12.5
b = 34

#funcion suma
def sumar(num_a, num_b):
    resultado = num_a + num_b
    return resultado

#funcion resta
def restar(num_a, num_b):
    resultado = num_a - num_b
    return resultado

#funcion multiplicacion
def multiplicar(num_a, num_b):
    resultado = num_a * num_b
    return resultado

#funcion division positiva
def dividir(num_a, num_b):
    resultado = num_b / num_a
    return resultado

#funcion modulo b entre a
def sacar_modulo(num_a, num_b):
    resultado = num_b / num_a
    return resultado

#funcion convertir entero a flotante
def to_float(num):
    resultado = float(num)
    return resultado

print(sumar(a,b))
print(restar(a,b))
print(multiplicar(a,b))
print(dividir(a,b))
print(sacar_modulo(a,b))
print(to_float(b))