import os
os.system("clear")

# create a list with names of at least 5 people

list = ['Mike','Chuck','Matt','Eva','Tim', 'Anthony']

for classmate_name in list:
    if 'a' in classmate_name.lower():
        print("Hello,",classmate_name +'!')

for classmate_name in list[0:4]:
    for character in classmate_name:
        print(character)
    print('\n')

for number in range(len(list)):
    print(list[number].upper())

days = ["mon","tue",'wed','thu','fri']
dates = [11,12,13,14,15]

for num in range(len(days)):
    print("Today is " + days[num] + " the " + str(dates[num]) + "th.")

#TO DO THIS AS A MATRIX (or a list of lists!!)
print('\n')
date_matrix = [["mon","tue",'wed','thu','fri'],[11,12,13,14,15]]

for i  in range(len(date_matrix[0])):
    print("Today is " + date_matrix[0][i] + " the " + str(date_matrix[1][num]) + "th.")