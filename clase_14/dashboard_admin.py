from tareas import Tarea
import utils , file_handler, estados

tareas = utils.get_tareas_from_file()

def menu_option():
    return int(input('''
    1 - Para Crear una Tarea
    2 - Para Buscar una Tarea
    3 - Para Editar estado de una Tarea
    4 - Para Mostrar Tareas
    5 - Para Mostrar Tareas por estado
    6 - Para Mostrar Tareas asignadas a un Usuario
    7 - Para Dar de alta a un Usuario
    0 - Para salir
    '''))

def crear_tarea():
    titulo = input('Ingrese un titulo para la Tarea\n')
    descripcion = input('Ingrese una descripcion para la Tarea\n')
    prioridad = input('Ingrese una prioridad para la Tarea\n')
    tarea = Tarea(titulo, descripcion, prioridad)
    tareas.append(tarea)
    actualizar_dashboard()

def actualizar_dashboard():
    dashboard = {
        "tareas" : []
    }
    for tarea in tareas:
        tarea_dict = utils.convertir_tarea_to_dict(tarea)
        dashboard['tareas'].append(tarea_dict)
    file_handler.guardar_dashboard(dashboard)

def buscar_tarea():
    titulo = input('Ingrese el titulo de la Tarea\n')
    index = 0
    while index < len(tareas):
        tarea :Tarea = tareas[index]
        if titulo == tarea.get_titulo():
            return tarea
        index += 1

    print('No existe un Alumno con ese nombre')
    return None

def imprimir_datos_tarea(tarea : Tarea):
    print(tarea.get_info())

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        crear_tarea()
    if opcion == 2:
        tarea = buscar_tarea()
        if tarea is not None:
            imprimir_datos_tarea(tarea)
    if opcion == 3:
        # tarea = buscar_tarea()
        # if tarea is not None:
        #     editar_estado_tarea(tarea)
        pass
    if opcion == 4:
        # mostrar_tareas()
        pass
    if opcion == 5:
        # buscar_tareas_estado()
        pass
    if opcion == 6:
        # buscar_tareas_usuario()
        pass
    if opcion == 7:
        # crear_usuario()
        pass

    opcion = menu_option()