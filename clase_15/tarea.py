class Tarea:

    def __init__(self,titulo, descripcion, prioridad) -> None:
        self.__titulo  = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad


    def get_info(self):
        return f'''
        Titulo: {self.__titulo} 
        Descripcion: {self.__descripcion}
        Prioridad: {self.__prioridad}
        '''