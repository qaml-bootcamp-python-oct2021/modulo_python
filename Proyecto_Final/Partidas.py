import Estados_Partidas
class Partida:
    def __init__(self, nombre_partida, jugador_a="", jugador_b="", ganador="Sin Ganador") -> None:
        self.__nombre_partida = nombre_partida
        self.__jugador_a = jugador_a
        self.__jugador_b = jugador_b
        self.__ganador = ganador
        self.__estado_partida = Estados_Partidas.ACTIVAS 


    def get_nombre_partida(self):
        return self.__nombre_partida

    def get_jugadores(self):
        return {
            1: self.__jugador_a,
            2: self.__jugador_b
        }

    def get_estado(self):
        return self.__estado_partida

    def set_estado(self, estado):
        self.__estado_partida = estado

    def get_ganador(self):
        return self.__ganador

    def set_ganador(self, ganador):
        self.__ganador = ganador

    def get_info(self):
        return f'''
            Partida: {self.__nombre_partida}
            Jugador A: {self.__jugador_a}
            Jugador B: {self.__jugador_b}
            Ganador: {'' if self.__ganador == '' else self.__ganador}
            Estado: {self.__status}
            '''

    def get_info_jugadores(self):
          return f'''
             1 : {self.__jugador_a}
             2 : {self.__jugador_b}
            '''
