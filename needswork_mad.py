import random
from random import shuffle

# The complicated list-y way (doees not work)
# Lists for the complicated list-y way
# noun = []
# noun.append(input("Enter 3 nouns, separated by commas: "))
# noun.split(", ")
#
# adjective = []
# adjective.append(input("Enter 6 adjectives, separated by commas: "))
# adjective.split(", ")
#
# verb = []
# verb.append(input("Enter 2 verbs, separated by commas: "))
# verb.split(", ")
#

# def split_words(string):
#     word_list = string.split(", ")
#     shuffle(word_list)
#     return word_list
#
# noun = input("Enter 3 nouns, separated by commas: ")
# adjective = input("Enter 6 adjectives, separated by commas: ")
# verb = input("Enter 2 verbs, separated by commas: ")
#
# nouns_list = split_words(noun)
# adjectives_list = split_words(adjective)
# verbs_list = split_words(verb)
#
# # Additional inputs not in lists...
# place1 = input("A geological feature (earth, sea, cliff): ")
# creature1 = input("Mythical Humanoid Creature: ")
# creature2 = input("Icky Creature (plural): ")


# Words in order...
# noun1 = input("Noun: ")
# place1 = input("A geological feature (earth, sea, cliff): ")
# creature1 = input("Mythical Humanoid Creature: ")
# adj1 = input("Adjective: ")
# adj2 = input("Adjective: ")
# adj3 = input("Adjective: ")
# noun3 = input("Noun: ")
# creature2 = input("Icky Creature (plural): ")
# adj4 = input("Adjective: ")
# adj5 = input("Adjective: ")
# adj6 = input("And one more Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# noun2 = input("Noun: ")
#
playing = True

while playing:
    query = input("Press 1 to enter words, 2 to read story, 3 to exit")
    if query == "1":
        def split_words(string):
            word_list = string.split(", ")
            shuffle(word_list)
            return word_list

        noun = input("Enter 3 nouns, separated by commas: ")
        adjective = input("Enter 6 adjectives, separated by commas: ")
        verb = input("Enter 2 verbs, separated by commas: ")

        nouns_list = split_words(noun)
        adjectives_list = split_words(adjective)
        verbs_list = split_words(verb)

        # Additional inputs not in lists...
        place1 = input("A geological feature (earth, sea, cliff): ")
        creature1 = input("Mythical Humanoid Creature: ")
        creature2 = input("Icky Creature (plural): ")

    elif query == "2":
        print("In a {} in the {} there lived a {}. Not a {}, {}, {} {}, filled with the {} of {}, nor yet a {}, {}, {} {}, with nothing to {} on, and nothing to {}. This was a {}-{}, and that means {}.".format(noun, place1, creature1, adjective, adjective, adjective, noun, noun, creature2, adjective, adjective, adjective, noun, verb, verb, creature1, noun, noun))
    elif query == "3":
        print("Goodbye!")
        playing = False
    else:
        print("You borked it.")






# The clumsy way...
# print("In a " + noun1 + " in the " + place1 + " there lived a " + creature1 + ". Not a " + adj1 + ", " + adj2 + ", " + adj3 + " " + noun1 + ", filled with the " + noun1 + " of " + creature2 + ", nor yet a " + adj4 + ", " + adj5 + ", " + adj6 + " " + noun1 + ", with nothing to " + verb1 + " on, and nothing to " + verb2 + ". This was a " + creature1 + "-" + noun1 + ", and that means " + noun2 + ".")

# The proper story...
# print("In a {} in the {} there lived a {}. Not a {}, {}, {} {}, filled with the {} of {}, nor yet a {}, {}, {} {}, with nothing to {} on, and nothing to {}. This was a {}-{}, and that means {}.".format(noun1, place1, creature1, adj1, adj2, adj3, noun1, noun3, creature2, adj4, adj5, adj6, noun1, verb1, verb2, creature1, noun1, noun2))

# The ~!*rAnDoM*!~ version...
# print("In a {} in the {} there lived a {}. Not a {}, {}, {} {}, filled with the {} of {}, nor yet a {}, {}, {} {}, with nothing to {} on, and nothing to {}. This was a {}-{}, and that means {}.".format(random.choice(noun), place1, creature1, random.choice(adjective), random.choice(adjective), random.choice(adjective), random.choice(noun), random.choice(noun), creature2, random.choice(adjective), random.choice(adjective), random.choice(adjective), random.choice(noun), random.choice(verb), random.choice(verb), creature1, random.choice(noun), random.choice(noun)))

# def mad_lib():
#     query = input("Press 1 to enter words, 2 to read story, 3 to exit")
#     if query == "1":
#         def split_words(string):
#             word_list = string.split(", ")
#             shuffle(word_list)
#             return word_list
#
#
#         noun = input("Enter 3 nouns, separated by commas: ")
#         adjective = input("Enter 6 adjectives, separated by commas: ")
#         verb = input("Enter 2 verbs, separated by commas: ")
#
#         nouns_list = split_words(noun)
#         adjectives_list = split_words(adjective)
#         verbs_list = split_words(verb)
#
#         # Additional inputs not in lists...
#         place1 = input("A geological feature (earth, sea, cliff): ")
#         creature1 = input("Mythical Humanoid Creature: ")
#         creature2 = input("Icky Creature (plural): ")
#
#     elif query == "2":
#         return "In a {} in the {} there lived a {}. Not a {}, {}, {} {}, filled with the {} of {}, nor yet a {}, {}, {} {}, with nothing to {} on, and nothing to {}. This was a {}-{}, and that means {}.".format(
#             noun1, place1, creature1, adj1, adj2, adj3, noun1, noun3, creature2, adj4, adj5, adj6, noun1, verb1, verb2,
#             creature1, noun1, noun2
#         elif query == "3":
#         return "Goodbye!"
#         playing = False
#     else:
#         return "You borked it."
#
# print(mad_lib())