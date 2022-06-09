import cards
import random


class RunningCount:

    def __init__(self):
        self.deck = cards.initialize_deck(1)  # default 1 deck
        self.running_count = 0
        self.true_count = 0
        self.cards_played = 0
        self.decks_left = 1

    """
     Initializes the game. Loads the decks and calls shuffle() to shuffle the cards
    """
    def init_game(self, num_decks):
        self.deck = cards.initialize_deck(num_decks)
        self.shuffle()

    """
     Shuffles the decks
    """
    def shuffle(self):
        random.shuffle(self.deck)

    """
     Resets the game with a different number of decks
    """
    def reset_game(self, num_decks):
        self.init_game(num_decks)

    """
     Increases the running count
    """
    def increase_count(self):
        ++self.running_count
        ++self.cards_played
        self.adjust_count()

    """
     Decreases the running count
    """
    def decrease_count(self):
        --self.running_count
        ++self.cards_played
        self.adjust_count()

    """
     Adjusts the true count each time a full deck of cards has been played
    """
    def adjust_count(self):
        if self.cards_played == 52:
            --self.decks_left
            self.cards_played = 0
            self.true_count = self.running_count/self.decks_left

    """
     Returns the Next card
    """
    def get_card(self):
        return self.deck.pop

