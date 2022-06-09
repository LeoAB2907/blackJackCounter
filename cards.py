from enum import Enum


class PlayingCard:
    def __init__(self, card, suit):
        self.card = card
        self.suit = suit
        self.path = "assets/" + suit.value + "/" + card.value + ".png"
        if card.value.isdigit():
            self.value = int(card.value)
        elif card.value.isalpha() and card.value != 'A':
            self.value = 10
        else:
            self.value = 11

    def __str__(self):
        return f'PlayingCard({self.card}, {self.suit}, {self.value})'


class Card(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'


class Suit(Enum):
    SPADES = 'spade'
    CLUBS = 'club'
    HEARTS = 'heart'
    DIAMONDS = 'diamond'


def initialize_deck(num):
    deck = []
    full_deck = []
    for card in Card:
        for suit in Suit:
            deck.append(PlayingCard(Card(card), Suit(suit)))
    for i in range(num):
        full_deck.append(deck)

    return full_deck