from tareas import Tarea
import file_handler 


def convertir_actividad_to_dict(tarea : Tarea):
    return  {
        "titulo" : tarea.get_titulo(),
        "descripcion" : tarea.get_descripcion(),
        "prioridad" : tarea.get_prioridad(),
        "estado" : tarea.get_estado()
    }

def get_actividades_from_file():
    list_actividades = []
    actividades = file_handler.leer_actividades()
    tareas = actividades['tareas']
    for tarea in tareas:
        tarea_o = Tarea(tarea['titulo'],tarea['descripcion'],tarea['prioridad'],tarea['estado'])
        list_actividades.append(tarea_o)
    return list_actividades