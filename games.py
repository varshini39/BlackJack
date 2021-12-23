# This class will be common for all games

class Game:
    """
    A class representing a game's basic standards
    """
    GAME_LIST = {'1': 'Blackjack'}

    def __init__(self):
        print(("*" * 40) + "Welcome to the GAME portal" + ("*" * 40))

    def display_rules(self):
        '''
        This function is used to display the welcome message to the game.
        '''
        print(("*" * 40) + " GAME TIME " + ("*" * 40))
    
    def choose_game(self):
        '''
        This function is used when the user wants to play one game from a group of games
        '''
        game_name = 0
        while True:
            print("Choose a game from the following")
            for num, name in self.GAME_LIST.items():
                print("{}. {}".format(num, name))
            game_name = input("Enter the game option: ")
            if game_name not in self.GAME_LIST.keys():
                print("Please enter the valid option!")
            else:
                break
        self.game_type = game_name
        return self.game_type
    
    def check_player_ready(self):
        '''
        This function is used to check if the player is ready for the game
        '''
        player_status = input("Are you ready? Give 'Y' to start or any other key to quit the game: ")
        if player_status.casefold() != 'y':
            print("Thank you!")
            self.players_ready = False
        else:
            self.players_ready = True

    def set_players_count(self):
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
        self.num_players = num_players
    
    def add_players_details(self):
        '''
        This function is used to get players details (name and the bet)
        '''
        players_details = {}
        for i in range(self.num_players):
            name = input("Enter the name of player "+i+": ")
            bet = int(input("Enter the bet of player "+i+": "))
            players_details[name] = {'bet': bet, 'points': 0}
        self.players_details = players_details

    def get_players_count(self):
        return self.num_players
    
    def get_players_details(self):
        return self.players_details
    
    def set_players_points(self, name, game_points):
        player_dict = self.players_details[name]
        player_dict.update(points = game_points)

    def get_details_for_game(self):
        '''
        This function is used to fetch all necessary details to start the game
        '''
        self.check_player_ready()
        
        self.set_players_count()
        self.add_players_details()

    def start_game(self):
        '''
        This class will be overwritten to start the game
        '''
        print("Game starts now!")
