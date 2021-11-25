import os , json

TORNEO_FILE = 'torneo.json'

torneo = {
    "jugadores" : []
}

def file_existe():
    if not os.path.exists(TORNEO_FILE):
        with open(TORNEO_FILE,'w') as file:
            json.dump(torneo,file)

def leer_file():
    file_existe()
    with open(TORNEO_FILE,'r') as file:
        data = json.load(file)
    return data


def guardar_torneo(jugador):
    with open(TORNEO_FILE,'w') as file:
        json.dump(torneo,file)