import os
from player_race import PlayerRace
from player_status import PlayerStatus
from player import Player
from game import Game
import constants
import messages
import json

from game_status import GameStatus


def get_race_option():
    race_option = 'Select race, Insert:\n'
    for race in PlayerRace:
        race_option += f'{race.get_info()} \n'
    return race_option


def validate_race_option(option):
    try:
        return PlayerRace(int(option))
    except ValueError:
        print(messages.ERROR_RACE_NO_FOUND)
        return None

def validate_create_game(games, new_game):
    index = 0
    while index < len(games):
        if games[index].get_name() == new_game:
            return False
        index += 1
    return True


def validate_winner_game(player_key):
    isValidate = player_key == constants.PLAYER_KEY_1 or player_key == constants.PLAYER_KEY_2
    if not isValidate:
        print(messages.ERROR_PLAYER_NO_FOUND)
       
    return isValidate


def validate_end_tornament(games):
    index = 0
    while index < len(games):
        if games[index].get_status() != GameStatus.DONE.value:
            return False
        index += 1
    return len(games) > 0


def get_key_loser_game(winner_key):
    if winner_key == constants.PLAYER_KEY_1:
        return constants.PLAYER_KEY_2
    else:
        return constants.PLAYER_KEY_1


def get_winner_tournament(players):
    winner: Player = None
    for player in players:
        player: Player
        if winner is None or player.get_score() > winner.get_score():
            winner = player
    return winner


def convert_game_to_dic(game: Game):
    players_dic = game.get_players()
    players_dic[constants.PLAYER_KEY_1] = convert_player_to_dic(
        players_dic.get(constants.PLAYER_KEY_1))
    players_dic[constants.PLAYER_KEY_2] = convert_player_to_dic(
        players_dic.get(constants.PLAYER_KEY_2))
    return {
        "name": game.get_name(),
        "players": players_dic,
        "winner_key": game.get_winner_key(),
        "status": game.get_status(),
    }


def convert_player_to_dic(player: Player):
    return {
        "name": player.get_name(),
        "email": player.get_email(),
        "race": player.get_race(),
        "score": player.get_score(),
        "status": player.get_status(),
    }


def export_result_to_file(dic_games, dic_players):
    create_dir_files()
    with open(constants.GAME_FILE, 'w') as file:
        json.dump(dic_games, file)

    with open(constants.PLAYER_FILE, 'w') as file:
        json.dump(dic_players, file)

def create_dir_files():
    if not os.path.exists(constants.DIR_FILES):
        os.makedirs(constants.DIR_FILES)

