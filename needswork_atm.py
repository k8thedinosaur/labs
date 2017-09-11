# # Lab: ATM Interface
#
# Save your solution in a directory in `practice/` named `atm-interface`.
#
# An account will be a class named `Account` in a module named `account`: it will have private attributes for the balance and interest rate.
# Remember to underscore `_` prefix any private attributes.
# A newly-instantiated account will have zero balance and an interest rate of 0.1%.
#
# Write class methods in the account class that:
#
# * `get_funds()` Return account balance
# * `deposit(amount)` Deposit to the account
# * `check_withdrawal(amount)` Return `True` if large enough balance for a withdrawal
# * `withdraw(amount)` Withdraw an allowed amount; raise a `ValueError` if insufficent balance
# * `calc_interest()` Calculate and return interest on the current account balance
#
# ## Advanced
#
# Write a program that functions as a simple ATM for two accounts:
#
# 1. Checking account
# 1. Savings account
#
# Implement a user interface in a module `main` that lets a user pick each of those actions for a given account and updates the account.
# After each action it will print the balance.
#
# ## Super Advanced
#
# Adds some advanced features to the account class.
#
# *   Add a function called `get_standing()` have it return a bool with whether the account has less than $1000 in it.
#
# *   Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.
#
# *   Save the account balance to a file after each operation.
#     Read that balance on startup so the balance persists across program starts.
#
# *   Add to each account class an account ID number.
#
# *   Allow the user to open more than one account.
#     Let them perform all of the above operations by account number.




# class BankAccount(BalanceRequestMixin):
#     def __init__(self, f_name, l_name, balance=0):
#         self.f_name = f_name
#         self.l_name = l_name
#         self.full_name = self.f_name + " " + self.l_name
#         self.balance = balance
#         self.setup()
#
#     def deposit(self, amount):
#         self.balance += amount
#         print("You have deposited {}. Your new balance is {}.".format(amount, self.balance))
#
#     def withdraw(self, amount):
#         if self.balance - amount >= 0:
#             self.balance -= amount
#             print("You have withdrawn {}. Your new balance is {}.".format(amount, self.balance))
#         else:
#             print("Insufficient funds.")
#
#     def setup(self):
#         print("You have created an account for {}".format(self.full_name))
#
#     def __str__(self):
#         return "Account of {}.".format(self.full_name)
#
#     def __repr__(self):
#         return self.__str__()
#
# class AltBankAccount(BankAccount, BalanceRequestMixin):
#     def withdraw(self, amount, cancel=False):
#         if cancel:
#             return super().withdraw(amount)
#         elif self.balance - amount - 200 >= 0:
#             self.balance -= amount
#             print("You have withdrawn {}. Your new balance is {}.".format(amount, self.balance))
#         else:
#             print("Insufficient funds. >:[")
#
#
# account1 = BankAccount("Kate", "Cat", 60)
# account2 = AltBankAccount("Murray", "Cat", 5000)
#
# print(account1.balance)
# print(account2.balance)
#
# # account2.withdraw(5000, True)