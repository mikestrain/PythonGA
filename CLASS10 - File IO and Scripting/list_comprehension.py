import os
os.system("clear")

# [MODIFICATION    OLD LIST    CONDITION]

numbers_list = [1,2,3,4,5]
[(x-2) for x in numbers_list] # this is called a "lambda" or a quick way of writing something...

print(numbers_list)

list1 = [1,3,4,5,7,6,10]
print([x**2 for x in list1])
print(list1)

students = ["chuck", "mike", "matt", "tim", "eva", "adam"]
print([x for x in students if 't' in x])


#RANDOM FUNCTION can be included in the list comprehension
def add_to_string(random_string):
    return random_string + "!!!!"

print([add_to_string(x) for x in students])

# example: remove the numbers out of a string
my_string = '99 fantastic 13 hello2 world'
print([x for x in my_string if x not in '0123456789 '])


