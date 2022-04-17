import os, json

JUGADORES_FILE = 'jugadores.json'
PARTIDAS_FILE = 'partidas.json'

jugador = {
    'jugadores': []
}
partida = {
    'partidas': []
}

def jugador_archivo_existe():
    if not os.path.exists(JUGADORES_FILE):
        with open(JUGADORES_FILE,'w') as file:
            json.dump(jugador,file)

def partida_archivo_existe():
    if not os.path.exists(PARTIDAS_FILE):
       with open(PARTIDAS_FILE,'w') as file:
           json.dump(partida,file)


def leer_archivo_jugadores():
    jugador_archivo_existe()
    with open(JUGADORES_FILE,'r') as file:
        data = json.load(file)
    return data

def leer_archivo_partidas():
    partida_archivo_existe()
    with open(PARTIDAS_FILE,'r') as file:
        data = json.load(file)
    return data


def guardar_jugadores(jugador):
    with open(JUGADORES_FILE,'w') as file:
        json.dump(jugador,file)

def guardar_partidas(jugador):
    with open(PARTIDAS_FILE,'w') as file:
        json.dump(jugador,file)
