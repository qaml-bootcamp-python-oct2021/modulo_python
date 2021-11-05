import json, os

ESTADO_INACTIVO = 'Inactivo'
ESTADO_ACTIVO = 'Activo'

CURSOS_FILE = './clase_12/cursos.json'

qa_minds = {
    'cursos' : []
}

def archivo_existe():
    if not os.path.exists(CURSOS_FILE):
        with open(CURSOS_FILE,'w') as file:
            json.dump(qa_minds,file)

def menu_option():
    return int(input('''
    1 - Para crear un curso
    2 - Para visualizar todos los cursos
    3 - Para buscar un curso
    4 - Para editar estado de curso
    0 - Para salir
    '''))

def obtener_datos_curso():
    nombre = input('Ingrese un nombre de curso\n')
    alumnos = input('Ingrese cantidad de alumnos del curso\n')
    clases = input('Ingrese cantidad de clases del curso\n')
    curso = {
        'nombre' : nombre,
        'alumnos' : alumnos,
        'estado' : ESTADO_INACTIVO,
        'clases' : clases
    }
    return curso

def leer_cursos():
    archivo_existe()
    with open(CURSOS_FILE,'r') as file:
        data = json.load(file)
    return data

def mostrar_cursos():
    data = leer_cursos()
    cursos = data['cursos']
    print('---- Listado de Cursos ----')
    for curso in cursos:
        print(f'Nombre de curso:{curso["nombre"]}')

def guardar_curso(curso):
    data = leer_cursos()
    data['cursos'].append(curso)
    with open(CURSOS_FILE,'w') as file:
        json.dump(data,file)

def mostrar_curso(nombre_curso):
    data = leer_cursos()
    cursos = data['cursos']
    index = 0
    result = False
    while index<len(cursos) and not result:
        curso = cursos[index]
        if nombre_curso == curso['nombre']:
            print(curso)
            result = True
        index +=1
    if not result:
        print('No existe curso con ese nombre')

def modificar_estado_curso(nombre_curso):
    data = leer_cursos()
    cursos = data['cursos']
    index = 0
    result = False
    while index<len(cursos) and not result:
        curso = cursos[index]
        if nombre_curso == curso['nombre']:
            estado = curso["estado"]
            print(f'El estado del curso es: {estado}')
            if estado == ESTADO_ACTIVO:
                opcion = input('Desea cambiar de estado Activo a Inactivo?, Presione Y para confirmar o N para cancelar\n')
                if opcion == 'Y':
                    curso["estado"] = ESTADO_INACTIVO
                    guardar_data(data)
            else:
                opcion = input('Desea cambiar de estado Inactivo a Activo?, Presione Y para confirmar o N para cancelar\n')
                if opcion == 'Y':
                    curso["estado"] = ESTADO_ACTIVO
                    guardar_data(data)
            result = True
        index +=1
    if not result:
        print('No existe curso con ese nombre')

def guardar_data(data):
    with open(CURSOS_FILE,'w') as file:
        json.dump(data,file)

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        curso = obtener_datos_curso()
        guardar_curso(curso)
    elif opcion == 2:
        mostrar_cursos()
    elif opcion == 3:
        nombre = input('Ingrese un nombre del curso\n')
        mostrar_curso(nombre)
    elif opcion == 4:
        nombre = input('Ingrese un nombre del curso\n')
        modificar_estado_curso(nombre)
    else:
        print('Opcion invalida, intente de nuevo')

    opcion = menu_option()