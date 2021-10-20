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
    resultado = num_b % num_a
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

#script compra de 2 productos
billetera = 200
chocolate = 150
agua = 100

def comprar_2_productos(producto_1, producto_2):
    costo_total = producto_1 + producto_2
    return costo_total

def calcular_saldo(billetera, costo_total):
    saldo = billetera - costo_total
    return saldo

def comprar_1_producto(producto_1):
    costo_total = producto_1
    return costo_total

#print costo total
print(f'costo total es {comprar_2_productos(chocolate, agua)}')
#print dinero disponible
print(f'dinero disponible es {billetera}')
#print el usuario tiene dinero suficiente
print(f'puede comprar? {(comprar_2_productos(chocolate,agua)<billetera)}')

#segundo escenario
print("segundo escenario")
print(f'puede comprar? {(comprar_1_producto(chocolate)<billetera)}')
print(f'puede comprar? {(comprar_1_producto(agua)<billetera)}')