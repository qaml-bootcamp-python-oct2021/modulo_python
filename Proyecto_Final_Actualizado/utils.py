import file_handler
from Jugador import Jugador
from Partida import Partida
import  opcion_raza

def obtener_jugadores_desde_archivo():
    lista_jugadores = []
    jugadores = file_handler.leer_archivo_jugadores()
    jugadores = jugadores['jugadores']
    for jugador in jugadores:
        raza = jugador['raza']
        opciones_raza = opcion_raza.opcion_raza
        opcion_seleccionada = list(opciones_raza.keys())[list(opciones_raza.values()).index(raza)]
        jugador_objeto = Jugador(jugador['nombre'],jugador['email'], opcion_seleccionada)
        jugador_objeto.set_estado(jugador['estado'])
        lista_jugadores.append(jugador_objeto)
    return lista_jugadores

def obtener_partidas_desde_archivo():
    lista_partidas = []
    partidas = file_handler.leer_archivo_partidas()
    partidas = partidas['partidas']
    
    jugadores_enviar = {
      1: '',
      2: ''
    }
    
    for partida in partidas:
        #print('Jug ', partida['jugadores'])
        #partida_objeto = Partida(partida['nombre'],partida['jugadores'])
        jugadores = partida['jugadores']
        index = 1
        jugadores_enviar = {
            1: '',
            2: ''
        }
    
        for jugador in jugadores:
            #print(jugadores[jugador])
            raza = jugadores[jugador].get('Raza')

            nombre = jugadores[jugador].get('Nombre')
            email = jugadores[jugador].get('Email')
            puntos_ganados = jugadores[jugador].get('Puntos Ganados')
            estado = jugadores[jugador].get('Estado')
            opciones_raza = opcion_raza.opcion_raza
            opcion_seleccionada = list(opciones_raza.keys())[list(opciones_raza.values()).index(raza)]
            
            jugador: Jugador = Jugador(nombre, email, opcion_seleccionada)
    

            jugador.set_estado(estado)
            jugador.set_puntaje(puntos_ganados)
            jugadores_enviar[index] = jugador
            index+=1

        
        partida_objeto = Partida(partida['nombre'],jugadores_enviar)
        partida_objeto.set_estado(partida['estado'])
        lista_partidas.append(partida_objeto)
    return lista_partidas


def convertir_jugador_a_dict(jugador : Jugador):
    dict_jugador = {
        "nombre": jugador.get_nombre_jugador(),
        "email": jugador.get_email(),
        "raza": jugador.get_raza(),
        "estado": jugador.get_estado(),
        "puntaje": jugador.get_puntaje(), 
    }
    return dict_jugador

def convertir_partida_a_dict(partida : Partida):
    dict_partida = {
        "nombre": partida.get_nombre_partida(),
        "jugadores": { 1: partida.get_jugadores().get(1).get_info_jugador_dict(), 
                       2: partida.get_jugadores().get(2).get_info_jugador_dict(),
                     },
        "estado": partida.get_estado()
    }
    return dict_partida