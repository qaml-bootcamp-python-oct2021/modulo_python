import os
import json

TAREAS_FILE='./clase_14/ejercicio_01_tareas/tareas.json'
USUARIOS_FILE='./clase_14/ejercicio_01_tareas/usuarios.json'

def usuario_existe():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE,'w') as file:
            json.dump({ "usuarios" : []},file)

def tarea_existe():
    if not os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE,'w') as file:
            json.dump({ "tareas" : []},file)

def leer_datos(dir_archivo):
    if(dir_archivo == USUARIOS_FILE):
        usuario_existe()
    else:
       tarea_existe() 
    with open(dir_archivo,'r') as file:
        data = json.load(file)
    return data 

def guardar_datos(diccionario_datos, dir_archivo):
    with open(dir_archivo,'w') as file:
        json.dump(diccionario_datos,file)

