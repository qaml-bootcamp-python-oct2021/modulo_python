from alumnos import Alumno
import file_handler , estados

def convertir_alumno_to_dict(alumno : Alumno):
    dict_alumno = {
        "nombre" : alumno.get_nombre() ,
        "apellido" : alumno.get_apellido(),
        "email" : alumno.get_email(),
        "estado" : alumno.get_estado()
    }
    return dict_alumno

def get_alumnos_from_file():
    list_alumnos = []
    agenda = file_handler.leer_agenda()
    alumnos = agenda['alumnos']
    for alumno in alumnos:
        alumno_o = Alumno(alumno['nombre'],alumno['apellido'],alumno['email'])
        alumno_o.set_estado(alumno['estado'])
        list_alumnos.append(alumno_o)
    return list_alumnos

def convertir_opcion_estado(opcion):
    if opcion == 1:
        return estados.ACTIVO
    elif opcion == 2:
        return estados.MORA
    elif opcion == 3:
        return estados.RETIRADO
    elif opcion == 4:
        return estados.EGRESADO
    elif opcion == 5:
        return estados.CERTIFICADO
    else:
        return None

def setear_estado(alumno : Alumno, opcion_estado):
    guardar = True
    if opcion_estado == 1:
        alumno.set_estado(estados.ACTIVO)
    elif opcion_estado == 2:
        alumno.set_estado(estados.MORA)
    elif opcion_estado == 3:
        alumno.set_estado(estados.RETIRADO)
    elif opcion_estado == 4:
        alumno.set_estado(estados.EGRESADO)
    elif opcion_estado == 5:
        alumno.set_estado(estados.CERTIFICADO)
    else:
        print('Opcion invalida, intente de nuevo.')
        guardar = False
    return guardar