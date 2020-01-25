

#MAKING A LIST
fav_foods_list = ['pizza', 'pad thai', 'sushi', 'tacos']
fav_foods_list.insert(0,'pizza')
fav_foods_list.append('eggs')
fav_foods_list.pop(0)
fav_foods_list[1] = 'popcorn'
removed_element = fav_foods_list.pop(2)
fav_foods_list.insert(0,removed_element)
print(fav_foods_list[0])

for item in fav_foods_list:
    print(item)
print(type(fav_foods_list))

print("\n")
#MAKING A SET
fav_foods_set = set(fav_foods_list)
fav_foods_set.add("pizza") # doesn't do anything because it's a duplicate
fav_foods_set.add('eggs') #can't specify adding to the end
fav_foods_set.remove("pizza")
# can't reassign element 1, since it's not in order
# can't change order
# can't print the first element

for item in fav_foods_set:
    print(item)
print(type(fav_foods_set))

print("\n")
#MAKING A TUPLE
fav_foods_tuple = tuple(fav_foods_list)
# can't do any change whatsoever
print(fav_foods_tuple[0])

for item in fav_foods_tuple:
    print(item)
print(type(fav_foods_tuple))