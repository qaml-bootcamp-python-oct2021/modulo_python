from jugadores import Jugador
from utils import get_jugadores_from_file

jugadores = get_jugadores_from_file()


def crear_jugador():
    nombre = input('Ingrese un nombre de jugador\n')
    email = input('Ingrese email de jugador\n')
    raza = input('Ingrese raza de jugador\n')
    jugador = Jugador(nombre,email,raza)
    jugadores.append(jugador)
    actualizar_torneo()

def actualizar_torneo():
    torneo = {
        "jugadores" : []
    }
    for jugador in jugadores:
        jugador_dict = utils.convertir_alumno_to_dict(alumno)
        agenda['alumnos'].append(alumno_dict)
    file_handler.guardar_agenda(agenda)