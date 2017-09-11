# # Practice: Blackjack
#
# Let's start modeling a game of [blackjack](https://en.wikipedia.org/wiki/Blackjack).
#
# ## Scoring
#
# Cards have integer point values.
# Aces are 1 or 11, number cards are their number, face cards are all 10.
# A hand is worth the sum of all the points of the cards in it.
# An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
#
# ## Advanced
#
# *   Bring in your dealer hitting logic from the [21 practice problem](/practice/21.md) into a top-level function it's own module `dealer`.
#     Update it to take in a `Hand` instance and return whether to hit.
#
# *   Add a "card counting assistant" function in a module `advisor`.
#     Have it take in a deck and a hand and print out the probability that you will bust.
#     You can find the [expectation value](http://www.wikihow.com/Calculate-an-Expected-Value) of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.
#
# *   Add in a UI so a single user can play versus the dealer.
#
# *   Allow multiple hands to be played with the same deck.


# class Card:
#     def __init__(self, suit):
#         self.suit = suit
#
#     def print_value(self):
#         print(self.suit)
#
#     def __str__(self):
#         return self.suit
#
#     def __repr__(self):
#         return self.__str__()
#
#
# card1 = Card("Hearts")
#
# print([card1])
# card1.print_value()

# class BalanceRequestMixin:
#     def get_balance(self):
#         return "Your balance is {}.".format(self.balance)


import random

# `Card` class with a suit and a rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def Value(self):
        if self.rank == "Ace":
            return 1
        elif self.rank == "King" or self.rank == "Queen" or self.rank == "Jack":
            return 10
        else:
            return int(self.rank)

    def __str__(self):
        return "{}{}".format(rank, suit)



# `Deck` class with a collection of cards
class Deck(Card):
    def __init__(self):
        self.deck


    def shuffle(self):
        random.shuffle(self.deck)

new_deck = Deck

print(new_deck)


#
#     def draw_card(self):
#
#     def draw_hand(self):
#
#     def cut_deck(self):
#
#
# # * Return a shuffled deck
# # * Cut the deck
# # * Draw a card off the top of a deck
#
#
# # `Hand` class with a collection of cards from a deck.
# class Hand:
#     def __init__(self):
#
# # * Add a card to a hand
# # * Allow a user to type in a hand and have it be converted into a `Hand` object
#
#
# # Game (class or function? or new program entirely?)
#
# # * Start a new game of Blackjack, or Quit
# # * Score a hand
# * Bust if the score is over 21
# * Holds players and dealer



class Hand:
    def __init__(self):
        self.hand = []

    def hit(self, card):
        hand.append(card)