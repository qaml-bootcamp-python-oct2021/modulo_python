from estado_enum import Estado


class Alumno:
    def __init__(self, nombre='',apellido='',email='') -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__estado = Estado.ACTIVO.name

    def get_info(self):
        return f'Nombre: {self.__nombre}, Apellido: {self.__apellido}, Email:{self.__email}, Estado:{self.__estado}'
    
    def set_estado(self,estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email