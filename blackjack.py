# This program is a basic version of blackjack game
# It will be played with 2 players (users) and a dealer (computer). We will use a set of 52 cards.

class Game:
    """
    A class representing a game's basic standards
    """

    def display_rules(self):
        '''
        This function is used to display the welcome message to the game.
        '''
        print(("*" * 40) + " GAME TIME " + ("*" * 40))
    
    def check_player_ready(self):
        '''
        This function is used to check if the player is ready for the game
        '''
        player_status = input("Are you ready? Give 'Y' to start or any other key to quit the game: ")
        if player_status.casefold() != 'y':
            print("Thank you!")
            return False
        return True

    def get_players_count(self):
        '''
        This function is used to get the number of players count
        '''
        num_players = 0
        while True:
            num_players = input("Enter the number of players [1/2]: ")
            if num_players != '1' and num_players != '2':
                print("Please enter the valid number 1 or 2")
            else:
                break
        return num_players
    
    def get_players_details(self, players_count):
        '''
        This function is used to get players details (name and the bet)
        '''
        players_details = {}
        
        return players_details


    def start_game(self):
        '''
        This function is used to start the game
        '''
        self.display_rules()

        if not self.check_player_ready():
            return False
        
        num_players = self.get_players_count()
        players_dict = self.get_players_details(players_count=num_players)
        print(players_dict)


class BlackJack(Game):
    """
    A class representing Blackjack game
    """
    CARD_VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 11}
    SYMBOLS = ["\u2764", "\u2660", "\u25C6", "\u2663"]

    def display_rules(self):
        '''
        This function is used to display the welcome message and the rules of the game.
        '''
        super().display_rules()
        print(("*" * 25) + " Welcome to the BlackJack Game " + ("*" * 25))
        print("Rules:")
        print("\u2022Maximum of 2 players can participate.")
        print("\u2022Place your bets first.")
        print("\u2022You can 'Hit' or 'Stand' depending upon your cards.")
        print("\u2022If your card total is above 21, you are busted.")
        print("\u2022If you reach 21 in 2 cards itself, you will get one and a half times your bet.")
        print("*" * 81)
        print()


