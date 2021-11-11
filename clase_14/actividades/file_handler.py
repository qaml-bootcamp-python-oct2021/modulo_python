import os , json

ACTIVIDADES_FILE = 'actividades.json'

actividades = {
    "tareas" : []
}

def actividades_existe():
    if not os.path.exists(ACTIVIDADES_FILE):
        with open(ACTIVIDADES_FILE,'w') as file:
            json.dump(actividades,file)

def leer_actividades():
    actividades_existe()
    with open(ACTIVIDADES_FILE,'r') as file:
        data = json.load(file)
    return data


def guardar_actividades(actividad):
    with open(ACTIVIDADES_FILE,'w') as file:
        json.dump(actividad,file)