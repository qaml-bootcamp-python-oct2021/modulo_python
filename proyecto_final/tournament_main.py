from player import Player
from player_race import PlayerRace
from game import Game
from player_status import PlayerStatus
from game_status import GameStatus
import constants
import messages

import util

players = []
games = []


def create_player(name):
    if name is None:
        name = input(messages.INPUT_NAME)
        if search_player_by_name(name) is not None:
            print(f'Player {name} {messages.INFO_ALREADY_EXIST} ')
            return None
    email = input(messages.INPUT_EMAIL)
    race_id = input(util.get_race_option())
    race_enum = util.validate_race_option(race_id)
    if race_enum is not None:
        new_player = Player(name, email, race_enum)
        players.append(new_player)
        print(messages.SUCCESS_PLAYER_CREATE)
        return new_player


def search_player_by_name(player_name):
    index = 0
    while index < len(players):
        if players[index].get_name() == player_name:
            return players[index]
        index += 1
    return None


def create_or_search_player(player_name):
    player: Player = search_player_by_name(player_name)
    if player is not None:
        if player.get_status() == PlayerStatus.INACTIVE.value or player.get_status() == PlayerStatus.PLAYING.value:
            print(f'Player with status: {player.get_status()}, insert another')
            return None
    else:
        print(messages.INFO_PLAYER_CREATE)
        player = create_player(player_name)
        if player is None:
            print(messages.ERROR_GRAL)

    return player


def ask_for_player(key_player):
    player_game = None
    while player_game == None:
        player_game = create_or_search_player(
            input(f'Insert player {key_player} (create or search):\n'))
    player_game.set_status(PlayerStatus.PLAYING)
    return player_game


def create_game():
    name = input(messages.INPUT_GAME)
    if util.validate_create_game(games, name):
        first_player = ask_for_player(constants.PLAYER_KEY_1)
        second_player = ask_for_player(constants.PLAYER_KEY_2)
        new_game = Game(name, first_player, second_player)
        games.append(new_game)
        print(messages.SUCCESS_GAME_CREATE)
    else:
        print(f'Game {name} {messages.INFO_ALREADY_EXIST}')


def search_game_by_name(game_name):
    index = 0
    while index < len(games):
        game_item: Game = games[index]
        if game_item.get_name() == game_name:
            return game_item
        index += 1
    return None


def finish_game():
    game: Game = search_game_by_name(input(messages.INPUT_GAME))
    if game is None:
        print(messages.ERROR_GAME_NO_FOUND)
    elif game.get_status() == GameStatus.ACTIVE.value:
        if register_players_score(game):
            game.set_status(GameStatus.DONE)
            print(f'{game.get_name()} {messages.SUCCESS_FINISH} ')
    else:
        print(f'{game.get_name()} {messages.INFO_ALREADY_FINISH}')


def register_players_score(game: Game):
    winner_key = input(f'''Select winner (Insert 1 or 2):
            {game.get_players_info()}
             ''')
    if util.validate_winner_game(winner_key):
        winner: Player = game.get_players().get(winner_key)
        loser: Player = game.get_players().get(util.get_key_loser_game(winner_key))
        game.set_winner_key(winner_key)
        winner.add_score(3)
        loser.add_score(1)
        winner.set_status(PlayerStatus.WINNER)
        loser.set_status(PlayerStatus.INACTIVE)
        return True
    return False


def finish_tournament():
    confirm = input(messages.WARNING_TOURNAMENT_FINISH)
    if confirm.upper() == 'Y':
        export_result()
        amount_games = len(games)
        if (amount_games % 2 == 1):
            winner_tournament: Player = util.get_winner_tournament(players)
            print(f'The winner is: {winner_tournament.get_info()}')
        else:
            print(messages.INFO_TOURNAMENT_WINNER)
        return True
    return False


def export_result():
    dicc_games = {'games': []}
    dicc_players = {'players': []}
    for game in games:
        dicc_games['games'].append(util.convert_game_to_dic(game))

    for player in players:
        dicc_players['players'].append(util.convert_player_to_dic(player))

    util.export_result_to_file(dicc_games, dicc_players)


def get_menu():
    try:
        return int(input('''
        ** Select an option **
        1 - Create player
        2 - Create game
        3 - Finish game
        4 - Finish tournament (Export results to files)
        0 - Exit
        '''))
    except ValueError:
        return -1


menu = get_menu()
while menu != 0:
    if menu == 1:
        create_player(None)

    elif menu == 2:
        create_game()

    elif menu == 3:
        finish_game()

    elif menu == 4:
        if util.validate_end_tornament(games):
            if finish_tournament():
                break
        else:
            print(messages.ERROR_TOURNAMENT_FINISH)

    else:
        print(messages.ERROR_MENU_OPTION)
    menu = get_menu()
