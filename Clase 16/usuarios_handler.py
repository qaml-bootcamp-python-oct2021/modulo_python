import os , json

USUARIOS_FILE = './clase 16/usuarios.json'

usuarios = {
    "usuario" : []
}
    
def usuarios_existe():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE,'w') as file:
            json.dump(usuarios,file)

def leer_usuarios():
    usuarios_existe()
    with open(USUARIOS_FILE,'r') as file:
        data = json.load(file)
    return data

def guardar_usurios(tareas):
    with open(USUARIOS_FILE,'w') as file:
        json.dump(usuarios,file)