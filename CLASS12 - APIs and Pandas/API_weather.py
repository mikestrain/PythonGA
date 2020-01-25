import requests
import os
import pprint

os.system("clear")

zip_or_city = input('what is your zip code or city?')
key = '052f26926ae9784c2d677ca7bc5dec98'

print("http://api.openweathermap.org/data/2.5/weather?zip="+zip_or_city+",us&appid="+key)
try:
    int(zip_or_city)
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zip_or_city+",us&appid="+key)
except:
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+zip_or_city+"&appid="+key)

weather = response.json()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(weather)

# print(weather)

temp_K = weather['main']['temp']

temp_C = temp_K - 273
temp_F = ((9/5) * temp_C) + 32

print(temp_F)

