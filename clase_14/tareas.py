import estados

class Tarea:

    def __init__(self, titulo='', descripcion='', prioridad='') -> None:
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__estado = estados.BACKLOG
        self.__usuario = 0

    def set_estado(self,estado):
        self.__estado = estado

    def get_estado(self):
        return self.__estado

    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_info(self):
        return f'Titulo: {self.__titulo} - Descripcion: {self.__descripcion} - Prioridad: {self.__prioridad} - Estado: {self.__estado} - Usuario: {self.__usuario}'