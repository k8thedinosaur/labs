# # Practice: Adventure Game
#
# Save your solution in a directory in `practice/` named `adventure`.
#
# Write a [NetHack](https://en.wikipedia.org/wiki/NetHack)-like terminal based dungeon crawler game.
#
# There are various **entities** in the game.
# Make each entity a class in it's own module.
#
# *   Creature
#     * Location
#     * Health
#     * Weapon
#
# *   Weapon
#     * Location (or None if picked up)
#     * Damage
#
# *   Potion
#     * Location
#     * Health Restored
#
# Put any functions that manipulate these classes in their respective modules.

# class NPC:
#     def __init__(self, name):
#         self.weapon = Weapon("Crappy Dagger", 3)
#         self.name = name
#         self.hp = 100
#
#
# class Weapon:
#     def __init__(self, name, ap):
#         self.name = name
#         self.ap = ap
#     def __str__(self):
#         return self.name
#
# def round_of_battle(npc1, npc2):
#     npc1.hp -= npc2.weapon.ap
#     npc2.hp -= npc1.weapon.ap
#
# player = NPC("Kate")
# orc = NPC("Orc Guy")
# sword = Weapon("Sword of many stabbings", 20)
# axe = Weapon("Axe of  great hackings", 20)
#
# # player.weapon = sword
# orc.weapon = axe
#
# print(player.weapon)
#
# print(player.hp, orc.hp)
# round_of_battle(player, orc)
# print(player.hp, orc.hp)



class AnHero:
    def __init__(self, name):
        self.name = name
        self.health = 25
        self.weapon = Weapon("Crappy Dagger", 3, "inventory")

    def __str__(self):
        return self.name


class BadGuy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Crappy Dagger", 3, "inventory")

    def __str__(self):
        return self.name


class Weapon:
    def __init__(self, name, attack, location):
        self.name = name
        self.attack = attack
        self.location = location

    def __str__(self):
        return self.name


# potion
#     * Location
#     * Health Restored
class Restorative:
    def __init__(self, name):
        self.name = name
        self.restore = restore

    def __str__(self):
        return self.name

# def battle():
#
#
def fight(an_hero, some_jerk):
    print("{} attacks {} with {} for {} damage!".format(an_hero.name, some_jerk.name, an_hero.weapon,
                                                        an_hero.weapon.attack))
    some_jerk.health -= an_hero.weapon.attack
    print("{} attacks {} with {} for {} damage!".format(some_jerk.name, an_hero.name, some_jerk.weapon,
                                                        some_jerk.weapon.attack))
    an_hero.health -= some_jerk.weapon.attack
    print("{}'s health is {}.".format(an_hero.name, an_hero.health))
    print("{}'s health is {}.".format(some_jerk.name, some_jerk.health))
    print("---------------------")

    if an_hero.health <= 0:
        print("{} has deathed.".format(an_hero.name))

    if some_jerk.health <= 0:
        print("{} has deathed.".format(some_jerk.name))

def restore(donut):
    print("{} uses {} to gain {} healths!".format(an_hero.name, donut.name, donut.restore))
    an_hero.health += donut.restore
    print("{}'s health is {}.".format(an_hero.name, an_hero.health))
    print("--------------------")


an_hero = AnHero("An Hero")
some_jerk = BadGuy("Some Jerk")
some_jerk.health = 20

pointy_stick = Weapon("Mr. Pointy Stick", 4, "a tree")
better_dagger = Weapon("Better Dagger", 5, "the ground")

donut = Restorative("Box of Donuts")
donut.restore = 10


print("A challenger appears!")
print("---------------------")

print("{} is using {}.".format(an_hero.name, an_hero.weapon))
print("{} is using {}.".format(some_jerk.name, some_jerk.weapon))
print("---------------------")

fight(an_hero, some_jerk)
fight(an_hero, some_jerk)

print("{} picks up {} from {}.".format(some_jerk.name, pointy_stick.name, pointy_stick.location))
print("---------------------")
some_jerk.weapon = pointy_stick


restore(donut)
fight(an_hero, some_jerk)
fight(an_hero, some_jerk)
restore(donut)

print("{} picks up {} from {}.".format(an_hero.name, better_dagger.name, better_dagger.location))
print("---------------------")
an_hero.weapon = better_dagger

fight(an_hero, some_jerk)
fight(an_hero, some_jerk)

