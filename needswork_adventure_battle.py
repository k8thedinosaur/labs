from needswork_adventure import AnHero, BadGuy, Weapon, Restorative

from random import randint


pointy_stick = Weapon("Mr. Pointy Stick", 4, "a tree")
better_dagger = Weapon("Better Dagger", 5, "the ground")

donut = Restorative("Box of Donuts", 5)
# donut.restore = 5

an_hero = AnHero("An Hero")
an_hero.health = 25
# an_hero.weapon = better_dagger
some_jerk = BadGuy("Some Jerk")
some_jerk.health = 25
# some_jerk.weapon = pointy_stick


def hero_attack():
    global hero_attack_power
    hero_attack_power = randint(0, an_hero.weapon.attack)
    return hero_attack_power


def baddie_attack():
    global baddie_attack_power
    baddie_attack_power = randint(0, some_jerk.weapon.attack)
    return baddie_attack_power


def fight(an_hero, some_jerk):
    print("{} attacks {} with {} for {} damage!".format(an_hero.name, some_jerk.name, an_hero.weapon, hero_attack()))
    some_jerk.health -= hero_attack_power
    print("{} attacks {} with {} for {} damage!".format(some_jerk.name, an_hero.name, some_jerk.weapon, baddie_attack()))
    an_hero.health -= baddie_attack_power
    print("{}'s health is {}.".format(an_hero.name, an_hero.health))
    print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
    print("-------------------------")


def restore(donut):
    print("{} uses {} to gain {} healths!".format(an_hero.name, donut.name, donut.restore))
    an_hero.health += donut.restore
    print("{}'s health is {}.".format(an_hero.name, an_hero.health))
    print("-------------------------")


def battle():
    print("-------------------------")
    print("  A challenger appears!")
    print("-------------------------")

    while True:
        print("What will you do? \n 0. Tell me more \n 1. Fight \n 2. Use restorative \n 3. Run away")
        choice = input("Enter your choice: ")
        print("-------------------------")

        if choice == "0":
            print("{}'s health is {}.".format(an_hero.name, an_hero.health))
            print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
            print("-------------------------")
            print("{} is using {}, maximum damage {}.".format(an_hero.name, an_hero.weapon, an_hero.weapon.attack))
            print("{} is using {}, maximum damage {}.".format(some_jerk.name, some_jerk.weapon, some_jerk.weapon.attack))
            print("-------------------------")

        elif choice == "1":
            # randint decides the strength of your and your enemy's attacks
            fight(an_hero, some_jerk)

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

        elif choice == "3":
            escape = randint(0, 3)
            if escape >= 3:
                print("Your escape is successful!")
                break
            else:
                print("Escape unsuccessful!")
                # if unsuccessful:
                print("{} attacks {} with {} for {} damage!".format(some_jerk.name, an_hero.name,
                                                                    some_jerk.weapon, baddie_attack()))
                an_hero.health -= baddie_attack_power

                print("{}'s health is {}.".format(an_hero.name, an_hero.health))
                print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
                print("-------------------------")

battle()


# print("{} picks up {} from {}.".format(some_jerk.name, pointy_stick.name, pointy_stick.location))
# print("---------------------")
# some_jerk.weapon = pointy_stick
#
# print("{} picks up {} from {}.".format(an_hero.name, better_dagger.name, better_dagger.location))
# print("---------------------")
# an_hero.weapon = better_dagger
#
