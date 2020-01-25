import requests
import os
os.system("clear")
# GET request - publically request information
# POST request - sending data securely

# PRODUCTION code is code that is embedded in a website and has to run by itself...

response = requests.get("http://www.google.com")
print(response)
# print(response.text)

# usually, response 200 is good
# usually, response 400 is bad.
# https://medium.com/@hanilim/http-codes-as-valentines-day-comics-8c03c805faa0

# API's are usually written in JSON or XML (JSON is much more readable!)


response = requests.get("http://api.open-notify.org/astros.json")
people_on_ISS = response.json()

for i in range(len(people_on_ISS['people'])):
    person = people_on_ISS['people'][i]['name']
    craft = people_on_ISS['people'][i]['craft']
    print(person,"is on board the",craft)



response = requests.get("http://api.giphy.com/v1/gifs/search?q=funny+cat&api_key=dc6zaTOxFJmzC")

