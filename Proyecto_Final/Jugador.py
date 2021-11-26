import Estados_Jugador
import Raza

class Jugador:
    def __init__(self, nombre="", email = "", puntos_ganados=0, estado="", raza="") -> None:
        self.__nombre = nombre
        self.__email = email
        self.__puntos_ganados = puntos_ganados
        self.__estado = Estados_Jugador.NUEVO
        self.__raza = Raza.raza_option.get(raza)

    
    
    def get_estado(self):
        return self.__estado
    def set_estado(self, estado):
        self.__estado = estado
    
    def get_raza(self):
        return self.__raza
    def set_raza(self, raza):
        self.__raza = raza
    
    def get_nombre(self):
        return self.__nombre
    def get_email(self):
        return self.__email
   
    def get_info(self):
        return f'''
           Nombre: {self.__nombre} - 
           Email: {self.__email} - 
           Puntos Ganados: {self.__puntos_ganados} - 
           Raza: {self.__raza} - 
           Estado: {self.__estado}'''


    def get_puntos_ganados(self):
        return self.__puntos_ganados
    def adicionar_puntaje(self, puntaje_jugador_partida):
        self.__puntos_ganados += puntaje_jugador_partida