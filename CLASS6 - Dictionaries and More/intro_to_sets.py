import os
os.system("clear")

# SETS ARE LISTS WITH ONLY UNIQUE ELEMENTS

# [] is a list, or indexing
# {} is a set, or a dictionary
# () is a tuple

set1 = {"yellow", "red", "green", 'blue', 'yellow'}
print(set1) #automatically deletes duplicate elements!!

# set1[1]  this will not work because sets can't be indexed.. they are in any order.

# SETS ARE A REALLY GOOD WAY TO REMOVE DUPLICATES!
myfamily = ['mom', 'dad', 'madie', 'tony', 'mike', 'theresa', 'mike']
print(myfamily)

myfamily_remove_duplicates = list(set(myfamily))
print(myfamily_remove_duplicates)

myfamily_list = set(myfamily_remove_duplicates)

myfamily_list.add("cookie") # append will not work here, "add" is the only way to do it!
print(myfamily_list)

myfamily_list.remove("mike") # this is the equivalent of "pop" for lists
print(myfamily_list)
