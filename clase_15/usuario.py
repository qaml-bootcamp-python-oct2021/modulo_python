class Usuario:

    __tareas = []

    def __init__(self, nombre, email) -> None:
        self.__nombre = nombre
        self.__email = email
        pass
    
    def get_nombre(self):
        return self.__nombre

    def set_tarea(self,tarea):
        self.__tareas.append(tarea)

    def get_tareas(self):
        return self.__tareas