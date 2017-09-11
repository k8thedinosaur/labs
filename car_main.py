from car import Car

bus = Car("Bus", 4, 1, "covered in advertisements")

bike = Car("Bike", 2, 0, "snazzy green with fenders and cargo rack")

car = Car("Idk some car", 4, 4, "whatever color a car is who cares")

incomplete_car = Car("Incomplete car", 0, 3, "rusted as fuck and up on blocks")
# incomplete_car = Car.description("up on blocks")

print(bus)
print(bus.number_of_doors)
print(bike)
print(bike.number_of_wheels)
print(car)
print(incomplete_car)

print(bike.honk() * 3)
