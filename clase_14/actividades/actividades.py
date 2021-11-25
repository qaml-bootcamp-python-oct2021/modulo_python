from tareas import Tarea
import utils
from utils import get_actividades_from_file
import file_handler

actividades = utils.get_actividades_from_file()

def menu_option():
    return int(input('''
    1 - Crear una tarea
    2 - Dar de alta un usuario
    3 - Buscar una tarea
    4 - Mostrar todas las tareas
    5 - Mostrar tareas por estado
    6 - Mostrar tareas por usuario
    0 - Para salir
    '''))

def crear_tarea():
    titulo = input('Ingrese el titulo de la tarea\n')
    descripcion = input('Ingrese la descripción de la tarea\n')
    prioridad = input('¿Qué prioridad tiene la tarea?\n')
    usuario = input('¿Quién hará la tarea?\n')
    tarea = Tarea(titulo,descripcion,prioridad,usuario)
    actividades.append(tarea)
    actualizar_actividades()


def actualizar_actividades():
    actividades = {
        "tareas" : []
    }
    for actividad in actividades:
        actividades_dict = utils.convertir_actividad_to_dict(actividad)
        actividades['tareas'].append(actividades_dict)
    file_handler.guardar_actividades(actividades)

def run_project():

    opcion = menu_option()

    while opcion != 0 :
        if opcion == 1:
            crear_tarea()
      

        opcion = menu_option()

run_project()