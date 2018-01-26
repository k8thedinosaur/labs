import requests

def cn_joke():
    yn = "yes"

    while yn == "yes" or yn == "y":
        r = requests.get("http://api.icndb.com/jokes/random")

        data = r.json()
        print("Joke #{} is: {}".format(data["value"]["id"], data["value"]["joke"]))

        yn = input("Another? (y/n) ")
        # if yn == "y":
        #     # weather

        if yn == "no" or yn == "n":
            break


cn_joke()