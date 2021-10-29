#DICCIONARIO: GUARDA LA INFORMACION EN PAREJAS CLAVE(KEY) Y VALOR(VALUE)
my_dict = {}
my_dict = dict()
my_dict = {
    'key1':'value1',
    'key2':'value2'
}

#LAS LLAVES Y LOS VALORES PUEDEN SER DE CUALQUIER TIPO DE DATO,
#PERO SE RECOMIENDA QUE LAS LLAVES SEAN DEL MISMO TIPO
my_dict = {
    'nombre_bootcamp':'Python',
    'alumnos':8
}

my_dict = {
    0:'value1',
    1:'value2'
}

#PARA ACCEDER A UN VALOR ESPECIFICO SE UTILIZA LA CLAVE CON LA SIGUIENTE SINTAXIS
#my_dict['key']
#KEY ES EL NOMBRE DE LA CLAVE AL ELEMENTO QUE SE QUIERE ACCEDER
my_dict = {
    'nombre':'Cristian',
    'apellido':'Briones'
}

print(my_dict['apellido'])

#METODO GET():
#RECIBE COMO PARAMETRO UNA KEY Y DEVUELVE EL VALOR DE LA MISMA
#SI LA KEY NO EXISTE DEVUIELVE NONE
#EN CASO DE EXISTIR UN SEGUNDO PARAMTRO, SERA LO QUE DEVOLVERA
my_dict = {
    'nombre':'Cristian',
    'apellido':'Briones'
}

print(my_dict.get('email','Esa llave no existe'))
print(my_dict.get('apellido'))

#LOS DICCIONARIOS MODIFICAN UN VALOR DE KEY IGUAL QUE LAS LISTAS
my_dict = {
    'nombre':'Cristian',
    'apellido':'Briones',
    'edad' : 29
}

my_dict['edad'] = 34

print(my_dict)

#PARA AGREGAR UN NUEVO ELEMENTO AL DICCIONARIO:
#my_dict['key']=value
my_dict = {
    'nombre':'Cristian',
    'apellido':'Briones',
    'edad' : 29
}

my_dict['fechaNacimiento'] = 1992
print(my_dict)

#PARA ELIMINAR UN ELEMENTO DEL DICCIONARIO SE UTILIZA pop()
#RECIBE EL NOMBRE DE LA KEY A ELIMINAR
#OBTIENE EL VALOR Y LUEGO LO ELIMINA EN CASO DE QUE SE OCUPE MAS ADELANTE EN UNA VARIABLE
#my_dict.pop('key')
#my_dict.pop('key','default_value')

#PARA VERIFICAR SI UN ELEMENTO EXISTE EN EL DICCIONARIO SE UTILIZA UN CONDICIONAL CON LA CLAVE SEGUIDO DE LA PALABRA in
if 'nombre' in my_dict:
    print(my_dict['nombre'])

#TAMBIEN SE PUEDE UTILIZAR EL METODO GET() PARA VERIFICAR
if my_dict.get('nombre') is not None:
    print(my_dict['nombre'])

#LOS DICCIONARIOS PUEDEN TENER MULTIPLES ELEMENTOS CON MISMOS key_value, YA QUE PUEDEN ESTAR COMPUESTOS POR LISTAS
alumnos = {
    'alumnos' : [
        {
            'nombre' : 'alumno A',
            'edad' : 27,
            'pais' : 'Mexico'
        },
        {
            'nombre' : 'alumno B',
            'edad' : 22,
            'pais' : 'Venezuela'
        },
        {
            'nombre' : 'alumno C',
            'edad' : 33,
            'pais' : 'Argentina'
        }
    ]
}

#PARA OBTEENR LOS VALORES DE CADA ALUMNO ES NECESARIO HACER UNA DOBLE ITERACION
#LA PRIMERA PARA OBTENER LA LISTA DE ALUMNOS
#LA SEGUNDA PARA OBTENER LAS KEY-VALUE DE CADA ALUMNO
for alumno in alumnos['alumnos']:
    for key, value in alumno.items():
        print('{} {}'.format(key,value))

for alumno in alumnos['alumnos']:
    for key, value in alumno.items():
        if key == 'pais':
            print(f'La key {key} tiene el valor {value}')

#PARA AGREGAR UN NUEVO ALUMNO ES NECESARIO CREAR UN DICCIONARIO Y LUEGO SUMARLO A LA LISTA
nombre_alumno = 'Alumno D'
edad_alumno = 30
pais_alumno = 'Mexico'

nuevo_alumno = {
    'nombre' : nombre_alumno,
    'edad' : edad_alumno,
    'pais' : pais_alumno 
}

alumnos['alumnos'].append(nuevo_alumno)

for alumno in alumnos['alumnos']:
    for key, value in alumno.items():
        if key == 'nombre':
            print(f'La key {key} tiene el valor {value}')

#PARA OBTENER TODAS LAS KEYS QUE PUEDEN POSEER UN DICCIONARIO, ES POSIBLE REALIZARLO POR MEDIO DEL METODO keys().
my_dict = {
    'NombreBootcamp' : 'Python',
    'Alumnos' : 8
}

my_dict['Profesor'] = 'David'

for key in my_dict.keys():
    print(key)

#PARA OBTENER TODOS LOS VALORES QUE PUEDE POSEER UN DICCIONARIO, ES POSIBLE REALIZARLO POR MEDIO DEL METODO values().
my_dict = {
    'NombreBootcamp' : 'Python',
    'Alumnos' : 8
}

my_dict['Profesor'] = 'David'

for value in my_dict.values():
    print(value)