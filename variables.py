# name = input("What is your name? ")
#
# number = 12345
# str_num = str(number)
#
# greeting = "Hello {}".format(name)
#
# print(greeting)

# number = 574542
# float_numb = 4823942.127841
#
# expo = 5**2
# mult = 5 * 5
# div = 5 / 5

# lst = ["I'm a string", 34, 3.14, [4, 5, 6]]
# lst.append("I'm on the end!")
# print(lst)
#
# lst[0] = "I am a string!"
#
# lst2 = lst[::]
# lst2[0] = 44
# print(lst)
# print(lst2)

# print(lst[::2])

# print(lst[-1])
# print(lst[3][2])

# removed_thing = lst.pop()
# print("You have popped {}".format(removed_thing))
# print(lst)

# my_list = ["cat", "dog", "monkey"]
# my_list[1] = ferret
# print(my_list)
#
# my_tuple = ("cat", ["4", "5", "6"], "ferret")
# my_tuple[1][1] = tortle
# print(my_tuple)

# for pet in my_list:
#     for char in pet:
#         print(char)
#     print()

# my_list = ["cat", "dog", "monkey"]
#
# num = 0
# while num < 10:
#     print("This is the song that never ends...")
#     num += 1
# print("It's over.")


name = input("What is your name? ")

if name == "Kate":
    print("Oh, it's you, {}.".format(name))
elif name == "Murray":
    print("{} is best cat.".format(name))
elif name == "Mushka":
    print("It's {}!".format(name))
