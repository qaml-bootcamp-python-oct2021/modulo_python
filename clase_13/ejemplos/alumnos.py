class Alumno():

    __curso = 'Python'

    def __init__(self,nombre='',apellido='',email='') -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email


    def get_info(self):
        return f'Nombre: {self.__nombre} - Apellido: {self.__apellido} - Email: {self.__email} - Curso: {self.__curso}'

    def set_nombre(self,nombre):
        self.__nombre = nombre

    def set_apellido(self,apellido):
        self.__apellido = apellido

    def set_email(self,email):
        self.__email = email

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_email(self):
        return self.__email

    def get_curso(self):
        return self.__curso