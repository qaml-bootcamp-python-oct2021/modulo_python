
#OBTENER TIPO DE VARIABLE
x = 5
print(type(x))

#CONVERTIR CADENA A ENTERO
x = '5'
y = int(x)
print(type(y))

#ERROR
x = 'hola'
print(type(x))
y = int(x)
print(type(y))

#CONVERTIR A DIFERENTE BASE
...

#EN PYTHON LAS VARIABLES SON DINAMICAS
x = 21
x = 5.2

print(x)

#CASTEO DE VARIABLES, CAMBIAR UN DATO DE UN TIPO A OTRO TIPO
# SIEMPRE Y CUANDO SEA COMPATIBLE (STRING DE NUMEROS A FLOAT/INT)
i = 21
f = 5.2
s = '12.5'

print(type(f))
print(f)

print(type(float(s))) #MISMO RESULTADO

#USO DE COMILLAS, ESCAPE, ESCAPADO
escape = "Hola \"QA\" Minds"
print(escape)
escape = 'Hola \'QA\' Minds'
print(escape)
escape = 'Hola \"QA\" Minds'
print(escape)
escape = "Hola \'QA\' Minds"
print(escape)
print('''Hola "QA" minds''')

#INT Y FLOAT
int_number = 10
float_number = 7.35

str_number = str(int_number)
print(type(str_number))
print(str_number)

str_number = str(float_number)
print(type(str_number))
print(str_number)

#CADENAS DE TEXTO
long_text = 'First line\nSecond line\n!"#$%&/()=?¡\n'
print(long_text)

x = False
print(type(str(x)))
print(x)

#AL EXISTIR INFORMACION EN LA CADENA, ES EQUIVALEMNTE A 1(TRUE)
x = "hola"
print(bool(x))

#NONE = NULL, UN BOJETO QUE NO TIENE VALOR, ES NADA
x = None
print(bool(x))

#MODULO(%) ES EL RESIDUO QUE QUEDA DE UNA DIVISION
#EXPONENCIAL(**)
suma = 1+3
resta = 4-1
multiplicacion = 3*3
division = int(7/3)
modulo = 25%5
exponencial = 3**3
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(modulo)
print(exponencial)

#PRIORIDAD DE OPERADORES(IZQUIERDA A DERECHA)
#01-PARENTESIS
#02-EXPONNETE
#03-MULTIPLICACION,DIVISION
#04-SUMA,RESTA
#(A+B)*C+D
a=1
b=2
c=3
d=4
resultado = (a+b)*c+d
print(resultado)



import datetime
print(datetime.date.today())
print(
    datetime.
    date.
    today()
)


#FORMATEAR UN STRING
name="David"
lastname="Gonzalez"
fullname=name+" "+lastname
print(fullname)

name='David'
lastname='Gonzalez'
fullname='{} {}'.format(name,lastname)
fullname2=f'{name} {lastname}'
print(fullname)
print(fullname2)

name='David'
lastname='Gonzalez'
edad=33
pais='Argentina'
sexo='Masculino'
hijos=False

fullname3='Hola {} {}, tienes {}, vivis en {} sos de sexo {} y tienes {} hijos'.format(name,lastname,edad,pais,sexo,hijos)
fullname4=f'Hola {name} {lastname}, tienes {edad}, vivis en {pais} sos de sexo {sexo} y tienes {hijos} hijos'

print(fullname3)
print(fullname4)


