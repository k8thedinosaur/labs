# # Lab: PyWeather
#
# Create a program that will prompt a user for city name or zip code.
# Use that information to get the current weather. Display that information
# to the user in a clean way.
# ## Advanced
#
# * Also ask the user if they would like to see the results in C or F.

import requests

package = {
    "APPID": "848e9a71a4b1c90877841baf319c1b68",
}

# K to F conversion
def k_to_f(temp):
    ans = temp * 9/5 - 459.67
    ans = int(ans)
    return ans

def k_to_c(temp):
    ans = temp - 273.15
    ans = int(ans)
    return ans

def get_weather():
    # ask city or zip
    city_zip = input("Would you like to search by (city) or (zip)? ")

    # conditional loop for either instance
    # if city ...
    if city_zip == "city":
        city_name = input("Enter your city: ")
        package["q"] = city_name
        # pull from api and write params to local dictionary package
        r = requests.post("http://api.openweathermap.org/data/2.5/weather", params=package)
        # convert from js object to python dict or maybe the other way around idk
        data = r.json()
        # pull temp data from package
        temp = (data["main"]["temp"])
        area = (data["name"])

        # give option to display in different units
        units = input("Would you like it displayed in (K), (C), or (F)? ")
        if units == "F":
            # apply k to f and display
            print("It is {} degrees F in {}.".format(k_to_f(temp), area))
            # apply k to c
        elif units == "C":
            print("It is {} degrees C in {}.".format(k_to_c(temp), area))
            # default is k
        else:
            print("It is {} degrees K in {}.".format(int(temp), area))

    # if zip ...
    elif city_zip == "zip":
        zipcode = input("Enter your zipcode: ")
        package["zip"] = zipcode
        r = requests.post("http://api.openweathermap.org/data/2.5/weather", params=package)
        data = r.json()
        temp = (data["main"]["temp"])
        units = input("Would you like it displayed in (K), (C), or (F)? ")
        if units == "F":
            print("It is {} degrees F in {}.".format(k_to_f(temp), zipcode))
        elif units == "C":
            print("It is {} degrees C in {}.".format(k_to_c(temp), zipcode))
        else:
            print("It is {} degrees K in {}.".format(int(temp), zipcode))
    else:
        print("Invalid response.")
get_weather()
