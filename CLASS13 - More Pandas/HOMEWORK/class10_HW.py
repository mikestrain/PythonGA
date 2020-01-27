#Mike Strain, Python 6
#HW for class 9 and 10, Packages and APIs

import geocoder
import requests
import pprint
import os
os.system("clear")

destinations = ["Space Needle","Crater Lake","Golden Gate Bridge",\
    "Yosemite National Park","Las Vegas Nevada","Grand Canyon National Park",\
        "Aspen, Colorado", "Mount Rushmore", "Yellowstone National Park",\
            "Sandpoint, Idaho", "Banff National Park", "Capilano Suspension Bridge"]

myAPIkey = '57f783073f963119610af704068d47a5'
API_BASE_URL="https://api.darksky.net/forecast/{0}/".format(myAPIkey)

for destination in destinations:

    coordinates = geocoder.arcgis(destination).latlng
    lat = round(coordinates[0],2)
    lng = round(coordinates[1],2)
    print("{0} is located at the coordinates ({1},{2})".format(destination,lat,lng))

    full_api_url = API_BASE_URL + str(lat) + "," + str(lng)    
    result = requests.request('GET', full_api_url).json()
    # pprint.pprint(result["currently"])

    summary = result["currently"]['summary'].lower()
    temperature = round(result['currently']['apparentTemperature'],1)
    print("At {0} right now, it's {1} with a temperature of {2}{3}F.\n".format(destination, summary, temperature,u"\u00b0"))
