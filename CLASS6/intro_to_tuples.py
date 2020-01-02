import os
os.system("clear")

# this is a tuple, it cannot be changed
planets = ("earth", "mars", "venus")

# tuples are indexed like lists!
print(planets)
print(planets[2])

# you can also convert to sets or lists
print(set(planets))
print(list(planets))

seasons = ("fall", "winter", "spring", "summer")

for season in seasons:
    print(season)