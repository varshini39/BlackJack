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
    
    def start_game(self):
        '''
        This function is used to start the Blackjack game
        '''
        super().start_game()
        self.display_rules()
        
        dealer_points = 0
        dealer_cards = []
        players_details = self.players_details
        # print(players_details)
        print("Dealer shuffles the card!")
        time.sleep(5)
        print("The dealer places two cards for every player")
        print()

        # Dealer draws
        card, points = self.pick_a_card()
        dealer_cards.append(card)
        dealer_points += points
        card, points = self.pick_a_card()
        dealer_cards.append(card)
        dealer_points += points
        print("Dealer has {} cards and {} points".format(dealer_cards, dealer_points))
        print()
        time.sleep(3)

        # Players draw
        for name in players_details.keys():
            player_dict = players_details[name]
            # print(player_dict)
            card, points = self.pick_a_card()
            player_dict['cards'].append(card)
            player_dict['points'] += points
            card, points = self.pick_a_card()
            player_dict['cards'].append(card)
            player_dict['points'] += points
            print("Player {} has {} cards and {} points".format(name, player_dict['cards'], player_dict['points']))
            print()
            time.sleep(3)

        print(self.drawn_cards)
