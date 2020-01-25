
import os
os.system("clear")

def print_names(town, **kwargs):
    print("The name of the town is",town)

    for person, age in kwargs.items():
        #here we are naming each keyword "person"
        #and we are naming each input "age"
        #that way we can pair a keyword to a person
        print(person, "'s age is", int(age))

print_names("west springfield",mom = 70,dad = 64, madie = 14)
