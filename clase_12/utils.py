from clase_12.alumnos import Alumno


def convertir_alumno_to_dict(alumno : Alumno):
    dict_alumno = {
        "nombre" : alumno.get_nombre(),
        "apellido" : alumno.get_apellido(),
        "email" : alumno.get_email(),
        "estado" : alumno.get_estado()
    }
    return dict_alumno