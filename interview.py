# Lucas King
# 12/08/2022

import random

# The pokerHand class
# Where all the evaluation of the 5-card hand is
class pokerHand:
    def __init__(self, hand, hand_dict):
        self.hand = hand
        self.hand_dict = hand_dict
        self.is_straight = False
        self.card_values = list(hand_dict.keys())
        self.card_values.sort()
        self.card_counts = self.cardCounts()
        self.is_flush = self.checkFlush()
        self.checkStraight()
        self.is_pair = False
        self.is_2_pair = False
        self.is_3_of_kind = False
        self.is_4_of_kind = False
        self.is_full_house = False
        self.is_straight_flush = False
        self.is_royal_flush = False
        self.duplicateCards()
        # self.finalOutPut()

    # Creates a dictionary with key as the card number and the data is the number of occurances
    def cardCounts(self):
        temp_counts = dict()
        for i in self.hand_dict.keys():
            temp_counts[i] = len(self.hand_dict[i])
        return temp_counts

    # Checks to see if all cards in the hand of the same suit
    def checkFlush(self):
        # Loop through cards in the users hand
        for i in self.hand:
            # If the suits are not the same then return false
            if (self.hand[0].getSuit() != i.getSuit()):
                return False
        print("\nYou have a flush!")
        return True

    # Checks for a straight by checking the length of card_values list
    def checkStraight(self):
        if (len(self.card_values) == 5):
            card_range = self.card_values[-1] - self.card_values[0]
            if (card_range == 4):
                print("\nYou have a straight!")
                self.is_straight = True
            else:
                # Accounting for the Ace of a suit
                if ((card_range == 12) and ((self.card_values[-1] - self.card_values[1]) == 3)):
                    print("\nYou have a straight!")
                    self.is_straight = True
                else:
                    self.is_straight = False

    def duplicateCards(self):
        # If there are 4 unique values then there is only 1 pair
        if (len(self.card_values) == 4):
            print("\nYou have a pair!")
            self.is_pair = True
        # There are 3 unique values then you can have 3-of-a-kind or 2-pair
        elif (len(self.card_values) == 3):
            max_occurances = 0
            for i in self.card_counts.keys():
                if (self.card_counts[i] > max_occurances):
                    max_occurances = self.card_counts[i]
            if (max_occurances == 3):
                print("\nYou have a 3-of-a-kind!")
                self.is_3_of_kind = True
            else:
                print("\nYou have two pairs!")
                self.is_2_pair = True
        # If only 2 unique values then 4 of a kind, full house
        elif (len(self.card_values) == 2):
            max_occurances = 0
            for i in self.card_counts.keys():
                if (self.card_counts[i] > max_occurances):
                    max_occurances = self.card_counts[i]
            if (max_occurances == 4):
                print("\nYou have a 4-of-a-kind")
                self.is_4_of_kind = True
            else:
                print("\nYou have a full house!")
                self.is_full_house = True

    
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
        # self.showDeck()

    def getDeck(self):
        return self.deck

# Helper function that deals 5 cards to the user
def deal(card_deck):
    user_hand = card_deck[0:5]
    print("\nYour hand is:")
    for i in user_hand:
        i.show()
    return user_hand

# Helper function that saves the 5-card information into a dictionary for later use
def dictHand(user_hand):
    ordered_hand = dict()
    # Loop through user hand to store into dictionary
    for i in user_hand:
        if (i.getValue() in ordered_hand.keys()):
            ordered_hand[i.getValue()].append(i)
        else:
            ordered_hand[i.getValue()] = [i]
    return ordered_hand

def main():
    # Create instance of Deck class
    deck = Deck()
    # print("Deck of cards:")
    # deck.showDeck()
    # print("\nShuffled deck of cards:")
    deck.shuffleDeck()

    user_hand = deal(deck.getDeck())    # User's 5-card hand
    dict_hand = dictHand(user_hand)
    playPoker = pokerHand(user_hand, dict_hand)


if __name__ == "__main__":
    main()