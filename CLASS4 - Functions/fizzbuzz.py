import os
os.system('clear')

def what_to_print(input1, input2, text1, text2):

    for j in range(input1, input2):
        if j%3 == 0 and j%5 == 0:
            print(text1 + text2)
        
        elif j%5 == 0:
            print(text2)
        
        elif j%3 == 0:
            print(text1)
        
        else:
            print(j)


what_to_print(100, 200, "hello", "world")

def viveks_function(a, b):
    print("This is Vivek's function.")
    print("This function adds, subtracts, multiplies, and divides two numbers.")

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

A = input("What is the first number to be used? ")
B = input("What is the second number to be used? ")
viveks_function(float(A), float(B))

#what about outputs?
#what about optional arguments?
#what about try/catch?