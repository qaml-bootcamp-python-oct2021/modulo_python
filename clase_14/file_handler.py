import os , json

DASHBOARD_FILE = './clase_14/dashboard.json'
DASHBOARD_USERS_FILE = './clase_14/dashboard_users.json'

dashboard = {
    "tareas" : []
}

dashboard_users = {
    "usuarios" : []
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

def dashboard_users_existe():
    if not os.path.exists(DASHBOARD_USERS_FILE):
        with open(DASHBOARD_USERS_FILE,'w') as file:
            json.dump(dashboard_users,file)

def leer_dashboard_users():
    dashboard_users_existe()
    with open(DASHBOARD_USERS_FILE,'r') as file:
        data = json.load(file)
    return data

def guardar_dashboard_users(dashboard_users):
    with open(DASHBOARD_USERS_FILE,'w') as file:
        json.dump(dashboard_users,file)