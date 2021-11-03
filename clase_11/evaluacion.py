cursosQA = {
    'cursos' : []
}

def altaCurso():
    nombreCurso = input('Nombre del curso: ')
    cantidadAlumnos = input('Cantidad de alumnos: ')
    estadoCurso = input('Estado del curso (No iniciado = X, Activo = O): ')
    cantidadClases = input('Cantidad de clases en el curso: ')
    curso = {
        'nombre_Curso' : nombreCurso,
        'cantidad_Alumnos' : cantidadAlumnos,
        'estado_Curso' : estadoCurso,
        'cantidad_Clases' : cantidadClases
    }
    return curso

def buscarCurso():
    cursoBuscado = input('Nombre del curso: ')
    index = 0
    while index < len(cursosQA['cursos']):
        curso = cursosQA['cursos']
        encontrado = curso[index]
        if encontrado['nombre_Curso'] == cursoBuscado:
            modificar = input('¿Deseas actualizar el estado? Y/N: ')
            if modificar == 'Y':
                modificarCurso()
        index += 1
        return encontrado
    return None

def modificarCurso(encontrado):
    if encontrado['estado_Curso'] == 'X':
        cursosQA['estado_Curso'] = 'O'
    else:
        cursosQA['estado_Curso'] = 'X'
    

def mostrarCursos():
    for curso in cursosQA['cursos']:
        for key, value in curso.items():
            if key == 'pais':
                print(f'{key}: {value}')

opcion = int(input('''
¿Que deseas hacer?
1. Dar de alta un curso
2. Buscar un curso
3. Modificar un curso
4. Mostrar los cursos existentes
0 - Para salir
'''))

while opcion != 0:
    if opcion == 1:
        altaCurso()
    elif opcion == 2:
        buscarCurso()
    elif opcion == 3:
        buscarCurso()
        modificarCurso()
        if curso is None:
            print('El curso no existe. Intente con otro')
    elif opcion == 4:
        mostrarCursos()
    else:
        print('opcion errada, intente de nuevo')
        opcion = int(input('''
        ¿Que deseas hacer?
        1. Dar de alta un curso
        2. Buscar un curso
        3. Modificar un curso
        4. Mostrar los cursos existentes
        0 - Para salir
        '''))