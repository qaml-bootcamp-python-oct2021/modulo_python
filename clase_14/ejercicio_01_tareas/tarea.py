from usuario import Usuario
from estado_enum import Estado


class Tarea:
    def __init__(self,titulo='',descripcion='', prioridad='', usuario='') -> None:
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__estado = Estado.BACKLOG.name
        self.__usuario : Usuario= usuario

    def set_estado(self,estado):
        self.__estado = estado

    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def get_estado(self):
        return self.__estado 

    def get_usuario(self):
        return self.__usuario

    def get_info(self):
        return f''' 
            Titulo: {self.__titulo},
            Descripción: {self.__descripcion},
            Prioridad: {self.__prioridad},
            Estado: {self.__estado}, 
            Alumno: {self.__usuario.get_nombre()}'''