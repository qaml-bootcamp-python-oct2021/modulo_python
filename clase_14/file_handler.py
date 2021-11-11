import os , json

DASHBOARD_FILE = './clase_14/dashboard.json'

dashboard = {
    "tareas" : []
}
    
def dashboard_existe():
    if not os.path.exists(DASHBOARD_FILE):
        with open(DASHBOARD_FILE,'w') as file:
            json.dump(dashboard,file)

def leer_dashboard():
    dashboard_existe()
    with open(DASHBOARD_FILE,'r') as file:
        data = json.load(file)
    return data

def guardar_dashboard(dashboard):
    with open(DASHBOARD_FILE,'w') as file:
        json.dump(dashboard,file)

def guardar_tarea(tarea):
    dashboard_data = leer_dashboard()
    dashboard_data['tareas'].append(tarea)
    with open(DASHBOARD_FILE,'w') as file:
        json.dump(dashboard_data,file)

def actualizar_tarea(tarea_existente):
    pass