import requests

r = requests.get("http://api.icndb.com/jokes/random")

data = r.json()
print("Joke #{} is: {}".format(data["value"]["id"], data["value"]["joke"]))