# Write a function that returns the meal for any given hour of the day or night in respect to the following schedule:
# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM

# # What time is it?
# current_time = input("What time is it? ")
# 
# # Is it AM or PM?
# meridian = current_time[-2:]
# time = int(current_time[:-2])
# 
# # What are our meal times?
# if meridian.lower() == "am":
#     if time <= 7 and time <= 9:
#         print("{} is bacon time.".format(current_time))
#     elif time == 12 or time >= 1 and time <= 4:
#         print("{} is hammer time.".format(current_time))
#     else:
#         print("It is not eats time. Get back to work!")
# elif meridian.lower() == "pm":
#     if time == 12 or time == 1 or time == 2:
#         print("{} is sandwich time.".format(current_time))
#     elif time >= 7 and time <= 9:
#         print("{} is chicken time.".format(current_time))
#     elif time >= 10 and time <= 11:
#         print("{} is hammer time.".format(current_time))
#     else:
#         print("It is not eats time. Get back to work!")
# else:
#     print("It is not eats time. Get back to work!")
# 
# # return what meal it is


def hammer_time():
    current_time = input("What time is it? ")

    meridian = current_time[-2:]
    time = int(current_time[:-2])

    if meridian.lower() == "am":
        if time >= 7 and time <= 9:
            return "{} is bacon time.".format(current_time)
        elif time == 12 or time >= 1 and time <= 4:
            return "{} is hammer time.".format(current_time)
        else:
            return "It is not eats time. Go back to sleep!"
    elif meridian.lower() == "pm":
        if time == 12 or time == 1 or time == 2:
            return "{} is sandwich time.".format(current_time)
        elif time >= 7 and time <= 9:
            return "{} is chicken time.".format(current_time)
        elif time >= 10 and time <= 11:
            return "{} is hammer time.".format(current_time)
        else:
            return "It is not eats time. Get back to work!"
    else:
        return "It is not eats time. Get back to work!"


print(hammer_time())