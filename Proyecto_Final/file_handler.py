import os , json

JUGADOR_ARCHIVO = 'jugador.json'
PARTIDA_ARCHIVO = 'partida.json'

jugadores = {
    "jugadores" : []
}
partidas = {
    "partidas" : []
}

def exportar_resultado_jugadores(jugadores):
    existe_archivo_jugadores()
    with open(JUGADOR_ARCHIVO, 'w') as file:
        json.dump(jugadores, file)

def exportar_resultado_partidas(partidas):
    existe_archivo_partidas
    with open(PARTIDA_ARCHIVO, 'w') as file:
        json.dump(partidas, file)


def existe_archivo_jugadores():
    if not os.path.exists(JUGADOR_ARCHIVO):
        with open(JUGADOR_ARCHIVO,'w') as file:
            json.dump(jugadores,file)

def existe_archivo_partidas():
  if not os.path.exists(PARTIDA_ARCHIVO):
        with open(PARTIDA_ARCHIVO,'w') as file:
            json.dump(partidas,file)

