class Card:
    def __init__(self, suit):
        self.suit = suit

    def print_value(self):
        print(self.suit)

    def __str__(self):
        return self.suit

    def __repr__(self):
        return self.__str__()


card1 = Card("Hearts")

print([card1])
card1.print_value()