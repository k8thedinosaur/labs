# Create a program that uses a dictionary to store phonebook entries. Must have user interaction.

# Integrate pretty printing phone number program as a function



phonebook = {
    "Kate": {"Name": "Kate Human", "Phone": "1111111"},
    "Murray": {"Name": "Murray Duck", "Phone": "2222222"},
    "Mushka": {"Name": "Mushka Goose", "Phone": "3333333"},
    "Tyler": {"Name": "Tyler Tiger", "Phone": "4444444"},
    "Jules": {"Name": "Jules Panther", "Phone": "5555555"}
}


def pretty_phone(add_number):
    map(int, add_number)
    part1 = add_number[0:3]
    part2 = add_number[3:6]
    part3 = add_number[6:10]
    return "({}) {}-{}".format(part1, part2, part3)

def catbook():
    while True:
        print("Welcome to the CatBook. What would you like to do? \n\
        0 - Display contacts \n\
        1 - Search contacts \n\
        2 - Add a contact \n\
        3 - Change a contact's information \n\
        4 - Delete a contact \n\
        5 - Close the phonebook")
        action = input("Enter your choice: ")

        # ***** 0. Display phonebook
        if action == "0":
            print(phonebook)

        # ***** 1. Search
        elif action == "1":
            query = input("What is the name of the cat you are looking for? ")

            print(phonebook[query]["Name"])
            print(phonebook[query]["Phone"])

        # ** 2. Add Entry
        # How to split first name from full name?
        # ~ make input into new mini-dictionary to insert into larger dictionary
        elif action == "2":
            add_name = input("What is the nickname of the cat you would like to add? ")
            full_name = input("What is the cat's full name? ")
            add_number = input("What is the cat's number? ")
            phonebook[add_name] = dict(Name=full_name, Phone=add_number)
            pretty_phone(add_number)
            print("{0} was added to the CatBook as {1} with the number: {2}".format(add_name, full_name, add_number))

        # *** 3. Change Entry
        elif action == "3":
            change = input("Which cat would you like to change? ")
            del phonebook[change]

            add_name = input("What is the cat's new nickname? ")
            full_name = input("What is the cat's full name? ")
            add_number = input("What is the cat's new number? ")
            phonebook[add_name] = dict(Name=full_name, Phone=add_number)
            print("{0} was changed in the CatBook to {1} with the number: {2}".format(add_name, full_name, add_number))

        # ***** 4. Delete Entry
        elif action == "4":
            delete = input("Which cat would you like to delete? (You monster.) ")
            del phonebook[delete]

        # ***** 5. Exit Program
        elif action == "5":
            print("You have closed the CatBook. Meow.")
            break


catbook()
