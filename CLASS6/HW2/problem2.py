import os
os.system("clear")
# The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When
# he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he
# sleeps! Write a conditional statement that selects one of the following actions for T-Rex based on
# his current mood. T-Rex's actions are ordered by precedence:

# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep.
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars.
# Otherwise T-Rex gives a toothy smile.

smile = r"""
       __
      /oo\
     |    |
 ^^  (vvvv)   ^^
 \\  /\__/\  //
  \\/      \//
   /        \        
  |          |    ^  
  /          \___/ | 
 (            )     |
  \----------/     /
    //    \\_____/
   W       W
"""

angry = True
bored = False
hungry = False
tired = False

if angry and hungry and bored: print("Triceratops gets eaten!")
elif tired and hungry: print("Iguandon gets eaten!")
elif tired: print("Trex is sleeping...")
elif angry and bored: print("Plan for velociraptor fight.")
elif angry or bored: print("ROARRRRRRRRRRRRRRRRRRRRRRRRR!!!!")
else: print(smile)