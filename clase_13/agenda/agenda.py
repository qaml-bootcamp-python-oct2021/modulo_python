from alumnos import Alumno
from utils import get_alumnos_from_file
import utils , file_handler, estados

alumnos = []

def menu_option():
    return int(input('''
    1 - Para crear un Alumno
    2 - Para buscar un Alumno
    3 - Para editar estado de Alumno
    4 - Para Mostrar Alumnos
    5 - Mostrar Alumnos por estado
    0 - Para salir
    '''))

def actualizar_agenda():
    agenda = {
        "alumnos" : []
    }
    for alumno in alumnos:
        alumno_dict = utils.convertir_alumno_to_dict(alumno)
        agenda['alumnos'].append(alumno_dict)
    file_handler.guardar_agenda(agenda)

def crear_alumno():
    nombre = input('Ingrese un nombre de Alumno\n')
    apellido = input('Ingrese un apellido de Alumno\n')
    email = input('Ingrese un mail de Alumno\n')
    alumno = Alumno(nombre,apellido,email)
    alumnos.append(alumno)
    actualizar_agenda()

def mostrar_alumnos():
    global alumnos
    alumnos = utils.get_alumnos_from_file()
    for alumno in alumnos:
        print('---- Alumno ----')
        imprimir_datos_alumno(alumno)
        print()

def buscar_alumno():
    nombre = input('Ingrese un nombre de Alumno\n')
    alumnos = utils.get_alumnos_from_file()
    index = 0
    result = False
    while index < len(alumnos) and not result:
        alumno :Alumno = alumnos[index]
        if nombre == alumno.get_nombre():
            return alumno
        index += 1
    if not result:
        print('No existe un Alumno con ese nombre')
    return None

def imprimir_datos_alumno(alumno : Alumno):
    print(alumno.get_info())

def editar_estado_alumno(alumno : Alumno):
    print(f'El estado actual de {alumno.get_nombre()} es: {alumno.get_estado()}')
    opcion = input('Desea modificar el estado? Y/N\n')
    if opcion == 'Y':
        opcion_estado = int(input(f'''
        1 - Para {estados.ACTIVO}
        2 - Para {estados.MORA}
        3 - Para {estados.RETIRADO}
        4 - Para {estados.EGRESADO}
        5 - Para {estados.CERTIFICADO}
        '''))
        guardar = False

        if opcion_estado == 1:
            alumno.set_estado(estados.ACTIVO)
            guardar = True
        elif opcion_estado == 2:
            alumno.set_estado(estados.MORA)
            guardar = True
        elif opcion_estado == 3:
            alumno.set_estado(estados.RETIRADO)
            guardar = True
        elif opcion_estado == 4:
            alumno.set_estado(estados.EGRESADO)
            guardar = True
        elif opcion_estado == 5:
            alumno.set_estado(estados.CERTIFICADO)
            guardar = True
        else:
            print('Opcion invalida, intente de nuevo.')
        
        if guardar:
            alumno_dict = utils.convertir_alumno_to_dict(alumno)
            file_handler.guardar_alumno(alumno_dict)

alumnos = get_alumnos_from_file()

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        crear_alumno()
    if opcion == 2:
        alumno = buscar_alumno()
        if alumno is not None:
            imprimir_datos_alumno(alumno)
    if opcion == 3:
        alumno = buscar_alumno()
        editar_estado_alumno(alumno)
    if opcion == 4:
        mostrar_alumnos()

    opcion = menu_option()