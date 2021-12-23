# This will be the main page to start the games

from games import Game
from blackjack import BlackJack

def call_game(id):
    games_list = {
        '1': BlackJack()
    }
    return games_list.get(id)

game = Game()
game_type = game.choose_game()
game_obj = call_game(game_type)

game_obj.start_game()
