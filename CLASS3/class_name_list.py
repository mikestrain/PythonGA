# 1. DECLARE A LIST WITH THE NAMES OF YOUR CLASSMATES
# [6:05 PM]
# 2. PRINT OUT THE LENGTH OF THAT LIST
# [6:05 PM]
# 3. PRINT THE 3RD NAME ON THE LIST
# [6:05 PM]
# 4. DELETE THE FIRST NAME ON THE LIST
# [6:05 PM]
# 5. RE-ADD THE NAME YOU DELETED TO THE END OF THE LIST

import os
os.system("clear")

python_class = ["Mike", "Tim", "Eva", "Adam", "Chuck", "Matt"]
print(len(python_class))
print(python_class[2])
x = python_class.pop(0)
python_class.append(x)
print(python_class)

python_class.insert(3,"NEW MEMBER")
print(python_class)

# this is how to change the place of something in a list
take_out = python_class.pop(3)
python_class.insert(0,take_out)
print(python_class)

# reverse the list
python_class = python_class[::-1]
print(python_class)

# sort the list in alphabetical order
python_class.sort()
print(python_class)

# sort the list in reverse
python_class.sort()
python_class = python_class[::-1]
print(python_class)

#OR
python_class.sort(reverse = True)
print(python_class)


print(u'\d248')