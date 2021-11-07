class Alumno():

    curso = 'Python'

    def __init__(self, nombre = '', apellido = '', email = '') -> None:
        self.__nombre =  nombre
        self.apellido = apellido
        self.email = email
        self.__curso = 'Python'

    def get_info(self):
        return f'Nombre: {self.__nombre} - Apellido: {self.apellido} - Email: {self.email} - Curso: {self.__curso}'

    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.apellido = apellido
    def set_email(self, email):
        self.email = email