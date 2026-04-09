import requests

url = "https://api.chucknorris.io/jokes/random"

r = requests.get(url)

data = r.json()

print(data["value"])