import os       # https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
os.system('clear') # Clears the bash terminal automatically for you

import numpy as np

countHeads = 0
countTails = 0
tosses = 0
headsLimit = 50

while countHeads < headsLimit:
    Results = np.random.random() > 0.5
    tosses += 1

    if Results == True:
        countHeads += 1
        print("Heads!")
    else:
        countTails += 1
        print("Tails!")
    
print("Reached", headsLimit, "heads in", tosses, " tosses.")