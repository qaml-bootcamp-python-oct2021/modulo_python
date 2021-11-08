from alumnos import Alumno
import utils, file_handler

def menu_option():
    return int(input('''
        1. Para crear un alumno
        2. Para buscar un aalumno
        3. Para editar estado de Alumno
        4. Para mostrar alumnos
        5. Mostrar alumnos por estado
        0. Salir
    '''))

def crear_alumno():
    nombre = input('Ingrese nombre de alumno\n')
    apellido = input('Ingrese apellido de alumno\n')
    email = input('Ingrese email de alumno\n')
    alumno = Alumno(nombre,apellido,email)
    alumno_dict = utils.convertir_alumno_to_dict(alumno)

    print(alumno_dict)


def obtener_datos_alumno():
    nombre = input('Ingrese nombre de alumno\n')
    apellido = input('Ingrese apellido de alumno\n')
    email = input('Ingrese email de alumno\n')
    alumno = Alumno(nombre,apellido,email)
    alumno_dict = utils
    return

opcion = menu_option()

while opcion != 0 :
    if opcion == 1:
        crear_alumno()

    opcion = menu_option()