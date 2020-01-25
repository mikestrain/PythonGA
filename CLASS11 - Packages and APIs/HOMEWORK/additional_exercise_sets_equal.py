
import random
import os

os.system("clear")

list1 = ["a",",b","c","d","e","f","g"]
list2 = ["a",",b","c","d","e","f","g"]
random.shuffle(list2)

print(list1)
print(list2)

def lists_equal(L1,L2):
    S1 = set(L1)
    S2 = set(L2)
    if S1 == S2:
        return True
    else: return False

print(lists_equal(list1,list2))