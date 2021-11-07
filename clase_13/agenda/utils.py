from alumnos import Alumno
import file_handler

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