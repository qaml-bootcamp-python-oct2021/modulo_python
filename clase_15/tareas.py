import estados
from usuario import Usuario


class Tareas:

    def __init__(self,titulo,descripcion,prioridad) -> None:
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__estado = estados.BACKLOG
        self.__usuario : Usuario = None
        
    
    def get_titulo(self):
        return self.__titulo
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_prioridad(self):
        return self.__prioridad
   
    def get_usuario(self):
        return self.__usuario
    
    def get_estado(self):
        return self.__estado
    
    def set_estado(self,estado):
        self.__estado = estado
    
    def set_usuario(self,usuario):
        self.__usuario = usuario

    def get_info(self):
        return f'''\nTitulo: {self.__titulo}\nDescripción: {self.__descripcion}\nPrioridad: {self.__prioridad}\nEstado: {self.__estado}\nUsuario asignado: {self.__usuario.get_nombre()}'''