#ASIGANCION INCREMENTAL, CONCATENACION
numerica = 5
numerica += 7.5
print(numerica)

var = 'Hola'
var += ' mundo'
print(var)

#ASIGNACION DECREMENTAL
var = 5
var -= 4
print(var)

#OPERADOR INCREMENTAL *=
#MULTIPLICA LA VARIABLE DEL LADO IZQUIERDO EL VALOR DEL LADO DERECHO
var = 3
var *= 2
print(var)

saludo = 'Hola'
saludo *= 3
print(saludo)

#OPERADOR DECREMNTAL /=
var = 25
var /= 5
print(var)

#OTROS OPERADORES
//=
%=
**=

credito = 100
figura = 50
resultado = credito >= figura
print(resultado)

#IS / IS NOT EVALUA EL OBJETO, ES DECIR EL TIPO DE DATO QUE SE EVALUA
numa = 3.5
numb = 5
print(numa is numb)

#FUNCIONES
def comparar(dato1,dato2):
    resultado = dato1 == dato2
    print(resultado)

comparar(credito,figura)
