from alumno import Alumno
def diccionario_to_alumno(list_dicc_alumnos):
    list_alumnos = []
    
    for alumno in list_dicc_alumnos:
        alumno_objeto= Alumno(alumno['nombre'],alumno['apellido'],alumno['email'])
        alumno_objeto.set_estado(alumno['estado'])
        list_alumnos.append(alumno_objeto)
    return list_alumnos

def alumno_to_diccionario(alumno : Alumno):
    return  {
        "nombre" : alumno.get_nombre() ,
        "apellido" : alumno.get_apellido(),
        "email" : alumno.get_email(),
        "estado" : alumno.get_estado()
    }