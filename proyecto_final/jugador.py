import estados_jugador

class Jugador:
    def __init__(self, id=0, nickname='', email='', raza='') -> None:
        self.__id = id
        self.__nickname = nickname
        self.__email = email
        self.__raza = raza
        self.__estado = estados_jugador.NO_JUGANDO
        self.__puntos = 0

    def get_id(self):
        return self.__id

    def get_nickname(self):
        return self.__nickname

    def get_email(self):
        return self.__email

    def get_raza(self):
        return self.__raza

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_puntos(self):
        return self.__puntos

    def set_puntos(self, puntos):
        self.__puntos += puntos

    def get_info(self):
        return f'ID: {self.__id} - Nickname: {self.__nickname} - Raza: {self.__raza} - Estado: {self.__estado} - Puntos: {self.__puntos}'