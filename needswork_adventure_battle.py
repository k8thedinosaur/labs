import random
from random import randint
from needswork_adventure import AnHero, BadGuy, Weapon, Restorative


pointy_stick = Weapon("Mr. Pointy Stick", 4, "a tree")
better_dagger = Weapon("A Better Dagger", 5, "the ground")
incred_sword = Weapon("Sword of Incredibly Many Stabbings", 10, "between the ribs of a spooky skeleton")
found_weapons = [pointy_stick, better_dagger, incred_sword]


donut = Restorative("Box of Donuts", 5)

an_hero = AnHero("An Hero")
an_hero.health = 25

some_jerk = BadGuy("Some Jerk")
some_jerk.health = 25


def hero_attack():
    hero_attack_power = randint(0, an_hero.weapon.attack)
    return hero_attack_power


def baddie_attack():
    baddie_attack_power = randint(0, some_jerk.weapon.attack)
    return baddie_attack_power


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
    # escape = randint(0, 3)
    # if escape >= 3:
    #     print("Your escape is successful! You run away like a little baby.")
    #     break
    # # if unsuccessful:
    # else:
    #     diversions = ["You tell a 'your mom' joke too filthy to repeat here, but {} was spawned from the "
    #                   "depths of hell and has no mother, so your taunt has no effect.".format(some_jerk.name),
    #                   "You try to distract {0} with a wholesome magic trick, but {0} eats your props and "
    #                   "kicks you in the shins for good measure.".format(some_jerk.name)]
    #     print(random.choice(diversions))
    #     print("Escape unsuccessful!")

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


def restore(donut):
    print("{} uses {} to gain {} healths!".format(an_hero.name, donut.name, donut.restore))
    an_hero.health += donut.restore
    print("{}'s health is {}.".format(an_hero.name, an_hero.health))
    print("-------------------------")

def escape_attempt():
    escape = randint(0, 3)
    if escape >= 3:
        print("Your escape is successful! You run away like a little baby.")
        break
    # if unsuccessful:
    else:
        diversions = ["You tell a 'your mom' joke too filthy to repeat here, but {} was spawned from the "
                      "depths of hell and has no mother, so your taunt has no effect.".format(some_jerk.name),
                      "You try to distract {0} with a wholesome magic trick, but {0} eats your props and "
                      "kicks you in the shins for good measure.".format(some_jerk.name)]
        print(random.choice(diversions))
        print("Escape unsuccessful!")


def battle():
    print("-------------------------")
    print("  A challenger appears!")
    print("-------------------------")

    while True:
        print("")
        print("What will you do? \n\
        0. Tell me more \n\
        1. Fight \n\
        2. Use restorative \n\
        3. Try to escape \n\
        4. Search the room for better weapons")
        choice = input("Enter your choice: ")
        print("")
        print("-------------------------")

        if choice == "0":
            print("{} is using {}, maximum damage {}.".format(an_hero.name, an_hero.weapon, an_hero.weapon.attack))
            print("{} is using {}, maximum damage {}.".format(some_jerk.name, some_jerk.weapon, some_jerk.weapon.attack))
            print("-------------------------")

            print("{}'s health is {}.".format(an_hero.name, an_hero.health))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")

        elif choice == "1":
            hero_fight()
            baddie_fight()
            print("{}'s health is {}.".format(an_hero.name, an_hero.health))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")

            if an_hero.health <= 0:
                print("{} has deathed.".format(an_hero.name))
                print("Oh no.")
                break

            if some_jerk.health <= 0:
                print("{} has deathed.".format(some_jerk.name))
                print("You win the battle!")
                break


        elif choice == "2":
            restore(donut)
            baddie_fight()

        elif choice == "3":
            escape = randint(0, 3)
            if escape >= 3:
                print("Your escape is successful! You run away like a little baby.")
                break
            # if unsuccessful:
            else:
                diversions = ["You tell a 'your mom' joke too filthy to repeat here, but {} was spawned from the "
                              "depths of hell and has no mother, so your taunt has no effect.".format(some_jerk.name),
                              "You try to distract {0} with a wholesome magic trick, but {0} eats your props and "
                              "kicks you in the shins for good measure.".format(some_jerk.name)]
                print(random.choice(diversions))
                print("Escape unsuccessful!")
                baddie_fight()

                print("{}'s health is {}.".format(an_hero.name, an_hero.health))
                print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
                print("-------------------------")

        elif choice == "4":
            new_weapon = randint(0, 5)
            if new_weapon >= 5:
                which_weapon = random.choice(found_weapons)
                an_hero.weapon = which_weapon
                print("{} found {}. Sweet!".format(an_hero.name, which_weapon))

            else:
                print("You didn't find anything.")

                baddie_fight()
                print("{}'s health is {}.".format(an_hero.name, an_hero.health))
                print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
                print("-------------------------")
        else:
            print("That's not an option! While {} is fumbling around like a doofus...".format(an_hero.name))
            baddie_fight()

            print("{}'s health is {}.".format(an_hero.name, an_hero.health))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")


battle()