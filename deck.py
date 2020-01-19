"""
Classes:
- Suit
- Colour
- Number
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