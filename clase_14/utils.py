from tareas import Tarea
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