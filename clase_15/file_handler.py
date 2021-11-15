import os, json

TAREAS_FILE = './clase_15/tareas.json'
USUARIOS_FILE = './clase_15/usuarios.json'

usuarios = {'usuario' : []}
tareas = {'tarea': []}

def usuarios_file_existe():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, 'w') as file:
            json.dump(usuarios,file)

def tareas_file_existe():
    if not os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE, 'w') as file:
            json.dump(tareas,file)

def leer_usuario_file():
    usuarios_file_existe()
    with open(USUARIOS_FILE,'r') as file:
        data = json.load(file)
    return data

def leer_tareas_file():
    tareas_file_existe()
    with open(TAREAS_FILE,'r') as file:
        data = json.load(file)
    return data

def guardar_usuario_file(usuario_file):
    with open(USUARIOS_FILE,'w') as file:
        json.dump(usuario_file,file)
    
def guardar_tarea_file(tarea_file):
    with open(TAREAS_FILE,'w') as file:
        json.dump(tarea_file,file)



