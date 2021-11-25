

from game_status import GameStatus
from player import Player
import constants


class Game:

    def __init__(self, name, player_a, player_b, winner_key='') -> None:
        self.__name = name
        self.__players = {constants.PLAYER_KEY_1: player_a,
                          constants.PLAYER_KEY_2: player_b}
        self.__winner_key = winner_key
        self.__status = GameStatus.ACTIVE.value

    def get_info(self):
        return f'''
            Game: {self.__name}
            Player 1: {self.__players.get(constants.PLAYER_KEY_1).get_name()}
            Player 2: {self.__players.get(constants.PLAYER_KEY_2).get_name()}
            Winner: {'' if self.__winner_key == '' else self.__players.get(self.__winner_key).get_name()}
            status: {self.__status}
            '''

    def get_name(self):
        return self.__name

    def get_players(self):
        return self.__players

    def get_players_info(self):
        return f'''
             {constants.PLAYER_KEY_1} : {self.__players.get(constants.PLAYER_KEY_1).get_name()}
             {constants.PLAYER_KEY_2} : {self.__players.get(constants.PLAYER_KEY_2).get_name()}
            '''

    def get_winner_key(self):
        return self.__winner_key

    def get_status(self):
        return self.__status

    def set_status(self, status: GameStatus):
        self.__status = status.value

    def set_winner_key(self, winner_key):
        self.__winner_key = winner_key
