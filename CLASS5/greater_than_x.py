#write a function that takes in a variable number of inputs
#and prints how many of them are greater than 50

import os
os.system("clear")

def greater_than_x(threshold,*args):
    counter = 0

    for i in args:
        if i>threshold:
            counter += 1

    return counter

howMany = greater_than_x(-1, 0, 100, 5)

print(howMany)