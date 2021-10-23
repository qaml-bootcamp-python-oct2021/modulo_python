#LISTAS
my_list = list()
print(type(my_list))

#ACCEDER A UN VALOR ESPECIFICO DE LA LISTA
my_list = ['a','b','c','d','e']
print(my_list[3])

#MODIFICAR EL VALOR DE UN ELEMENTO
my_list[1] = 'B'
print(my_list)

#OBTENER LA LONGITUD DE LA LISTA
print(len(my_list))

#AGREGAR UN NUEVO ELEMENTO
my_list.append('f')
print(len(my_list))
print(my_list)

#ELIMINAR UN ELEMENTO EN UNA LISTA != del
my_list.pop(0)
print(len(my_list))
print(my_list)

#LOS INDICES NEGATIVOS NOS DEVUELVEN LOS ELEMENTOS DE LA LISTA DEL FINAL AL INICIO
print(my_list[-1])

#ORDENAR UNA LISTA DE NUMEROS MENOR A MAYOR
my_list = [5,1,4,3,6,2]
my_list.sort()
print(my_list)

#REVERSE NOS PERMITE INVERTIR EL ORDEN DE LA LISTA
my_list = [5,1,4,3,6,2]
my_list.reverse()
print(my_list)

