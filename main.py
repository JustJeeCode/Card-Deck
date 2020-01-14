"""
Deck Of Cards
by JustJeeCode.

Todo List:
- Make the deck of cards
    - 3 types in a card (suit, number, colour)
- Make a function where you can shuffle them
"""
from deck import Suit
from deck import Number
from deck import Colour


def main():
    #Card Deck
    #Numbers
    Number.card_numb = ["ace ", 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

    #Colours
    Colour.red = "red"
    Colour.black = "black"

    #Suits
    Suit.clubs = [Number.card_numb[0] + Colour.black + " ♣️"]
    Suit.diamonds = []
    Suit.hearts = []
    Suit.spades = []

    print(Suit.clubs)

if __name__ == "__main__":
    main() 