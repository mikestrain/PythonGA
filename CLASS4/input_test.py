

import os
os.system('clear')

# user_name = input('please enter your name')

print("great!")

# num_students = input("enter number of students: ")
# print(type(num_students))
# print((float(num_students) + 5))

# USING THE "BREAK" FUNCTION
counter = 0
while True:
    counter += 1
    print('running your code...')
    if counter == 110:
        break

# USING THE "CONTINUE" FUNCTION
number = 0
print("\n")
for number in range(5):
    
    number += 1
    
    # skip the number 3 by using "continue"
    if number == 3:
        continue

    print("my number is ",number)
