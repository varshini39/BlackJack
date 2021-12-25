# This class represents a basic version of blackjack game
# It will be played with 2 players (users) and a dealer (computer). We will use a set of 52 cards.
from games import Game
import random
import time

class BlackJack(Game):
    """
    A class representing Blackjack game
    """
    CARD_VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 11}
    SYMBOLS = {'H': "\u2764", 'S': "\u2660", 'D': "\u25C6", 'C': "\u2663"}
    drawn_cards = []

    def __init__(self, players_details):
        self.players_details = players_details

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
    
    def pick_a_card(self):
        '''
        This function is used to draw a card from the pack
        '''
        card = '0'
        points = 0
        while True:
            card_value = random.choice(list(self.CARD_VALUES.keys()))
            symbol = random.choice(list(self.SYMBOLS.values()))
            card = card_value + " " + symbol
            points = self.CARD_VALUES.get(card_value)
            if card!='0' and card not in self.drawn_cards:
                self.drawn_cards.append(card)
                break
        return card, points

    def recalculate_points(self, player):
        '''
        This function is used to recalculate the points for each player according to cards
        '''
        cards = player["cards"]
        for card in cards:
            card_value = card.split()[0]
            if card_value == 'A' and not player.get("recalculated", False):
                # Consider the ace as 1 point
                player["points"] -= 10
                player["recalculated"] = True
        return player
    
    def drawAndCalculatePoints(self, player):
        '''
        This function draws a card and calculates points
        '''
        card, points = self.pick_a_card()
        player["cards"].append(card)
        player["points"] += points
        # print("Points before recalculating ::: {0}".format(player["points"]))
        if player["points"] > 21:
            self.recalculate_points(player)
        return player

    def playAsDealer(self):
        '''
        This function is for Dealer's hand (generates random choice according to score)
        '''
        if self.dealer_details["points"] >= 18 and self.dealer_details["points"] < 21:
            options = random.choice(['h', 's', 'f'])
            if options == 'h':
                print("Dealer draws a card")
                self.dealer_details = self.drawAndCalculatePoints(self.dealer_details)
                time.sleep(2)
                print("Dealer has {} cards and {} points".format(self.dealer_details["cards"], self.dealer_details["points"]))
            return options
        elif self.dealer_details["points"] < 18:
            print("Dealer draws a card")
            self.dealer_details = self.drawAndCalculatePoints(self.dealer_details)
            time.sleep(2)
            print("Dealer has {} cards and {} points".format(self.dealer_details["cards"], self.dealer_details["points"]))
            return 'h'
        elif self.dealer_details["points"] > 21:
            return 'f'
        else:
            return 's'   
    
    def checkForBust(self, player):
        '''
        This function checks if the player has lost
        '''
        if player["points"] > 21:
            return True
        return False
    
    def checkForWin(self, is_first_round):
        '''
        This function checks if any player has scored 21
        '''        
        if self.dealer_details["points"] == 21:
            print("Dealer wins!")
            for name in self.players_details.keys():
                player_dict = self.players_details[name]
                print("{} lost {} coins".format(name, player_dict["bet"]))
            return True
        for name in self.players_details.keys():
            player_dict = self.players_details[name]
            if player_dict["points"] == 21:
                if is_first_round:
                    bet_won = int(player_dict["bet"]) + round(int(player_dict["bet"])/2)
                else:
                    bet_won = int(player_dict["bet"])
                print("Player {} won {} coins".format(name, bet_won))
                return True
    
    def calculatePointsForWin(self, players_in_game):
        '''
        This function is used to calculate the points when everyone stands
        '''
        high_points = 0
        winner = ""
        if "Dealer" in players_in_game:
            high_points = self.dealer_details["points"]
            winner = "Dealer"
        for name in self.players_details.keys():
            if name in players_in_game:
                player_dict = self.players_details[name]
                if player_dict["points"] > high_points:
                    high_points = player_dict["points"]
                    winner = name
                elif player_dict["points"] == high_points:
                    winner = ""
        if winner == "":
            print("Draw Game!")
        else:
            print("{} is the winner! Congrats!!!".format(winner))
        
    def start_game(self):
        '''
        This function is used to start the Blackjack game
        '''
        super().start_game()
        self.display_rules()
        players_in_game = ["Dealer"]
        
        dealer_details = {"points": 0, "cards": []}
        players_details = self.players_details
        # print(players_details)
        print("Dealer shuffles the card!")
        time.sleep(5)
        print("The dealer places two cards for every player")
        print()

        # Dealer draws
        dealer_details = self.drawAndCalculatePoints(dealer_details)
        dealer_details = self.drawAndCalculatePoints(dealer_details)
        self.dealer_details = dealer_details

        print("Dealer has {} cards and {} points".format(dealer_details["cards"], dealer_details["points"]))
        print()
        time.sleep(3)

        # Players draw
        for name in players_details.keys():
            player_dict = players_details[name]
            # print(player_dict)
            players_details[name] = self.drawAndCalculatePoints(player_dict)
            players_details[name] = self.drawAndCalculatePoints(player_dict)
            players_in_game.append(name)
            print("Player {} has {} cards and {} points".format(name, player_dict['cards'], player_dict['points']))
            print()
            time.sleep(3)

        is_game_over = False
        is_first_round = True
        
        # Check for bust and continue to stand or hit
        while not is_game_over:
            # Check if the dealer or player has won
            is_game_over = self.checkForWin(is_first_round)
            if is_game_over:
                break

            if self.checkForBust(dealer_details):
                print("Dealer lost and is out of the game")
                dealer_details["points"] = -1
                players_in_game.remove("Dealer")
            
            for name in players_details.keys():
                player_dict = players_details[name]
                if self.checkForBust(player_dict):
                    print("Player {} lost and is out of the game".format(name))
                    player_dict["points"] = -1
                    players_details[name] = player_dict
                    players_in_game.remove(name)
            
            if len(players_in_game) == 1:
                print("{} is the winner! Congrats!!!".format(players_in_game[0]))
                is_game_over = True
                break
            elif len(players_in_game) == 0:
                print("Draw game!")
                is_game_over = True
                break
            
            print()
            print("*" * 50)
            print()

            standing_players = []
            
            if "Dealer" in players_in_game:
                dealer_choice = self.playAsDealer()
                time.sleep(2)
                if dealer_choice == 's':
                    print("Dealer stands")
                    standing_players.append("Dealer")
                    print("Dealer has {} cards and {} points".format(dealer_details['cards'], dealer_details['points']))
                elif dealer_choice == 'f':
                    print("Dealer folds and is out of the game")
                    players_in_game.remove("Dealer")
                    print("Dealer had {} cards and {} points".format(dealer_details['cards'], dealer_details['points']))
                else:
                    if self.checkForBust(dealer_details):
                        print("Dealer lost and is out of the game")
                        dealer_details["points"] = -1
                        players_in_game.remove("Dealer")
                print()
                if len(players_in_game) == 1:
                    print("{} is the winner! Congrats!!!".format(players_in_game[0]))
                    is_game_over = True
                    break

            for name in players_details.keys():
                if not name in players_in_game:
                    continue
                player_dict = players_details[name]
                choice = 'a'
                while choice.casefold() != 'h'and choice.casefold() != 's' and choice.casefold() != 'f':
                    choice = input("Player "+name+", do you want to hit, stand or fold? Press 'H' for hit, 'S' for stand or 'F' for fold: ")
                    # print("choice: {}".format(choice.casefold()))
                    time.sleep(2)
                    if choice.casefold() == 'h':
                        print("Player {} draws a card".format(name))
                        player_dict = self.drawAndCalculatePoints(player_dict)
                        print("Player {} has {} cards and {} points".format(name, player_dict['cards'], player_dict['points']))
                        if self.checkForBust(player_dict):
                            print("Player {} lost and is out of the game".format(name))
                            player_dict["points"] = -1
                            players_details[name] = player_dict
                            players_in_game.remove(name)
                    elif choice.casefold() == 's':
                        print("Player {} stands".format(name))
                        standing_players.append(name)
                        print("Player {} has {} cards and {} points".format(name, player_dict['cards'], player_dict['points']))
                    elif choice.casefold() == 'f':
                        print("Player {} folds and is out of the game".format(name))
                        players_in_game.remove(name)
                        print("Player {} had {} cards and {} points".format(name, player_dict['cards'], player_dict['points']))
                    else:
                        print("Please enter an appropriate choice!")
                print()
                if len(players_in_game) == 1:
                    print("{} is the winner! Congrats!!!".format(players_in_game[0]))
                    is_game_over = True
                    break

            # Check for winner if everyone stands
            if not is_game_over and sorted(players_in_game) == sorted(standing_players):
                self.calculatePointsForWin(players_in_game)
                break

            is_first_round = False
            self.dealer_details = dealer_details
            self.players_details = players_details

        print(self.drawn_cards)
