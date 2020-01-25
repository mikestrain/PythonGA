import random
import os
from pytime import pytime
os.system("clear")

deck = ["ten", "jack", "queen", "king", "ace"]

print("Printing the deck...")
for i in range(len(deck)):
    print(deck[i])

my_card = random.choice(deck)
print("The card you picked is", my_card)

print("\n")
print("Shuffling the deck...")
random.shuffle(deck)
print("Printing the deck...")
for i in range(len(deck)):
    print(deck[i])

def when_is_christmas():
    print("christmas is on",pytime.christmas())

