import os
os.system("clear")

def arebotheven(num1, num2):

    if (num1%2 == 0) and (num2%2 == 0):
        return True
    else:
        return False

print(arebotheven(1, 4))
print(arebotheven(2, 4))
print(arebotheven(2, 3))

def viveks_function(a, b=10):  #to set a default argument, just use var="default input"
                                #however, DEFAULT arguments have to come after the non-default ones!!
    print("This is Vivek's function.")
    print("This function adds, subtracts, multiplies, and divides two numbers.")

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

    return a+b, a-b, a*b, a/b # as soon as the program sees a return, the function is done!
    b = b + 1000000           # this will not even run, since it's after the return!

A = input("What is the first number to be used? ")
B = input("What is the second number to be used? ")

l, m, n, o = viveks_function(float(A), float(B)) #this returns as a TUPLE!!

print(l,m,n,o)


data = [10, 45, 66, 55, 33, 45, 33]
def split_data(data):
    train_set = data [0:5]
    test_set = data[5:]
    return train_set, test_set

print(split_data(data))

first = split_data(data)[0]
second = split_data(data)[1]
print(first)
print(second)
