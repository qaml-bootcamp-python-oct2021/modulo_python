import estados_jugadores
import raza_jugadores

class Jugador:
     def __init__(self, nombre='',email='',puntos='',raza='',estado='') -> None:
        self.__nombre = nombre
        self.__email = email
        self.__puntos = puntos
        self.__raza = raza  
        self.__estado = estado