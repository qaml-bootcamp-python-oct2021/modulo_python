class Tarea:
    
    def __init__(self, titulo, descripcion, prioridad, usuario) -> None:
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__usuario = usuario
        pass

    def get_usuario(self):
        return self.__usuario

    def get_info(self):
        return f'titulo: {self.__titulo} Descripcion: {self.__descripcion} Prioridad: {self.__prioridad}'