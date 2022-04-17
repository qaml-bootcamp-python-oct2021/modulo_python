import opcion_raza
import estado_jugador

class Jugador: 
    def __init__(self, nombre='', email='', raza='', puntos_ganados = 0) -> None:
        self.__nombre = nombre
        self.__email = email
        self.__raza = opcion_raza.opcion_raza[raza]
        self.__estado = estado_jugador.ACTIVO
        self.__puntos_ganados = puntos_ganados
    
    def set_estado(self, estado):
        self.__estado = estado
    def get_estado(self):
        return self.__estado
    
    def get_email(self):
        return self.__email

    def get_nombre_jugador(self):
        return self.__nombre
    def get_raza(self):
        return self.__raza
    
    def get_info_jugador(self):
        return f'''
           Nombre: {self.__nombre}
           Email:  {self.__email}
           Raza:   {self.__raza}
           Estado: {self.__estado}
           Puntos Ganados: {self.__puntos_ganados}
        '''
    def get_info_jugador_dict(self):
        return {
           "Nombre": self.__nombre,
           "Email":  self.__email,
           "Raza":   self.__raza,
           "Estado": self.__estado,
           "Puntos Ganados": self.__puntos_ganados
        }
    def get_info_basica_jugador(self):
         return f'''
           Nombre: {self.__nombre}
           Raza:   {self.__raza}
           Estado: {self.__estado}
        '''
    def dar_puntaje(self, puntos):
        self.__puntos_ganados += puntos
        return self.__puntos_ganados
    def get_puntaje(self):
        return self.__puntos_ganados
    def set_puntaje(self, puntos):
        self.__puntos_ganados = puntos