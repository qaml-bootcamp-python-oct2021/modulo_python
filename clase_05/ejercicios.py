print('''Bienvenidos a 'QA' "Minds"!!!''')
print('''"I Love\nPython\n'<3' "''')

a = 12.5
b = 34

def suma(a,b):
    total = a + b
    return total

def resta(a,b):
    total = b - a
    return total

def multiplicacion(a,b):
    total = a * b
    return total

def division(a,b):
    total = b/a
    return total

def modulo(a,b):
    total = b % a
    return total

def convertir(num):
    conversion = float(num)
    return conversion

print(suma(a,b))
print(resta(a,b))
print(multiplicacion(a,b))
print(division(a,b))
print(modulo(a,b))
print(convertir(7))


cantidad_billetera = 200
chocolate = 150
agua = 100

def compra1(cantidad_billetera,chocolate,agua):
    total_compra = chocolate + agua
    puedo_comprar = cantidad_billetera >= total_compra
    print(f'¿Me alcanza el dinero para un chocolate y agua? {puedo_comprar}')
    print(f'El total de la compra es: {total_compra}')

def compra2(cantidad_billetera,chocolate,agua):
    total_compra = chocolate
    puedo_comprar = cantidad_billetera >= total_compra
    print(f'¿Me alcanza el dinero para un chocolate? {puedo_comprar}')
    print(f'El total de la compra es: {total_compra}')

compra1(cantidad_billetera,chocolate,agua)
compra2(cantidad_billetera,chocolate,agua)