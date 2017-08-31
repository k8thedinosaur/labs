# digits = input("Please enter a phone number in all digits: ")
#
# map(int, digits)
#
# part1 = digits[0:3]
# part2 = digits[3:6]
# part3 = digits[6:10]
#
# print("({}) {}-{}".format(part1, part2, part3))
# # The clunky way:
# #  print("(" + part1+ ") " + part2 + "-" + part3)

def pretty_phone(add_number):
    map(int, add_number)
    part1 = add_number[0:3]
    part2 = add_number[3:6]
    part3 = add_number[6:10]
    print("({}) {}-{}".format(part1, part2, part3))


pretty_phone(input("Please enter a phone number in all digits: "))
