#scripting uses a scripted language as opposed to compiling, with a compiled language like C or Java

#QUESTION: why can't you open a .jpeg file in a text editor??

import os
os.system("clear")

my_file = open("new_text_file.txt") #open the file, by default in "read only"
print(my_file.read()) #read all the contents
my_file.close #close the file

#open(file_name, mode)
my_file = open("new_text_file.txt","w") #the letter implies that it's writable - but overwrites everything else by default!!
my_file.write("hello world") #this will overwrite everything else!!
my_file.close()

my_file = open("new_text_file.txt","w")
for i in range(1000):
    my_file.write(str(i)+"\n")
my_file.close()

# w = write
# a = append
# r = read
# r+ = read and write!

# WRITE will also create a file if none exists!
my_new_file = open("totally_new_file.txt","w")

a_file = open("a_file.txt")
file_contents = a_file.read()
b_file = open("b_file.txt","w")
b_file.write(file_contents)

a_file.close()
b_file.close()

# image = open("IMG_0604.jpg")
# image.read()

print("\n\n\n\n")
# THE "WITH" STATEMENT
with open("a_file.txt") as my_file:
    print(my_file.read())
    print("The file is not yet closed here.")

print("Now the file is closed automatically.")

# my_file.writelines(your list)
# new_list = my_file.readlines()