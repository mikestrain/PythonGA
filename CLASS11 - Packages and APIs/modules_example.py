# MODULES or PACKAGES

# a module is like a file
# a package is like a folder
# (from standard) import random

# from PACKAGE import MODULE
# pip install PACKAGE (call this line in terminal)


import itertools # this is easy, but slows down your code
from itertools import chain # you might just import one function to save load time

import random

mynumber = random.randint(3,200)
print(mynumber)

# example weibull distribution
# alpha is the scale parameter, beta is the shape parameter
weibull = random.weibullvariate(1.1,2.1)
print(weibull)

# example triangular distribution
for i in range(100):
    triangular = random.triangular(1,100,10)
    print(int(triangular))