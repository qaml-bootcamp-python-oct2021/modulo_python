
class Usuario:

    def __init__(self, nombre, email) -> None:
        self.__nombre = nombre
        self.__email = email
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def get_info(self):
        return f'Nombre: {self.__nombre}\nEmail: {self.__email}'