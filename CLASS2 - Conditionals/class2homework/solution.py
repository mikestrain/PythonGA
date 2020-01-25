#Mike Strain, General Assembly Python Class
#2019-12-8, Class 2 HW

# 2 beeps, 6 boops
# 0 beeps, 5 boops
# 9 beeps, 3 boops
# 4 beeps, 8 boops
# 10 beeps, 5 boops
# BOP!
# 11 beeps, 12 boops
# 5 beeps, 5 boops
# 1 beep, 17 boops
# 5 beeps, 7 boops
# 4 beeps, 0 boops

import os       # https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
os.system('clear') # Clears the bash terminal automatically for you

import winsound #https://stackoverflow.com/questions/6537481/python-making-a-beep-noise
fBeep = 1500    # Set Frequency for a beep
dBeep = 100     # Set Duration for a beep
fBoop = 1000    # Set Frequency for a boop
dBoop = 150     # Set Duration for a boop

Beeps = [2, 0, 9, 4, 10, 0, 11, 10, 1, 5, 4]
Boops = [6, 5, 3, 8, 5, 0, 12, 5, 17, 7, 0]

# Cycle through the amount of beeps and boops, playing sound and printing the letter.
for x in range(len(Beeps)):
    
    # Play the sound for each beep
    beeps = Beeps[x]
    for beep in range(beeps):
        winsound.Beep(fBeep,dBeep)
    
    # Play the sound for each boop
    boops = Boops[x]
    for boop in range(boops):
        winsound.Beep(fBoop,dBoop)
    
    # Add the beeps and boops together, and print the letter
    # If the total is zero, consider that a "BOP"
    total = beeps + boops
    if total == 0:
        print(" ", end='')
        winsound.Beep(500,1000)
    else:
        print(chr(96 + total), end='')

