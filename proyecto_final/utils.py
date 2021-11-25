import file_handler 
from jugadores import Jugador



def get_jugadores_from_file():
    list_jugadores = []
    file_content = file_handler.leer_file()
    jugadores = file_content['jugadores']
    for jugador in jugadores:
        jugador_o = Jugador(jugador['nombre'],jugador['email'],jugador['puntos'],jugador['raza'],jugador['estado'])
        list_jugadores.append(jugador_o)
    return list_jugadores

def convertir_jurador_to_dict(jugador : Jugador):
    dict_jugador = {
        "nombre" : jugador.get_nombre() ,
        "apellido" : jugador.get_email()
    }
    return dict_alumno