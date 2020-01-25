import os
os.system("clear")

clothing_list = ["green","blue","grey","blue","blue","grey"]

clothing_set = set(clothing_list)

for element in clothing_list:
    print(element)

print("\n")

for element in clothing_set:
    print(element)
    #Hello, this is a comment?

print(clothing_list[0])
# print(clothing_set[0]) #this doesn't work

set_1 = {'a','b','c','d'}
set_2 = {'b','d'}

#to find the commmon elements in these sets, do this:
print(set_1.intersection(set_2))

#to put two sets together, but don't keep any duplicates?
print(set_1.union(set_2))