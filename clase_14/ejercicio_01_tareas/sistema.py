
from estado_enum import Estado
from usuario import Usuario
from tarea import Tarea
import archivo_util
import util

lista_usuarios = []
lista_tareas = []

def crear_usuario():
    nombre = input('Ingrese nombre de Usuario\n')
    email = input('Ingrese email\n')
    usuario = Usuario(nombre,email)
    lista_usuarios.append(usuario)
    guardar_usuarios()
    return usuario

def crear_tarea():
    titulo = input('Ingrese un nombre un titulo\n')
    descripcion = input('Ingrese una descripción\n')
    prioridad = input('Ingrese un prioridad\n')
    usuario = buscar_usuario()
    if usuario is None:
        print('El usuario ingresado no existe, favor de dar de alta')
        usuario = crear_usuario()

    tarea = Tarea(titulo,descripcion,prioridad,usuario)
    lista_tareas.append(tarea)
    guardar_tareas()

def buscar_usuario():
    nombre_usuario = input('Ingrese el nombre del usuario: ')
    indice = 0
    while indice< len(lista_usuarios):
        if lista_usuarios[indice].get_nombre()== nombre_usuario:
           return  lista_usuarios[indice]
        indice+=1
    return None

def buscar_tarea_nombre():
    nombre_tarea = input('Ingrese el nombre de Tarea: ')
    indice = 0
    while indice< len(lista_tareas):
        if lista_tareas[indice].get_titulo()== nombre_tarea:
           return  lista_tareas[indice]
        indice+=1
    return None

def mostrar_tareas_estado():
    estado_id = input(util.get_estado_opcion())
    estado_enum= util.validar_estado_opcion(estado_id)
    if estado_enum != None:
        estado_nombre = estado_enum.name
        indice = 0
        existen_tareas = False
        while indice< len(lista_tareas):
            tarea= lista_tareas[indice]
            if tarea.get_estado()==estado_nombre :
                print(tarea.get_info())
                existen_tareas = True
            indice+=1
        if not existen_tareas:
            print(f'No existen tareas con el estado {estado_nombre}')

def mostrar_tareas_usuario():
    usuario = buscar_usuario()
    if usuario is None:
        print('El usuario ingresado no existe')
    else:
        existen_tareas = False
        indice = 0
        while indice< len(lista_tareas):
            tarea= lista_tareas[indice]
            if tarea.get_usuario().get_nombre() == usuario.get_nombre():
                print(tarea.get_info())
                existen_tareas = True
            indice+=1
        if not existen_tareas:
            print(f'No existen tareas asignadas al usuario {usuario.get_nombre()}')

def editar_estado_tarea(tarea : Tarea):
    print(f'El estado actual de {tarea.get_titulo()} es: {tarea.get_estado()}')
    confirmar_edicion = input('Desea modificar el estado? Y/N : ')
    if confirmar_edicion == 'Y':
        estado_id = (input(util.get_estado_opcion()))
        estado_enum= util.validar_estado_opcion(estado_id)
        if estado_enum!= None:
            tarea.set_estado(estado_enum.name)
            guardar_tareas()

def guardar_usuarios():
    sistema = {
        "usuarios" : []
    }
    for usuario in lista_usuarios:
        usuario: Usuario
        usuario_dicc = util.usuario_to_diccionario(usuario)
        sistema['usuarios'].append(usuario_dicc)
    archivo_util.guardar_datos(sistema,archivo_util.USUARIOS_FILE)

def guardar_tareas():
    sistema = {
        "tareas" : []
    }
    for tarea in lista_tareas:
        tarea: Tarea
        tarea_dicc = util.tarea_to_diccionario(tarea)
        sistema['tareas'].append(tarea_dicc)
    archivo_util.guardar_datos(sistema,archivo_util.TAREAS_FILE)

def mostrar_tareas():
    for tarea in lista_tareas:
        print(tarea.get_info())
    if(len(lista_tareas)==0):
        print('::: No hay registros :::')

def menu_opcion():
    return int(input('''
    1 - Crear usuario
    2 - Crear tarea
    3 - Buscar tarea
    4 - Editar estado tarea
    5 - Mostrar Tareas
    6 - Mostrar Tareas por estado
    7 - Mostrar Tareas por usuario
    0 - Salir
    '''))

opcion = menu_opcion()
lista_usuarios_archivo = archivo_util.leer_datos(archivo_util.USUARIOS_FILE).get('usuarios')
lista_usuarios= util.diccionario_to_usuarios(lista_usuarios_archivo)

lista_tareas_archivo = archivo_util.leer_datos(archivo_util.TAREAS_FILE).get('tareas')
lista_tareas= util.diccionario_to_tareas(lista_tareas_archivo)

while opcion != 0 :
    if opcion == 1:
        print('Creando usuario...')
        crear_usuario()

    if opcion == 2:
        print('Creando tarea...')
        crear_tarea()

    if opcion == 3:
        print('Buscar tarea...')
        tarea_buscar = buscar_tarea_nombre()
        if tarea_buscar != None:
            print(tarea_buscar.get_info())
        else:
            print('Tarea no localizada')

    if opcion == 4:
        print('Editando estado de tarea...')
        tarea_editar = buscar_tarea_nombre()
        if tarea_editar != None:
            editar_estado_tarea(tarea_editar)
        else:
            print('Tarea no localizada')
        
    if opcion == 5:
        print('Mostrar Tareas...')
        mostrar_tareas()
       
    if opcion == 6:
        print('Mostrar Tareas por estado...')
        mostrar_tareas_estado()

    if opcion == 7:
        print('Mostrar Tareas por usuario...')
        mostrar_tareas_usuario()

    opcion = menu_opcion()