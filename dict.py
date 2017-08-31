# name = "Kate"
# my_dict = {"key1": {"some": "thing"}, "key2": "value2"}
#
# print(my_dict)
#
# my_dict["key3"] = "value3"
#
# print(my_dict)

# prints
# {'key1': {'some': 'thing'}, 'key2': 'value2'}
# {'key1': {'some': 'thing'}, 'key2': 'value2', 'key3': 'value3'}


name = "Kate"
my_dict = {"key1": {"some": "thing"}, "key2": "value2"}

# print(my_dict)

my_dict["key3"] = "value3"

# print(my_dict)

my_dict["key3"] = "value4"

# print(my_dict)

# del my_dict["key3"]

# print(my_dict)

# print(my_dict.items())

for k, v in my_dict.items():
    print("Key is: {}".format(k))
    print("Value is: {}".format(v))
    print("~~~~~~~~~~~~~~~~~~~~~~~")

# prints thing

# students = {
#     "Watters": {"Name": "Kasey Watters", "Phone": 1111111},
#     "Magnuson": {"Name": "Tom Magnuson", "Phone": 2222222},
#     "Yeaney": {"Name": "Johnny Yeaney", "Phone": 3333333}
# }
#
# query = input("What is the last name of the student you are looking for? ")
#
# print(students[query]["Name"])
# print(students[query]["Phone"])
