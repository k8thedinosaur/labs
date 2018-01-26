# # # Practice: Blackjack
# #
# # Let's start modeling a game of [blackjack](https://en.wikipedia.org/wiki/Blackjack).
# #
# # ## Scoring
# #
# # Cards have integer point values.
# # Aces are 1 or 11, number cards are their number, face cards are all 10.
# # A hand is worth the sum of all the points of the cards in it.
# # An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
# #
# # ## Advanced
# #
# # *   Bring in your dealer hitting logic from the [21 practice problem](/practice/21.md) into a top-level function it's own module `dealer`.
# #     Update it to take in a `Hand` instance and return whether to hit.
# #
# # *   Add a "card counting assistant" function in a module `advisor`.
# #     Have it take in a deck and a hand and print out the probability that you will bust.
# #     You can find the [expectation value](http://www.wikihow.com/Calculate-an-Expected-Value) of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.
# #
# # *   Add in a UI so a single user can play versus the dealer.
# #
# # *   Allow multiple hands to be played with the same deck.
#
#
# # class Card:
# #     def __init__(self, suit):
# #         self.suit = suit
# #
# #     def print_value(self):
# #         print(self.suit)
# #
# #     def __str__(self):
# #         return self.suit
# #
# #     def __repr__(self):
# #         return self.__str__()
# #
# #
# # card1 = Card("Hearts")
# #
# # print([card1])
# # card1.print_value()
#
# # class BalanceRequestMixin:
# #     def get_balance(self):
# #         return "Your balance is {}.".format(self.balance)
#
#
# import random
#
# # `Card` class with a suit and a rank
# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#
#     def getSuit(self):
#         return self.suit
#
#     def getRank(self):
#         return self.rank
#
#     def Value(self):
#         if self.rank == "Ace":
#             return 1
#         elif self.rank == "King" or self.rank == "Queen" or self.rank == "Jack":
#             return 10
#         else:
#             return int(self.rank)
#
#     def __str__(self):
#         return "{}{}".format(rank, suit)
#
#
#
# # `Deck` class with a collection of cards
# class Deck(Card):
#     def __init__(self):
#         self.deck
#
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
# new_deck = Deck
#
# print(new_deck)
#
#
# #
# #     def draw_card(self):
# #
# #     def draw_hand(self):
# #
# #     def cut_deck(self):
# #
# #
# # # * Return a shuffled deck
# # # * Cut the deck
# # # * Draw a card off the top of a deck
# #
# #
# # # `Hand` class with a collection of cards from a deck.
# # class Hand:
# #     def __init__(self):
# #
# # # * Add a card to a hand
# # # * Allow a user to type in a hand and have it be converted into a `Hand` object
# #
# #
# # # Game (class or function? or new program entirely?)
# #
# # # * Start a new game of Blackjack, or Quit
# # # * Score a hand
# # * Bust if the score is over 21
# # * Holds players and dealer
#
#
#
# class Hand:
#     def __init__(self):
#         self.hand = []
#
#     def hit(self, card):
#         hand.append(card)



import random
import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.a, self.b, self.c, self.d, self.e, self.f, self.g = self.arts(self.suit, str(self.value))

    def arts(self, s, v):
        if s == "Clubs":
            a = ".-------."
            b = "|   _   |"
            c = "| _( )_ |"
            d = "|(_ . _)|"
            e = "|   I   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Diamonds":
            a = ".-------."
            b = "|  / \\  |"
            c = "| /   \\ |"
            d = "| \\   / |"
            e = "|  \\ /  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Hearts":
            a = ".-------."
            b = "| ** ** |"
            c = "|*  *  *|"
            d = "| *   * |"
            e = "|   *   |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g
        if s == "Spades":
            a = ".-------."
            b = "|   *   |"
            c = "| *   * |"
            d = "|*     *|"
            e = "|  *I*  |"
            if len(v) == 2:
                f = "|   {}  |".format(v)
            else:
                f = "|   {}   |".format(v[:1])
            g = "'-------'"
            return a, b, c, d, e, f, g

    def card_art(self):
        return self.a + '\n' + self.b + '\n' + self.c + '\n' + self.d + '\n' + self.e + '\n' + self.f + '\n' + self.g

    def __str__(self):
        return self.card_art()

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    def __init__(self, number_of_decks=6):
        self.cards = self.generate_decks(number_of_decks)
        random.shuffle(self.cards)

    def generate_decks(self, n):
        name_value = {
            'Ace': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }
        suits = [
            "Clubs",
            "Diamonds",
            "Hearts",
            "Spades"
        ]
        deck = []
        for i in range(n):
            for suit in suits:
                for r, v in name_value.items():
                    deck.append(Card(suit, r, v))
        return deck


class Hand:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.score = 0

    def score_hand(self):
        self.score = 0
        aces = False
        for i in self.cards:
            if i.value == 1:
                aces = True
                self.score += 1
            else:
                self.score += i.value
        if aces:
            if self.score + 10 <= 21:
                self.score += 10

    def clear_hand(self):
        self.cards = []

    def hit(self, card):
        self.cards.append(card)
        self.score_hand()

    def render_hand(self):
        a = ''
        b = ''
        c = ''
        d = ''
        e = ''
        f = ''
        g = ''

        for card in self.cards:
            a += card.a + '  '
            b += card.b + '  '
            c += card.c + '  '
            d += card.d + '  '
            e += card.e + '  '
            f += card.f + '  '
            g += card.g + '  '

        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)


class Dealer(Hand):
    def __init__(self, name):
        Hand.__init__(self, name)

    def render_dealer_hand(self):
        cls()
        a = self.cards[0].a + '  ' + ".-------."
        b = self.cards[0].b + '  ' + "|*******|"
        c = self.cards[0].c + '  ' + "|0000000|"
        d = self.cards[0].d + '  ' + "|*******|"
        e = self.cards[0].e + '  ' + "|0000000|"
        f = self.cards[0].f + '  ' + "|*******|"
        g = self.cards[0].g + '  ' + "'-------'"

        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)


class Game:
    def __init__(self, decks=6):
        self.players = self.create_players()
        self.dealer = Dealer('Dealer')
        self.deck = Deck(decks)

    def create_players(self):
        number_of_players = int(input('How many players are there? '))
        players = []
        for n in range(number_of_players):
            name = input("What is player {}'s name? ".format(n + 1))
            players.append(Hand(name))
        return players

    def deal_first_round(self):
        self.dealer.clear_hand()
        for x in self.players:
            x.clear_hand()
        for i in range(2):
            for p in self.players:
                p.hit(self.deck.cards.pop())
        self.dealer.hit(self.deck.cards.pop())
        self.dealer.hit(self.deck.cards.pop())

    def play(self):
        gaming = True
        while gaming:
            self.deal_first_round()
            for p in self.players:
                player_turn = True
                while player_turn and p.score < 21:
                    print('=====Dealer=====')
                    self.dealer.render_dealer_hand()
                    print('====={}====='.format(p.name))
                    p.render_hand()
                    query = input('Would you like to Hit or Stay? ')
                    if query.lower() == 'h' or query.lower() == 'hit':
                        p.hit(self.deck.cards.pop())
                    elif query.lower() == 's' or query.lower() == 'stay':
                        player_turn = False
                    else:
                        print('I didn\t understand that')
                else:
                    if p.score > 21:
                        print('=====Dealer=====')
                        self.dealer.render_dealer_hand()
                        print('====={}====='.format(p.name))
                        p.render_hand()
                        print('You Bust!')
                        time.sleep(3)
            else:
                dealer_turn = True
                while dealer_turn and self.dealer.score < 22:
                    print(self.dealer.score)
                    print('=====Dealer=====')
                    self.dealer.render_hand()
                    if self.dealer.score < 16:
                        self.dealer.hit(self.deck.cards.pop())
                        time.sleep(1)
                    else:
                        dealer_turn = False
                else:
                    if self.dealer.score > 21:
                        self.dealer.render_hand()
                        print('Dealer Busts')
                    else:
                        for p in self.players:
                            if self.dealer.score < p.score < 22:
                                print('{} wins!'.format(p.name))
                            elif self.dealer.score == p.score:
                                print('{} pushes'.format(p.name))
                            else:
                                print('{} loses'.format(p.name))
            asking = True
            while asking:
                query = input('Would you like to play again? ')
                if query.lower() == 'y' or query.lower() == 'yes':
                    asking = False
                elif query.lower() == 'n' or query.lower() == 'no':
                    print('Goodbye!')
                    quit()
                else:
                    print('I didn\'t understand that.')


# deck = Deck()
# hand = Hand('player')
# hand.cards.append(Card('Hearts', 'Ace', 1))
# hand.cards.append(Card('Hearts', 'Ace', 10))
#
# print(hand.cards)
# hand.score_hand()
# print(hand.score)
game = Game()
game.play()