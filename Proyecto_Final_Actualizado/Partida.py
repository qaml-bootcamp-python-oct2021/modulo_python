import estado_partidas

class Partida:
    def __init__(self, nombre_partida='', jugadores=[]) -> None:
        self.__nombre_partida = nombre_partida
        self._jugadores = jugadores
        self.__estado = estado_partidas.ACTIVAS
    def get_nombre_partida(self):
        return self.__nombre_partida
    def get_jugadores(self):
        return self._jugadores
    
    def set_estado(self, estado):
        self.__estado = estado
    def get_estado(self):
        return self.__estado
    def get_info_partida(self):
        return f'''
           Nombre Partida: {self.__nombre_partida}
           Jugador A:   {self.get_jugadores().get(1).get_info_jugador_dict()} 
           Jugador B:   {self.get_jugadores().get(2).get_info_jugador_dict()}
           Estado: {self.__estado}
        '''
    def get_info_dict(self):
        return {
           "Nombre Partida": self.__nombre_partida,
           "Jugadores": { '1': self.get_jugadores().get(1), #.get_info_jugador_dict(), 
                          '2': self.get_jugadores().get(2) #.get_info_jugador_dict(),
                        },
           "Estado": self.__estado
        }

