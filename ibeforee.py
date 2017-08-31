# # Lab: I before E except after C.
# From wikipedia:
# "The i before e except after c rule is not worth teaching. It applies only to words in which the ie or ei stands for a clear /ee/ sound and unless this is known, words such as 'sufficient', 'veil' and 'their' look like exceptions."
# #### Goal
# Create a program that asks for a _single_ English word and checks if it follows the rule **"I before E except after C".**
# # #### Instructions
# 1. Create a file named `spelling.py`
# 1. Write a function that searches for the index of any instances of `ie` in the string, then see if the preceding letter is `c`.
# #### Advanced
#  * Find a list of exceptions to use and check if the word given is an exception to the rule.
# #### Key Concepts
## - string lookup with `in`

# testing version
def i_before_e():
    word = input("What word would you like to check? ")
    while True:
        i_e = "ie"
        c_i_e = "cie"
        if c_i_e in word:
            print("{} has i before e after c! You've broken language!".format(word))
        elif i_e in word:
            print("{} has i before e but no c.".format(word))
        else:
            print("{} does not contain i before e.".format(word))
i_before_e()

# useful version
# word = input("What word would you like to check? ")
#
# def i_before_e(word):
#     i_e = "ie"
#     c_i_e = "cie"
#     if c_i_e in word:
#         return "{} has i before e after c! You've broken language!".format(word)
#     elif i_e in word:
#         return "{} has i before e but no c.".format(word)
#     else:
#         return "{} does not contain i before e.".format(word)
# i_before_e(word)
