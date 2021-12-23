# This class represents a basic version of blackjack game
# It will be played with 2 players (users) and a dealer (computer). We will use a set of 52 cards.
from games import Game
import random

class BlackJack(Game):
    """
    A class representing Blackjack game
    """
    CARD_VALUES = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 11}
    SYMBOLS = {'H': "\u2764", 'S': "\u2660", 'D': "\u25C6", 'C': "\u2663"}
    drawn_cards = []

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
        while True:
            card_value = random.choice(list(self.CARD_VALUES.keys()))
            symbol = random.choice(list(self.SYMBOLS.keys()))
            card = card_value + " " + symbol
            if card!='0' and card not in self.drawn_cards:
                self.drawn_cards.append(card)
                break
        return card
    
    def start_game(self):
        super().start_game()
        self.display_rules()
        print(self.pick_a_card())
        print(self.pick_a_card())
        print(self.pick_a_card())
        print(self.pick_a_card())
        print(self.pick_a_card())
        print(self.drawn_cards)
