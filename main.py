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
from deck import Misc


def main():
    #Card Deck
    #Numbers
    Number.card_numb = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    #Colours
    Colour.red = "Red"
    Colour.black = "Black"

    #Suits
    #Clubs
    Suit.clubs = ["Number: " + Number.card_numb[0] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.", 
    "Number: " + Number.card_numb[1] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[2] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[3] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[4] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[5] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[6] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[7] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[8] + ". Colour: " + Colour.black + ". Suit: " + " ♣️.",
    "Number: " + Number.card_numb[9] + ". Colour: " + Colour.black + ". Suit: " + " ♣️."]

    #Jack
    #Queen
    #King

    #Diamonds
    Suit.diamonds = ["Number: " + Number.card_numb[0] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.", 
    "Number: " + Number.card_numb[1] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[2] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[3] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[4] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[5] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[6] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[7] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[8] + ". Colour: " + Colour.red + ". Suit: " + " ♦️.",
    "Number: " + Number.card_numb[9] + ". Colour: " + Colour.red + ". Suit: " + " ♦️."]

    #Jack
    #Queen
    #King

    #Hearts
    Suit.hearts = ["Number: " + Number.card_numb[0] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.", 
    "Number: " + Number.card_numb[1] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[2] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[3] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[4] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[5] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[6] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[7] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[8] + ". Colour: " + Colour.red + ". Suit: " + " ♥️.",
    "Number: " + Number.card_numb[9] + ". Colour: " + Colour.red + ". Suit: " + " ♥️."]

    #Jack
    #Queen
    #King

    #Spades
    Suit.spades = ["Number: " + Number.card_numb[0] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.", 
    "Number: " + Number.card_numb[1] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[2] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[3] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[4] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[5] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[6] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[7] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[8] + ". Colour: " + Colour.black + ". Suit: " + " ♠️.",
    "Number: " + Number.card_numb[9] + ". Colour: " + Colour.black + ". Suit: " + " ♠️."]

    #Jack
    #Queen
    #King


if __name__ == "__main__":
    main() 