#Tienes dos variables a=12.5 y b=34, crea funciones que permitan calcular la suma, resta, multiplicación y división positiva, como también el valor del módulo de b entre a 
a=12.5
b=34
#Suma
def suma (a,b):
    total = a+b
    return total
print(f'Suma: {suma(a,b)}')

#Resta
def resta(a,b):
    total = b-a
    return total
print(f'Resta: {resta(a,b)}')

#Multiplicación
def multiplicacion(a,b):
    total = a*b
    return total
print(f'Multiplicación: {multiplicacion(a,b)}')

#División
def division(a,b):
    total = b/a
    return total
print(f'División: {division(a,b)}')

#Módulo
def modulo(a,b):
    total = b%a 
    return total
print(f'Módulo: {modulo(a,b)}')

#Crear un método que permita convertir cualquier número entero a flotante 

def convertir(entero):
    convierte = float(entero)
    return convierte
print(f'Flotante: {convertir(5)}')