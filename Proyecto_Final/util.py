from Partidas import Partida
from Jugador import Jugador


def convertir_partida(partida: Partida):
    return {
        "nombre_partida": partida.get_nombre_partida(),
        "jugador_a":      partida.get_jugadores().get(1),
        "jugador_b":      partida.get_jugadores().get(2),
        "ganador":        partida.get_ganador(),
        "estado_partida": partida.get_estado()
    }

def convertir_jugador(jugador: Jugador):
    return {
        "nombre":         jugador.get_nombre(),
        "email":          jugador.get_email(),
        "raza":           jugador.get_raza(),
        "puntos_ganados": jugador.get_puntos_ganados(),
        "estado":         jugador.get_estado(),
    }

