from alumnos import Alumno
import utils , file_handler, estados

alumnos = utils.get_alumnos_from_file()

def menu_option():
    return int(input('''
    1 - Para crear un Alumno
    2 - Para buscar un Alumno
    3 - Para editar estado de Alumno
    4 - Para Mostrar Alumnos
    5 - Mostrar Alumnos por estado
    0 - Para salir
    '''))

def crear_alumno():
    nombre = input('Ingrese un nombre de Alumno\n')
    apellido = input('Ingrese un apellido de Alumno\n')
    email = input('Ingrese un mail de Alumno\n')
    alumno = Alumno(nombre,apellido,email)
    alumnos.append(alumno)
    actualizar_agenda()

def actualizar_agenda():
    agenda = {
        "alumnos" : []
    }
    for alumno in alumnos:
        alumno_dict = utils.convertir_alumno_to_dict(alumno)
        agenda['alumnos'].append(alumno_dict)
    file_handler.guardar_agenda(agenda)

def buscar_alumno():
    nombre = input('Ingrese un nombre de Alumno\n')
    index = 0
    while index < len(alumnos):
        alumno :Alumno = alumnos[index]
        if nombre == alumno.get_nombre():
            return alumno
        index += 1
    
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
        guardar = utils.setear_estado(alumno,opcion_estado)
        
        if guardar:
            actualizar_alumno(alumno)
            actualizar_agenda()
            print('Estado actualizado satisfactoriamente')
            
def actualizar_alumno(alumno : Alumno):
    index = 0
    result = False
    while index < len(alumnos) and not result:
        alumno_lista :Alumno = alumnos[index]
        if alumno.get_nombre() == alumno_lista.get_nombre():
            alumnos[index] = alumno
            result = True
        index += 1
    if not result:
        print('No hay alumno en el listado de Alumnos con ese nombre.')

def mostrar_alumnos():
    for alumno in alumnos:
        print('---- Alumno ----')
        imprimir_datos_alumno(alumno)
        print()

def buscar_alumnos_estado():
    opcion_estado = int(input(f''' Ingrese la opcion de estado a buscar
        1 - Para {estados.ACTIVO}
        2 - Para {estados.MORA}
        3 - Para {estados.RETIRADO}
        4 - Para {estados.EGRESADO}
        5 - Para {estados.CERTIFICADO}
        '''))

    estado = utils.convertir_opcion_estado(opcion_estado)
    if estado is not None:
        for alumno in alumnos:
            alumno : Alumno    
            if alumno.get_estado() == estado:
                imprimir_datos_alumno(alumno)
    else:
        print('El estado ingresado es invalido. Intente de nuevo')

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
        if alumno is not None:
            editar_estado_alumno(alumno)
    if opcion == 4:
        mostrar_alumnos()
    if opcion == 5:
        buscar_alumnos_estado()

    opcion = menu_option()