import json

curso = None
cursos = None
json_path = './examen/cursos.json'

def leer_curso():
    nombre = input('ingrese el nombre del curso:\n')
    alumnos = int(input('ingrese la cantidad de alumnos:\n'))
    estado = 'No Iniciado'
    num_clases = int(input('ingrese el numero de clases del curso:\n'))

    return {
        'nombre' : nombre,
        'alumnos' : alumnos,
        'estado' : estado,
        'num_clases' : num_clases
    }

def crear_curso(curso):
    try:
        with open(json_path, 'r') as json_file:
            cursos = json.load(json_file)

        cursos['cursos'].append(curso)

        with open(json_path, 'w') as json_file:
            json.dump(cursos, json_file)

    except FileNotFoundError:
        cursos_json = open(json_path, 'a')
        cursos_json.write('''{"cursos" : []}''')
        cursos_json.close()
        print('cursos.json creado')
        crear_curso(curso)

def cargar_cursos():
    with open(json_path, 'r') as json_file:
        return json.load(json_file)

def mostrar_cursos_no_iniciados(cursos):
    list_temp = []
    for curso in cursos['cursos']:
        if curso['estado'] == 'No Iniciado':
            list_temp.append(curso['nombre'])

    print('Cursos no iniciados:')
    for element in list_temp:
        print(f'{(list_temp.index(element)+1)} - {element}')

    opcion = int(input('Seleccione el curso a ser dado de alta\n'))

    cursos['cursos'][opcion -1]['estado'] = 'Activo'
    guardar_cambios(cursos)

def guardar_cambios(cursos):
    with open(json_path, 'w') as json_file:
        json.dump(cursos, json_file)

def mostrar_cursos(cursos):
    index = 0
    for curso in cursos['cursos']:
        index += 1
        nombre_curso = curso.get('nombre')
        print(f'{index} - Curso: {nombre_curso}')

opcion = int(input('''
Gestion de Cursos de QA Minds Labs
1 - Crear Nuevo Curso
2 - Dar de Alta un Curso
3 - Buscar Curso
4 - Mostrar los Cursos Existentes
0 - Salir del sistema
'''))

while opcion != 0:
    if opcion == 1:
        curso = leer_curso()
        crear_curso(curso)
    elif opcion == 2:
        #dar de alta un curso
        cursos = cargar_cursos()
        mostrar_cursos_no_iniciados(cursos)
    elif opcion == 3:
        #buscar curso
        pass
    elif opcion == 4:
        cursos = cargar_cursos()
        mostrar_cursos(cursos)
    else:
        print('Valor incorrecto')
    
    opcion = int(input('''
1 - Crear Nuevo Curso
2 - Dar de Alta un Curso
3 - Buscar Curso
4 - Mostrar los Cursos Existentes
0 - Salir del sistema
'''))

