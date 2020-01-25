# YOU CAN USE "ITERTOOLS.CHAIN" TO CHAIN TOGETHER DIFFERENT DATA TYPES OR LISTS
import itertools
colors = ["red", "green", "yellow", "blue"]
hobbies = {"baseball":"a fun sport","programming":"a great endeavor","model rockets":"a dangerous hobby"}
numbers = [1, 2, 3, 4, 5, 6]
my_list = list(itertools.chain(colors,hobbies,numbers))
print(my_list)

print(type(my_list[8]))