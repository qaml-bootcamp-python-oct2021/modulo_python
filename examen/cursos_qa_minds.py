import json
data = None

qa_cursos = {
    'cursos' : []
}

def crear_curso():
    nombre_curso = input('Ingrese nombre del curso\n')
    alumnos = input('Ingrese la cantidad de alumnos\n')
    status = input('Ingrese el status del curso (No Iniciado, Activo)\n')
    clases = input('Ingrese la cantidad de clases del curso\n')
    curso = {
        'nombre_curso' : nombre_curso,
        'alumnos' : alumnos,
        'status' : status,
        'clases' : clases
    }
    
    return curso

def guardar_curso(curso):
    qa_cursos['cursos'].append(curso)
    with open('./examen/cursos.json','w') as cursos:
        json.dump(qa_cursos,cursos)

def mostrar_cursos():
    with open('./examen/cursos.json','r') as cursos:
       data = json.load(cursos)
    for curso in data['cursos']:
        mostrar_info_curso(curso)

def get_curso():
    return input('Ingrese nombre del curso a buscar\n')

def buscar_curso(nombre_curso):
    index = 0
    while index < len(qa_cursos['cursos']):
        cursos = qa_cursos['cursos'] 
        curso = cursos[index]
        if curso['nombre_curso'] == nombre_curso:
            return curso
        index += 1
    return None

def mostrar_info_curso(curso):
    for key, value in curso.items():
        print(f'{key} - {value}')

def modificar_status_curso(curso):
    status = curso['status']
    print(f'Este curso tiene status: {status} ')
    nuevo_status = input(f'Cambiar status a:\n')
    curso['status'] = nuevo_status
    


opcion = int(input('''
Utilice las siguentes opciones:
1 - Para dar de alta un curso
2 - Para ver todos los cursos disponibles
3 - Para buscar un curso
4 - Para modificar status de curso
0 - Para salir
'''))

while opcion != 0:
    if opcion == 1:
        curso = crear_curso()
        guardar_curso(curso)
    elif opcion == 2:
        mostrar_cursos()
    elif opcion == 3:
        nombre_curso = get_curso()
        curso = buscar_curso(nombre_curso)
        if curso is not None:
            mostrar_info_curso(curso)
        else:
            print('El curso ingresado no existe. Intente de nuevo')
    elif opcion == 4:
        nombre_curso = get_curso()
        curso = buscar_curso(nombre_curso)
        if curso is not None:
            modificar_status_curso(curso)
        else:
            print('El curso ingresado no existe. Intente de nuevo')
        
    else:
        print('Elija una opcion correcta, intente de nuevo')

    opcion = int(input('''
Utilice las siguentes opciones:
1 - Para dar de alta un curso
2 - Para ver todos los cursos disponibles
3 - Para buscar un curso
4 - Para modificar status de curso
0 - Para salir
'''))