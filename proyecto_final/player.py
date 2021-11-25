from player_status import PlayerStatus


class Player:
    def __init__(self, name, email, race) -> None:
        self.__name = name
        self.__email = email
        self.__race = race.name
        self.__score = 0
        self.__status = PlayerStatus.NEW.value

    def get_info(self):
        return f'''
            Player: {self.__name}
            Email: {self.__email}
            Race: {self.__race}
            Score: {self.__score}
            status: {self.__status}
                '''

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_race(self):
        return self.__race

    def get_score(self):
        return self.__score

    def get_status(self):
        return self.__status

    def set_status(self, status: PlayerStatus):
        self.__status = status.value

    def add_score(self, score):
        self.__score += score
