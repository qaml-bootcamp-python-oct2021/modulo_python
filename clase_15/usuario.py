class Usuario:

    def __init__(self, nombre, email) -> None:
        self.__nombre = nombre
        self.__email = email
        pass

    def get_nombre(self):
        return self.__nombre