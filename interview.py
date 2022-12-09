# Lucas King
# 12/08/2022

import random

# Card class
# - A helper class that stores the suit and the value into a Card object
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(self.value, "of", self.suit)

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

# Deck class
class Deck:
    def __init__(self):
        self.deck = list()
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.buildDeck()
    
    def buildDeck(self):
        # Loop through all of the suits
        for i in self.suits:
            # Loop through all card numbers
            for j in range(1, 14):
                dummy_card = Card(i,j)
                self.deck.append(dummy_card)

    def showDeck(self):
        # Loop through all cards in deck
        for i in self.deck:
            i.show()
    
    def shuffleDeck(self):
        random.shuffle(self.deck)
        self.showDeck()

    def getDeck(self):
        return self.deck


def main():
    # Create instance of Deck class
    deck = Deck()
    print("Deck of cards:")
    deck.showDeck()
    print("\nShuffled deck of cards:")
    deck.shuffleDeck()


if __name__ == "__main__":
    main()