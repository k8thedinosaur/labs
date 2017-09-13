# some things to let's do:
# figure out "break outside loop" issue so repeated actions can be made into smaller functions and reduce verbosity of text in program (unlike right here)

# implement magic system
#     assign magic points to character which deplete when spells are used
#     spells are unusable without enough points
#     allow ability to not use spell (or cancel any action in general)
#         how to exit smaller loop and return to main program without closing everything?
#     have magic attacks that build strength with each turn
#         increment turns for higher damage at end, while baddie attacks in between

# implement inventory system to limit restoratives
#     items currently showing as memory location rather than objects

# allow enemy to take random actions (fight, magic, restore)


import random
from random import randint
from needswork_adventure import AnHero, BadGuy, Weapon, Spell, Restorative

# Weapons
pointy_stick = Weapon("Mr. Pointy Stick", 4, "a tree")
better_dagger = Weapon("A Better Dagger", 5, "the ground")
incred_sword = Weapon("Sword of Incredibly Many Stabbings", 10, "between the ribs of a spooky skeleton")
found_weapons = [pointy_stick, better_dagger, incred_sword]

# Restoratives
donut = Restorative("Box of Donuts", 5)

# Hero
an_hero = AnHero("An Hero")
an_hero.health = 25
an_hero.magic = 15
# an_hero.inventory = [donut]
an_hero.inventory.append(donut.name)

# Antihero
some_jerk = BadGuy("Some Jerk")
some_jerk.health = 25

# Spells
attack_sp = Spell("Attack", 3, 6)
cure_sp = Spell("Cure", 5, 10)

# how to get break to work?
# error: "break outside loop"
# def is_dead():
#         if an_hero.health <= 0:
#             print("{} has deathed.".format(an_hero.name))
#             print("Oh no.")
#             break
#
#         if some_jerk.health <= 0:
#             print("{} has deathed.".format(some_jerk.name))
#             print("You win the battle!")
#             break

# same issue
# def escape_attempt():
#     escape = randint(0, 3)
#     if escape >= 3:
#         print("Your escape is successful! You run away like a little baby.")
#         break
#     # if unsuccessful:
#     else:
#         diversions = ["You tell a 'your mom' joke too filthy to repeat here, but {} was spawned from the "
#                       "depths of hell and has no mother, so your taunt has no effect.".format(some_jerk.name),
#                       "You try to distract {0} with a wholesome magic trick, but {0} eats your props and "
#                       "kicks you in the shins for good measure.".format(some_jerk.name)]
#         print(random.choice(diversions))
#         print("Escape unsuccessful!")

def hero_magic_attack():
    spell_success = randint(0, 1)
    if spell_success == 1:
        hero_magic_power = randint(1, attack_sp.power)
        return hero_magic_power

def hero_magic_cure():
    spell_success = randint(0, 1)
    if spell_success == 1:
        hero_magic_restore = randint(1, cure_sp.power)
        return hero_magic_restore

def hero_magic():
    print("Which spell? \n\
    0. None \n\
    1. Attack (3)\n\
    2. Cure (5)")
    spell = input("Enter your choice: ")
    if spell == "0":
        print("While {} is derping about...".format(an_hero.name))
        return
    elif spell == "1":
        if an_hero.magic >= 3:
            hero_magic_power = hero_magic_attack()
            an_hero.magic -= attack_sp.power
            if hero_magic_power is None:
                print("{}'s spell failed!".format(an_hero.name))
            else:
                print("{} casts {} for {} damage!".format(an_hero.name, attack_sp.name, hero_magic_power))
                some_jerk.health -= hero_magic_power
            print("{} has {} magic left.".format(an_hero.name, an_hero.magic))
        else:
            print("{0} doesn't have enough magic! ({0} has {1} points.)".format(an_hero.name, an_hero.magic))
            baddie_fight()
    elif spell == "2":
        if an_hero.magic >= 5:
            hero_magic_restore = hero_magic_cure()
            an_hero.magic -= cure_sp.power
            if hero_magic_restore is None:
                print("{}'s spell failed!".format(an_hero.name))
            else:
                print("{} casts {} to restore {} healths!".format(an_hero.name, cure_sp.name, hero_magic_restore))
                an_hero.health += hero_magic_restore
            print("{} has {} magic left.".format(an_hero.name, an_hero.magic))

        else:
            print("{0} doesn't have enough magic! ({0} has {1} points.)".format(an_hero.name, an_hero.magic))
    else:
        fumble()

# def baddie_magic():
# copy contents

def hero_attack():
    hero_attack_power = randint(0, an_hero.weapon.attack)
    return hero_attack_power

def baddie_attack():
    baddie_attack_power = randint(0, some_jerk.weapon.attack)
    return baddie_attack_power

def hero_fight():
    hero_attack_power = hero_attack()
    if hero_attack_power > 0:
        print("{} attacks {} with {} for {} damage!".format(an_hero.name, some_jerk.name,
                                                            an_hero.weapon, hero_attack_power))
        some_jerk.health -= hero_attack_power
    else:
        print("{0} attacks {1} with {2}. It's a miss! {0} burns with shame.".format(an_hero.name, some_jerk.name, an_hero.weapon))

def baddie_fight():
    baddie_attack_power = baddie_attack()
    if baddie_attack_power > 0:
        print("{} attacks {} with {} for {} damage!".format(some_jerk.name, an_hero.name,
                                                            some_jerk.weapon, baddie_attack_power))
        an_hero.health -= baddie_attack_power
    else:
        print("{0} attacks {1} with {2}. It's a miss! {0} sulks in the corner.".format(some_jerk.name, an_hero.name,  some_jerk.weapon))

# def restore(donut):
#     for i in an_hero.inventory:
#         if i == donut.name:
#             print("{} uses {} to gain {} healths!".format(an_hero.name, donut.name, donut.restore))
#             print(an_hero.inventory)
#             an_hero.inventory.pop(donut.name)
#             print(an_hero.inventory)
#             an_hero.health += donut.restore
#             print("{}'s health is {}.".format(an_hero.name, an_hero.health))
#             print("-------------------------")
#         else:
#             print("{} doesn't have any items!".format(an_hero.name))

def fumble():
    print("That's not an option! While {} is fumbling around like a doofus...".format(an_hero.name))
    baddie_fight()

def is_deathed():
    if an_hero.health <= 0:
        print("{} has deathed.".format(an_hero.name))
        print("Oh no.")
        exit()

    if some_jerk.health <= 0:
        print("{} has deathed.".format(some_jerk.name))
        print("You win the battle!")
        exit()


def battle():
    print("-------------------------")
    print("  A challenger appears!")
    print("-------------------------")

    while True:
        print("")
        print("What will {} do? \n\
    0. Tell me more \n\
    1. Fight \n\
    2. Magic \n\
    3. Use restorative \n\
    4. Try to escape \n\
    5. Search the room for better weapons".format(an_hero.name))
        choice = input("Enter your choice: ")
        print("")
        print("-------------------------")

        # info
        if choice == "0":
            print("{} is using {}, maximum damage {}.".format(an_hero.name, an_hero.weapon, an_hero.weapon.attack))
            print("{} is using {}, maximum damage {}.".format(some_jerk.name, some_jerk.weapon, some_jerk.weapon.attack))
            print("-------------------------")

            print("{}'s health is {}, magic is {}.".format(an_hero.name, an_hero.health, an_hero.magic))
            print("{}'s health is {}, magic is none.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")

        # fight
        elif choice == "1":
            hero_fight()
            baddie_fight()
            print("{}'s health is {}.".format(an_hero.name, an_hero.health, an_hero.magic))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")
            is_deathed()

        elif choice == "2":
            hero_magic()
            baddie_fight()

            print("{}'s health is {}.".format(an_hero.name, an_hero.health, an_hero.magic))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")
            is_deathed()

        # restorative (broken)
        elif choice == "3":
            restore(donut)
            baddie_fight()

        # escape
        elif choice == "4":
            escape = randint(0, 3)
            if escape >= 3:
                print("{0}'s escape is successful! {0} runs away like a little baby.".format(an_hero.name))
                break
            # if unsuccessful:
            else:
                diversions = ["{0} tells a 'your mom' joke too filthy to repeat here, but {1} was spawned from the "
                              "depths of hell and has no mother, so {0} taunt has no effect.".format(an_hero.name, some_jerk.name),
                              "{0} tries to distract {1} with a wholesome magic trick, but {1} eats {0}'s props and "
                              "kicks {0} in the shins for good measure.".format(an_hero.name, some_jerk.name)]
                print(random.choice(diversions))
                print("Escape unsuccessful!")
                baddie_fight()

                print("{}'s health is {}.".format(an_hero.name, an_hero.health))
                print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
                print("-------------------------")

        # search for weapon
        elif choice == "5":
            new_weapon = randint(1, 5)
            if new_weapon >= 5:
                which_weapon = random.choice(found_weapons)
                an_hero.weapon = which_weapon
                print("{} found {}. Sweet!".format(an_hero.name, which_weapon))

            else:
                print("{} didn't find anything.".format(an_hero.name))

                baddie_fight()
                print("{}'s health is {}.".format(an_hero.name, an_hero.health))
                print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
                print("-------------------------")

        # fumble
        else:
            fumble()
            print("{}'s health is {}.".format(an_hero.name, an_hero.health))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")


battle()