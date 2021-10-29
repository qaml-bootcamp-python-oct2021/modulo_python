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

#ELIMINAR UN ELEMENTO EN UNA LISTA ES DIFERENTE A 'del'
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

#FORMAS DE RECORRER LAS LISTAS
#WHILE
my_list = [1,2,3,4]
total_numbers = len(my_list)
count = 0
while count < total_numbers:
    print(my_list[count])
    count += 1
#FOR
my_list = [1,2,3,4]
for number in my_list:
    print(number)

#SLICING
#my_list[start:end:step]
my_list = [1,2,3,4,5,6,7,8,9]
nueva_lista = my_list[3:6:1]
print(nueva_lista)

#JOIN: PARA CONVERTIR UNA LISTA EN UN STRING
#string = 'delimeter'.join(list)
my_list = ['red','green','blue']
string_list = '-'.join(my_list)
print(string_list)

#SPLIT: PARA CONVERTIR UN STRING EN UNA LISTA
#my_list = 'string'.split('delimeter','max_split')

string_list = '1-2-3-4-5-6-7-8-9'
list_string = string_list.split('-')
print(list_string)

#EXTEND: PERMITE AGREGAR MULTIPLES ELEMENTOS O EXTENDER LA MISMA
#list_a.extend(list_b)
list_a = [1,2,3,4,5]
list_b = [6,7,8,9]

print(list_a)
list_a.extend(list_b)
print(list_a)

#APPEND, agrega el objeto lista
list_a = ['a','b','c']
list_b = [1,2,3]
print(list_a)
list_a.append(list_b)
print(list_a)

#EXTEND VS APPEND
#EXTEND AGREGA CADA ELEMENTO DE FORMA INDIVIDUAL A CADA VALOR DE LA LISTA
#APPEND AGREGA COMO OBJETO NUEVO A LA LISTA B

#CONCATENAR
list_a = [1,2,3,4,5]
list_b = [6,7,8,9]
list_a += list_b
print(list_a)

#CLONAR, PERMITE CREAR UNA LISTA EN BASE A OTRA EXISTENTE
#list_b = list(list_a)
list_a = [1,2,3,4,5]
list_b = list(list_a)
list_c = list_a
#FALSE
print(list_a is list_b)
#TRUE
print(list_a is list_c)

print(list_a)
print(list_b)
print(list_c)

#COUNT, RECIBE COMO PARAMETRO EL ELEMENTO QUE QUEREMOS CONTAR, DEVUELVE EL NUMERO DE VECES QUE APARECE DICHO ELEMENTO
list_a = ['A','B','C','A','B','A']
print(list_a.count('A'))