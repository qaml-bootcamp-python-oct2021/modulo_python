
from utils import get_tareas_from_file, get_usuarios_from_file
from usuario import Usuario
from tareas import Tareas
import utils, file_handler,estados

usuarios_list = utils.get_usuarios_from_file()
tareas_list = utils.get_tareas_from_file()

def crear_tarea():
    t_usuario = buscar_usuario()
    if t_usuario is not None:
        t_titulo= input('Ingrese titulo de la tarea: ')
        t_descripcion = input('Ingrese uan descripcion para la tarea: ')
        t_prioridad = input('Ingrese la prioridad de la tarea: ')
        tarea = Tareas(t_titulo,t_descripcion,t_prioridad)
        tarea.set_usuario(t_usuario)
        tareas_list.append(tarea)
        actualizar_tarea()

def buscar_tarea():
    titulo_tarea = input('Ingrese el titulo de la tarea a buscar: ')
    indice = 0
    result = False
    while indice < len(tareas_list) and not result:
        tarea : Tareas = tareas_list[indice]
        if titulo_tarea == tarea.get_titulo():
            return tarea
        indice +=1
    if not result:
        print('No existe una Tarea con ese titulo')
    return None   

def crear_usuario():
    u_nombre = input('Ingrese el nombre del usuario: ')
    u_email = input('Ingrese el email del usuario: ')
    usuario = Usuario(u_nombre,u_email)
    usuarios_list.append(usuario)
    actualizar_usuario()
    return usuario

def buscar_usuario():
    nombre = input ('Ingrese el nombre del usuario: ')
    indice = 0
    result = False
    while indice < len(usuarios_list) and not result:
        usuario : Usuario = usuarios_list[indice]
        if nombre == usuario.get_nombre():
            return usuario
        indice +=1
    if not result:
        opcion = input('No existe ningun usuario con ese nombre registrado ¿Quiere dar de alta al usuario? Y/N: ' ) 
        if opcion == 'Y':
            usuario = crear_usuario()
            return usuario
     
def actualizar_tarea():
    tareas = {'tarea' : []}
    for tarea in tareas_list:
        tarea_dicc = utils.convertir_tarea_a_dicc(tarea)
        tareas['tarea'].append(tarea_dicc)
    file_handler.guardar_tarea_file(tareas)

def actualizar_usuario():
    usuarios ={'usuario' : []}
    for usuario in usuarios_list:
        usuario_dicc = utils.convertir_usuario_a_dicc(usuario)
        usuarios['usuario'].append(usuario_dicc)
    file_handler.guardar_usuario_file(usuarios)

def imprimir_datos_tarea(tarea : Tareas):
    print(tarea.get_info())

def editar_estado_tarea(tarea : Tareas):
    print(f'El estado actual de {tarea.get_titulo()} es: {tarea.get_estado()}')
    opcion = input('Desea modificar el estado? Y/N\n')
    if opcion == 'Y':
        opcion_estado = int(input(f'''
        1 - Para {estados.BACKLOG}
        2 - Para {estados.TODO}
        3 - Para {estados.DOING}
        4 - Para {estados.RESOLVED}
        '''))
        guardar = utils.setear_estado(tarea, opcion_estado)
        
        if guardar:
            actualizar_dato_tarea(tarea)
            actualizar_tarea()
            print('Estado actualizado satisfactoriamente')

def actualizar_dato_tarea(tarea : Tareas):
    index = 0
    result = False
    while index < len(tareas_list) and not result:
        tareas : Tareas = tareas_list[index]
        if tarea.get_titulo() == tareas.get_titulo():
            tareas_list[index] = tarea
            result = True
        index += 1
    if not result:
        print('No hay una tarea en el listado de Tareas con ese titulo.')

def mostrar_tareas():
    for tarea in tareas_list:
        print(tarea.get_info())
    if(len(tareas_list)==0):
        print('No hay Tareas registradas')

def mostrar_tareas_usuario():
    usuario = buscar_usuario()
    if usuario is not None:
        result = False
        indice = 0
        while indice< len(tareas_list):
            tarea :Tareas = tareas_list[indice]
            if tarea.get_usuario().get_nombre() == usuario.get_nombre():
                print(tarea.get_info())
                result = True
            indice+=1
        if not result:
            print(f'No existen tareas asignadas al usuario {usuario.get_nombre()}')

def mostrar_tareas_estado():
    opcion_estado = int(input(f''' Ingrese la opcion de estado a buscar
        1 - Para {estados.BACKLOG}
        2 - Para {estados.TODO}
        3 - Para {estados.DOING}
        4 - Para {estados.RESOLVED}
        '''))
    estado = utils.convertir_opcion_estado(opcion_estado)
    if estado is not None:
        for tarea in tareas_list:
            tarea : Tareas    
            if tarea.get_estado() == estado:
                imprimir_datos_tarea(tarea)
    else:
        print('El estado ingresado es invalido. Intente de nuevo')

def menu_opciones():
    return int(input('''
    1 - Para crear un Usuario
    2 - Para crear una Tarea
    3 - Para buscar una Tarea
    4 - Para cambiar estado a una Tarea
    5 - Para mostrar todas las Tareas
    6 - Para mostrar las tareas de un usuario
    7 - Para mostrar las tareas por estado
    0 - Para salir
    '''))


opcion = menu_opciones()

while opcion != 0 :

    if opcion == 1:
        crear_usuario()
    if opcion == 2:
        crear_tarea()
    if opcion == 3:
       tarea = buscar_tarea()
       if tarea is not None:
            imprimir_datos_tarea(tarea)
    if opcion == 4:
        tarea = buscar_tarea()
        if tarea is not None:
            editar_estado_tarea(tarea)
    if opcion == 5:
        mostrar_tareas()
    if opcion == 6:
        mostrar_tareas_usuario()
    if opcion == 7:
        mostrar_tareas_estado()

    opcion = menu_opciones()
