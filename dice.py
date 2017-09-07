# # Lab: Dice
# ##### Goal
# Write a simple program that, when run, prompts the user for input then prints a result.
# ##### Instructions
# Program should ask the user for the number of dice they want to roll as well as the number of sides per die.
# #### Documentation
# 1. [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)
# 1. [Python Std. Library: Random Module random.randint()](https://docs.python.org/3/library/random.html#random.randint)
# #### Key Concepts
# - Importing
# - The Random Module
# - `for` looping
# - `input()` function
# - programmatic logic

# randint is randrange + 1
# print(randint(1, 10))
# print(randrange(1, 10))

from random import randrange


# testing version
# def dice_roll():
#     while True:
#         # ask for number of dice
#         dice = int(input("How many dice would you like to roll? "))
#         # ask for number of sides
#         sides = int(input("How many sides do the dice have? "))
#
#
#         # for loop to roll
#         for i in range(dice):
#             i + 1
#             answer = randrange(1, sides)
#             print(str(answer))
#
# dice_roll()

# useful version
dice = int(input("How many dice would you like to roll? "))
sides = int(input("How many sides do the dice have? "))

def dice_roll():
    # for loop to roll
    for i in range(dice):
        i + 1
        answer = randrange(1, sides)
        return (str(answer))

dice_roll()