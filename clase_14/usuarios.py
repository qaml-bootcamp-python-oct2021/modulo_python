class Usuario:
    def __init__(self, nombre='', email='') -> None:
        self.__id = 0
        self.__nombre = nombre
        self.__email = email

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_info(self):
        return f'Usuario: {self.__nombre} - email: {self.__email}'