from jugador import Jugador
import estados_partida

class Partida:
    def __init__(self, id=0, nombre='', jugador_a=None, jugador_b=None) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__jugador_a : Jugador = jugador_a
        self.__jugador_b : Jugador = jugador_b
        self.__ganador : Jugador = None
        self.__perdedor : Jugador = None
        self.__estado = estados_partida.ACTIVA
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre

    def get_jugador_a(self):
        return self.__jugador_a

    def get_jugador_b(self):
        return self.__jugador_b

    def get_ganador(self):
        try:
            return self.__ganador
        except AttributeError:
            return 'No definido'

    def set_ganador(self, jugador):
        self.__ganador = jugador

    def get_perdedor(self):
        try:
            return self.__perdedor
        except AttributeError:
            return 'No definido'

    def set_perdedor(self, jugador):
        self.__perdedor = jugador

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_info(self):
        try:
            return f'ID: {self.__id} - Partida: {self.__nombre} - Jugador A: {self.__jugador_a.get_nickname()} - Jugador B: {self.__jugador_b.get_nickname()} - Estado: {self.__estado} - Ganador: {self.__ganador.get_nickname()} - Perdedor: {self.__perdedor.get_nickname()}'
        except AttributeError:
            return f'ID: {self.__id} - Partida: {self.__nombre} - Jugador A: {self.__jugador_a.get_nickname()} - Jugador B: {self.__jugador_b.get_nickname()} - Estado: {self.__estado} - Ganador: {self.__ganador} - Perdedor: {self.__perdedor}'