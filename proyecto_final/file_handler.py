import os

PARTIDAS_FILE = './proyecto_final/partidas.txt'
JUGADORES_FILE = './proyecto_final/jugadores.txt'

def exportar_info_partidas(partidas):
    file = open(PARTIDAS_FILE, 'w')
    file.write('Partidas del Torneo de Starcraft 2\n')
    file.close()

    file = open(PARTIDAS_FILE, 'a')
    for partida in partidas:
        file.write(f'ID: {partida.get_id()}\n')
        file.write(f'Nombre: {partida.get_nombre()}\n')
        file.write(f'Estado: {partida.get_estado()}\n')
        try:
            file.write(f'Ganador: {partida.get_ganador().get_nickname()}\n')
            file.write(f'Perdedor: {partida.get_perdedor().get_nickname()}\n')
        except AttributeError:
            file.write('Ganador: No definido\n')
            file.write('Perdedor: No definido\n')
        file.write('---------------------------------------------\n')
    file.close()

def exportar_info_jugadores(jugadores):
    file = open(JUGADORES_FILE, 'w')
    file.write('Jugadores del Torneo de Starcraft 2\n')
    file.close()

    file = open(JUGADORES_FILE, 'a')
    for jugador in jugadores:
        file.write(f'ID: {jugador.get_id()}\n')
        file.write(f'Nickname: {jugador.get_nickname()}\n')
        file.write(f'Email: {jugador.get_email()}\n')
        file.write(f'Raza: {jugador.get_raza()}\n')
        file.write(f'Estado: {jugador.get_estado()}\n')
        file.write(f'Puntos: {jugador.get_puntos()}\n')
        file.write('---------------------------------------------\n')
    file.close()
