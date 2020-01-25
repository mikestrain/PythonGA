import os       # https://stackoverflow.com/questions/18937058/clear-screen-in-shell/47296211
os.system('clear') # Clears the bash terminal automatically for you

list_name = [1,2,3,"string",False,3.4]
# print(list_name[0])

list_name_2 = [list_name, 5, 7]
print(list_name_2[0][1])

print(list_name[-1]) # you can start counting from the back by using negative numbers

print(list_name[0:2]) # this is to get multiple elements from a list, and the output is a list

print(list_name[0:-2]) # this gets all the numbers except the last two

print(list_name[0:5:2]) # this can increment the counting by two (odd numbers)

print(list_name[1::2]) # this works if you don't know the ending number

print(list_name[::2]) # this works if you're lazy and dont want to put in the zero

print(list_name[::-2]) # this REVERSES a list!

if "string" in list_name:
    print("this string is in the list")

print("Hello World"[::-1]) #strings act exactly like lists
print("Hello World"[::2]) #strings act exactly like lists

#INDEX is the method to get the position of something in a list
pos = list_name.index("string")
print("The position is",pos)

#LEN is the method to count the length
length = len(list_name_2)
print(length)

len("Hello World") # you can also count the letters in a string

#POP is the method to remove something from the list
list_name.pop(2)
print(list_name)

#APPEND is the method to add something to the list
list_name.append("hello world end of string")
print(list_name)