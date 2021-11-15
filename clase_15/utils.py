from usuario import Usuario
from tareas import Tareas
import file_handler,estados

def convertir_usuario_a_dicc(usuario:Usuario):
    return {
        'nombre' : usuario.get_nombre(),
        'email' : usuario.get_email()
    }

def diccionario_to_usuario(usuario_dicc):
        return (Usuario(usuario_dicc['nombre'],usuario_dicc['email']))

def convertir_tarea_a_dicc(tarea:Tareas):
    return {
        'titulo' : tarea.get_titulo(),
        'descripcion' : tarea.get_descripcion(),
        'prioridad' : tarea.get_prioridad(),
        'estado' : tarea.get_estado(),
        'usuario' : convertir_usuario_a_dicc(tarea.get_usuario())
    }

def get_usuarios_from_file():
    usuarios_lista = []
    usuarios_archivo = file_handler.leer_usuario_file()
    usuarios = usuarios_archivo['usuario']
    for usuario in usuarios:
        objeto_usuario = Usuario(usuario['nombre'],usuario['email'])
        usuarios_lista.append(objeto_usuario)
    return usuarios_lista

def get_tareas_from_file():
    tareas_lista = []
    tareas_archivo = file_handler.leer_tareas_file()
    tareas = tareas_archivo['tarea']
    for tarea in tareas:
        objeto_tarea = Tareas(tarea['titulo'],tarea['descripcion'],tarea['prioridad'])
        objeto_tarea.set_estado(tarea['estado'])
        objeto_tarea.set_usuario(diccionario_to_usuario(tarea['usuario']))
        tareas_lista.append(objeto_tarea)
    return tareas_lista

def setear_estado(tarea : Tareas, opcion_estado):
    guardar = True
    if opcion_estado == 1:
        tarea.set_estado(estados.BACKLOG)
    elif opcion_estado == 2:
        tarea.set_estado(estados.TODO)
    elif opcion_estado == 3:
        tarea.set_estado(estados.DOING)
    elif opcion_estado == 4:
        tarea.set_estado(estados.RESOLVED)
    else:
        print('Opcion invalida, intenta de nuevo.')
        guardar = False
    return guardar

def convertir_opcion_estado(opcion):
    if opcion == 1:
        return estados.BACKLOG
    elif opcion == 2:
        return estados.TODO
    elif opcion == 3:
        return estados.DOING
    elif opcion == 4:
        return estados.RESOLVED
    else:
        return None