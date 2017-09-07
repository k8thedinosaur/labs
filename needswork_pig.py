# Create a program asks for a _single_ English word and translates it to **Pig Latin**.
# It prints out the input word and the resulting translation like the example below.

# #### Instructions
# 1. If the first letter is a consonant, move it to the end.
# 1. Add "ay" to the end of that.
# 1. If the first letter is a vowel, just ad "yay" to the end.

# > Word? hat
# > hat in Pig Latin is athay
# > Word? apple
# > apple in Pig Latin is appleyay

#### Advanced
# Properly maintain the position of capitalization and punctuation.
# > Word? Cat
# > Cat in Pig Latin is Atcay
# > Word? hat.
# > hat. in Pig Latin is athay.

# #### Super Advanced
# Handle words that start with multiple consonants by moving all of the consonants
#  to the end.
# > Word? string
# > string in Pig Latin is ingstray


# What I did:
vow = 'aeiou'
word = input("Give me a word and I'll say it in Pig Latin!: ")
# if word[0] in vow:
if word[0] in vow:
    word += "yay"
else:
    word = word[1:] + word[0] + "ay"
print(word.capitalize())
#

# # First class version
# word = input("What word would you like translated?: ")
# first_letter = word[0]
# left_over = word[1:]
# vowels = "aeiouAEIOU"
# if first_letter.islower() in vowels:
#     print("{} in Pig Latin is {}yay".format(word).capitalize())
# else:
#     if first_letter.isupper:
#         print("{} in Pig Latin is {}{}ay".format(word, left_over.capitalize(), first_letter.lower()))
#     else:
#         print("{} in Pig Latin is {}{}ay".format(word, left_over, first_letter))

# Better class version
# word = input("Thingy: ")
# def pig_latin(word):
#     vowels = "aeiou"
#     consonant = -1
#     first_letter = ""
#     for letter in word:
#         if letter.lower() in vowels:
#             break
#         else:
#             consonant += 1
#
#     first_letter = word[0:consonant + 1]
#     left_over = word[consonant + 1:]
#
#     if first_letter.lower() in vowels:
#         # print("{} in Pig Latin is {}yay".format(word).capitalize())
#         return "{}yay".format(word.capitalize())
#     else:
#         if first_letter[0].isupper():
#             # print("{} in Pig Latin is {}{}ay".format(word, left_over.capitalize(), first_letter.lower()))
#             return "{}{}ay".format(word, left_over.capitalize(), first_letter.lower())
#         else:
#             # print("{} in Pig Latin is {}{}ay".format(word, left_over, first_letter))
#             return "{}{}ay".format(word, left_over.capitalize(), first_letter.lower())
#
# print(pig_latin(word))