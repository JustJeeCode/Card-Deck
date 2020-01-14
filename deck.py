"""
Classes:
- Suit
- Colour
- Number
- Misc
"""

"""
class Deck:
    def __init__(self, card_suit, card_number, card_colour):
        self.card_suit = card_suit
        self.card_number = card_number
        self.card_colour = card_colour
"""

class Suit:
    def __init__(self, clubs, diamonds, hearts, spades):
        self.clubs = clubs
        self.diamonds = diamonds
        self.hearts = hearts
        self.spades = spades

class Number:
    def __init__(self, card_numb):
        self.card_numb = card_numb


class Colour:
    def __init__(self, black, red):
        self.black = black
        self.red = red

class Misc:
    def __init__(self, jack, king, queen):
        self.jack = jack
        self.king = king
        self.queen = queen