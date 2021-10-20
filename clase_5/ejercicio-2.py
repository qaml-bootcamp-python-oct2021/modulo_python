def sum(a,b):
    return a+b
def subs(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return b/a
def mod(a,b):
    return a%b
def int_to_float(a):
    return float(a)

a = 12.5
b = 34
print(f'Suma de:  {a} + {b} es = {sum(a,b)}')
print(f'Resta de:  {a} - {b} es = {subs(a,b)}')
print(f'Multiplicacion de:  {a} * {b} es = {mul(a,b)}')
print(f'Division de:  {b} / {a} es = {div(a,b)}')
print(f'Modulo de:  {a} % {b} es = {mod(a,b)}')

number = 8
print(f'Conversion del entero:  {number} a float: {int_to_float(number)}')

    