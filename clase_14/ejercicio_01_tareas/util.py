from tarea import Tarea
from estado_enum import Estado
from usuario import Usuario

def diccionario_to_usuario(usuario_dicc):
        return (Usuario(usuario_dicc['nombre'],usuario_dicc['email']))

def diccionario_to_usuarios(list_dicc_usuarios):
    list_usuarios = []
    for usuario_dicc in list_dicc_usuarios:
        list_usuarios.append(diccionario_to_usuario(usuario_dicc))
    return list_usuarios


def usuario_to_diccionario(usuario : Usuario):
    return  {
        "nombre" : usuario.get_nombre() ,
        "email" : usuario.get_email(),
    }
def diccionario_to_tareas(list_dicc_tarea):
    list_tarea = []
    for tarea_dicc in list_dicc_tarea:
        tarea_objeto=Tarea(tarea_dicc['titulo'],tarea_dicc['descripcion'],
        tarea_dicc['prioridad'], diccionario_to_usuario(tarea_dicc['usuario']))
        tarea_objeto.set_estado(tarea_dicc['estado']);
        list_tarea.append(tarea_objeto)
    return list_tarea

def tarea_to_diccionario(tarea :Tarea):
    return  {
        "titulo" : tarea.get_titulo() ,
        "descripcion" : tarea.get_descripcion(),
        "prioridad" : tarea.get_prioridad(),
        "estado" : tarea.get_estado(),
        "usuario" : usuario_to_diccionario(tarea.get_usuario()),
    }

def get_estado_opcion():
    opcion_estado='Ingrese::::\n'
    for estado in Estado:
        opcion_estado+= f'{estado.value} - Para {estado.name} \n'
    return opcion_estado

def validar_estado_opcion(opcion_estado):
    try:
        return Estado(opcion_estado)
    except ValueError:
        print('Opción invalida, intente de nuevo.') 
        return None
