# itertools is an easy way to do some things with lists:

import itertools

my_list = ["dog", "dog", "horse","horse","horse","dog"]
itertools.groupby(my_list)

for name,group in itertools.groupby(my_list):
    print(name)
    # print(group) -- need to explicitly convert to a list!
    print(list(group))

# this gives "dog" twice, because it's not in order in the list
# an easy way to fix this is "sorted"
print("\n")
for name,group in itertools.groupby(sorted(my_list)):
    print(name)
    # print(group) -- need to explicitly convert to a list!
    print(list(group))

print("\n\n\n")
things_tuple = [("animal", "wolf"), ("animal", "sparrow"), ("plant", "cactus"), ("vehicle", "yacht"), ("vehicle", "school bus"), ("vehicle", "car")]

def element_to_look_for(element):
    return(element[0])

for key, group in itertools.groupby(things_tuple,element_to_look_for):
    print(key,list(group))