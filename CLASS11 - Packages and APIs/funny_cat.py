import requests
import os
import pprint
os.system("clear")

response = requests.get("http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC")

list_GIFS = response.json()
for i in range(len(list_GIFS["data"])):
    print(list_GIFS["data"][i]['url'])

kw = input("pick a keyword:")
response = requests.get("http://api.giphy.com/v1/gifs/search?q="+kw+"&api_key=dc6zaTOxFJmzC")

list_GIFS = response.json()
for i in range(len(list_GIFS["data"])):
    print(list_GIFS["data"][i]['url'])



# print(list_GIFS)