import os , json

TAREAS_FILE = './clase 16/tareas.json'

tareas = {
    "tarea" : []
}
    
def tareas_existe():
    if not os.path.exists(TAREAS_FILE):
        with open(TAREAS_FILE,'w') as file:
            json.dump(tareas,file)

def leer_tareas():
    tareas_existe()
    with open(TAREAS_FILE,'r') as file:
        data = json.load(file)
    return data

def guardar_tareas(tareas):
    with open(TAREAS_FILE,'w') as file:
        json.dump(tareas,file)
