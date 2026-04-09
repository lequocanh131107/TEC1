import requests

city = input("Nhap ten duong hoac thanh pho ik bro: ")

api_key = "a662f6b08cf75a0d6db88998b2753af0"

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=metric"

r = requests.get(url)

data = r.json()

weather = data["weather"][0]["description"]
temp = data["main"]["temp"]

print("Weather:", weather)
print("Temperature:", temp, "C")
print(data)