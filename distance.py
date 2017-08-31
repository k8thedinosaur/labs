convert = input("Enter the distance you would like to convert: ")

orig_unit = input("Enter the units (miles, feet, km, m): ")

to_unit = input("Enter the units you would like to convert to (miles, feet, km, m): ")

distance = int(convert)

if orig_unit == 'miles':
    if to_unit == 'km':
        answer = distance * 1.6
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'm':
        answer = distance * 1609.33
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'feet':
        answer = distance * 5280
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
#
if orig_unit == 'km':
    if to_unit == 'miles':
        answer = distance * 0.62
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'm':
        answer = distance * 1000
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'feet':
        answer = distance * 3280.83
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))

if orig_unit == 'm':
    if to_unit == 'km':
        answer = distance * 0.001
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'miles':
        answer = distance * 0.00062
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'feet':
        answer = distance * 3.28
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))

if orig_unit == 'feet':
    if to_unit == 'km':
        answer = distance * 0.0003
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'm':
        answer = distance * 0.3
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
    elif to_unit == 'miles':
        answer = distance * 0.00018
        print("{} {} converted to {} is {}".format(distance, orig_unit, to_unit, answer))
