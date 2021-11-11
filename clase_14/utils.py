from tareas import Tarea
from usuarios import Usuario
import file_handler , estados

def convertir_tarea_to_dict(tarea : Tarea):
    dict_tarea = {
        "titulo" : tarea.get_titulo() ,
        "descripcion" : tarea.get_descripcion(),
        "prioridad" : tarea.get_prioridad(),
        "estado" : tarea.get_estado(),
        "usuario" : tarea.get_usuario()
    }
    return dict_tarea

def get_tareas_from_file():
    list_tareas = []
    dashboard = file_handler.leer_dashboard()
    tareas = dashboard['tareas']
    for tarea in tareas:
        tarea_o = Tarea(tarea['titulo'],tarea['descripcion'],tarea['prioridad'])
        tarea_o.set_estado(tarea['estado'])
        tarea_o.set_usuario(tarea['usuario'])
        list_tareas.append(tarea_o)
    return list_tareas

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

def setear_estado(tarea : Tarea, opcion_estado):
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
        print('Opcion invalida, intente de nuevo.')
        guardar = False
    return guardar

def convertir_usuario_to_dict(usuario : Usuario):
    dict_usuario = {
        "nombre" : usuario.get_nombre(),
        "email" : usuario.get_email(),
        "id" : usuario.get_id()
    }
    return dict_usuario

def get_usuarios_from_file():
    list_usuarios = []
    dashboard_users = file_handler.leer_dashboard_users()
    usuarios = dashboard_users['usuarios']
    for usuario in usuarios:
        usuario_o = Usuario(usuario['nombre'],usuario['email'])
        usuario_o.set_id(usuario['id'])
        list_usuarios.append(usuario_o)
    return list_usuarios