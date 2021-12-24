# This will be the main page to start the games

from games import Game
from blackjack import BlackJack

def call_game(id, player_details):
    games_list = {
        '1': BlackJack(player_details)
    }
    return games_list.get(id)

game = Game()
game.get_details_for_game()
game_type = game.choose_game()

player_details = game.get_players_details()
game_obj = call_game(game_type, player_details)

game_obj.start_game()
