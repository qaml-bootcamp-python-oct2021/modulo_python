from usuarios import Usuario
from tareas import Tarea
import utils , file_handler, estados

tareas = utils.get_tareas_from_file()
usuarios = utils.get_usuarios_from_file()

def menu_option():
    return int(input('''
    1 - Para Crear una Tarea
    2 - Para Buscar una Tarea
    3 - Para Editar estado de una Tarea
    4 - Para Mostrar Tareas
    5 - Para Mostrar Tareas por estado
    6 - Para Asignar una Tarea a un Usuario
    7 - Para Mostrar Tareas asignadas a un Usuario
    8 - Para Dar de alta a un Usuario
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

    print('No existe la Tarea con ese titulo')
    return None

def imprimir_datos_tarea(tarea : Tarea):
    print(tarea.get_info())

def editar_estado_tarea(tarea : Tarea):
    print(f'El estado actual de {tarea.get_titulo()} es: {tarea.get_estado()}')
    opcion = input('Desea modificar el estado? Y/N\n')
    if opcion == 'Y':
        opcion_estado = int(input(f'''
        1 - Para {estados.BACKLOG}
        2 - Para {estados.TODO}
        3 - Para {estados.DOING}
        4 - Para {estados.RESOLVED}
        '''))
        guardar = utils.setear_estado(tarea,opcion_estado)
        
        if guardar:
            actualizar_tarea(tarea)
            actualizar_dashboard()
            print('Estado actualizado satisfactoriamente')

def actualizar_tarea(tarea : Tarea):
    index = 0
    result = False
    while index < len(tareas) and not result:
        tarea_lista :Tarea = tareas[index]
        if tarea.get_titulo() == tarea_lista.get_titulo():
            tareas[index] = tarea
            result = True
        index += 1
    if not result:
        print('No hay una tarea en el listado de Tareas con ese titulo.')

def mostrar_tareas():
    index = 0
    for tarea in tareas:
        if tareas:
            index += 1
            # print('---- Tarea ----')
            # imprimir_datos_tarea(tarea)
            # print()
            print(f'{index} - {tarea.get_info()}')
            

def buscar_tareas_estado():
    opcion_estado = int(input(f''' Ingrese la opcion de estado a buscar
        1 - Para {estados.BACKLOG}
        2 - Para {estados.TODO}
        3 - Para {estados.DOING}
        4 - Para {estados.RESOLVED}
        '''))

    estado = utils.convertir_opcion_estado(opcion_estado)
    if estado is not None:
        for tarea in tareas:
            tarea : Tarea    
            if tarea.get_estado() == estado:
                imprimir_datos_tarea(tarea)
    else:
        print('El estado ingresado es invalido. Intente de nuevo')

def crear_usuario():
    nombre = input('Ingrese nombre de Usuario\n')
    email = input('Ingrese email de Usuario\n')
    usuario = Usuario(nombre, email)
    id_usuario = generar_id_usuario()
    usuario.set_id(id_usuario)
    usuarios.append(usuario)
    actualizar_dashboard_users()

def generar_id_usuario():
    if usuarios:
        ultimo_usuario : Usuario
        ultimo_usuario = usuarios[-1]
        ultimo_id_usuario = ultimo_usuario.get_id()
        return ultimo_id_usuario + 1
    else:
        return 1

def actualizar_dashboard_users():
    dashboard_users = {
        "usuarios" : []
    }
    for usuario in usuarios:
        usuario_dict = utils.convertir_usuario_to_dict(usuario)
        dashboard_users['usuarios'].append(usuario_dict)
    file_handler.guardar_dashboard_users(dashboard_users)

def buscar_usuario():
    nombre = input('Ingrese el nombre del Usuario\n')
    index = 0
    while index < len(usuarios):
        usuario :Usuario = usuarios[index]
        if nombre == usuario.get_nombre():
            return usuario
        index += 1

    print('No existe el Usuario con ese nombre')
    return None

def asignar_tarea_usuario(usuario : Usuario):
    print(f'Seleccione una Tarea para el usuario {usuario.get_nombre}')
    mostrar_tareas()
    opcion = int(input())
    index = opcion - 1
    if 0 <= index < len(tareas):
        tarea : Tarea = tareas[index]
        print(f'La Tarea {tarea.get_titulo()} esta asignada a: {tarea.get_usuario()}')
        opcion = input('Desea modificar la asignacion? Y/N\n')
        if opcion == 'Y':
            tarea_id_usuario = usuario.get_id
            print(f'---------------------->{tarea_id_usuario}')
            tarea.set_usuario(tarea_id_usuario)
            print(tarea)
            actualizar_tarea(tarea)
            actualizar_dashboard()
            print('Estado actualizado satisfactoriamente')
    else:
        print('Opcion invalida, intente de nuevo')

opcion = menu_option()

while opcion != 0 :

    if opcion == 1:
        crear_tarea()
    if opcion == 2:
        tarea = buscar_tarea()
        if tarea is not None:
            imprimir_datos_tarea(tarea)
    if opcion == 3:
        tarea = buscar_tarea()
        if tarea is not None:
            editar_estado_tarea(tarea)
    if opcion == 4:
        mostrar_tareas()
    if opcion == 5:
        buscar_tareas_estado()
    if opcion == 6:
        usuario = buscar_usuario()
        if usuario is not None:
            asignar_tarea_usuario(usuario)
    if opcion == 7:
        # buscar_tareas_usuario()
        pass
    if opcion == 8:
        crear_usuario()

    opcion = menu_option()