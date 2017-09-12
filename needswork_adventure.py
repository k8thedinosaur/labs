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
# axe = Weapon("Axe of great hackings", 20)
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
        self.health = 20
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


class Restorative:
    def __init__(self, name, restore):
        self.name = name
        self.restore = restore

    def __str__(self):
        return self.name

