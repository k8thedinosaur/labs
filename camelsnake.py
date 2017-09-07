# # Lab: Case Conversion
# Write a program that prompts the user for a word.
# Print out either  `snake_case` or `CamelCase` depending case convention it is!.
# ##### Instructions
# Use substring membership with the `in` operator


# testing version
# def camel_snake():
#     while True:
#         word = input("What word would you like to check? ")
#         under = "_"
#         first_letter = word[0]
#         if first_letter.upper() in word:
#             if under not in word:
#                 print("{} is CamelCase!".format(word))
#             else:
#                 print("{} is neither snake_case nor CamelCase.".format(word))
#         elif under in word:
#             if first_letter.lower():
#                 print("{} is snake_case!".format(word))
#             elif first_letter.upper():
#                 print("{} is neither snake_case nor CamelCase.".format(word))
#
#
#
# camel_snake()


# useful version
def camel_snake(word):
    under = "_"
    first_letter = word[0]
    if first_letter.upper() in word:
        if under not in word:
            return "{} is CamelCase!".format(word)
        else:
            return "{} is incorrectly formatted. You made a Camel_snake!".format(word)

    elif under in word:
        if first_letter.lower():
            return "{} is snake_case!".format(word)
        elif first_letter.upper():
            return "{} is incorrectly formatted. You made a Camel_snake!".format(word)
        else:
            return "{} is incorrectly formatted. You made a Camel_snake!".format(word)
