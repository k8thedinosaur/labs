class Car:
    def __init__(self, name, number_of_wheels, number_of_doors, color):
        self.name = name
        self.number_of_wheels = str(number_of_wheels)
        self.number_of_doors = str(number_of_doors)
        self.color = color
        # self.description = None

    def __str__(self):
        return "A {} has {} wheels, {} doors, and is {}.".format(self.name, self.number_of_wheels, self.number_of_doors, self.color)


    def honk(Car):
        return "Boop. "
