#Mike Strain, Python 6
#HW for class 9 and 10, Packages and APIs

import geocoder
import os
os.system("clear")

destinations = ["Space Needle","Crater Lake","Golden Gate Bridge",\
    "Yosemite National Park","Las Vegas Nevada","Grand Canyon National Park",\
        "Aspen, Colorado", "Mount Rushmore", "Yellowstone National Park",\
            "Sandpoint, Idaho", "Banff National Park", "Capilano Suspension Bridge"]

# g = geocoder.arcgis("Redlands, CA")
# print(g.latlng)

for destination in destinations:
    coordinates = geocoder.arcgis(destination).latlng
    print("{0} is located at the coordinates ({1},{2})".format(destination,coordinates[0],coordinates[1]))