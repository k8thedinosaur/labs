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

class BalanceRequestMixin:
    def get_balance(self):
        return "Your balance is {}.".format(self.balance)


class BankAccount(BalanceRequestMixin):
    def __init__(self, f_name, l_name, balance=0):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + " " + self.l_name
        self.balance = balance
        self.setup()

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {}. Your new balance is {}.".format(amount, self.balance))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("You have withdrawn {}. Your new balance is {}.".format(amount, self.balance))
        else:
            print("Insufficient funds.")

    def setup(self):
        print("You have created an account for {}".format(self.full_name))

    def __str__(self):
        return "Account of {}.".format(self.full_name)

    def __repr__(self):
        return self.__str__()

class AltBankAccount(BankAccount, BalanceRequestMixin):
    def withdraw(self, amount, cancel=False):
        if cancel:
            return super().withdraw(amount)
        elif self.balance - amount - 200 >= 0:
            self.balance -= amount
            print("You have withdrawn {}. Your new balance is {}.".format(amount, self.balance))
        else:
            print("Insufficient funds. >:[")


account1 = BankAccount("Kate", "Cat", 60)
account2 = AltBankAccount("Murray", "Cat", 5000)

print(account1.balance)
print(account2.balance)

# account2.withdraw(5000, True)