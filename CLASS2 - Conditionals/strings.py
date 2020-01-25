print("This is a string \n this is another line") #this is an "escape character"

print("5" * 5)
# print("5" + 5) this will throw an error

#how to access variables like MATLAB?
#how to make a literal string without any escape characters
first_string = "some text"

print(first_string[7])

print("5"+"4\n")

firstNumber = "5"
secondNumber = "4"
print(int(firstNumber) + int(secondNumber))

firstNumber = "5.564"
secondNumber = "4"
print(float(firstNumber) + float(secondNumber))

print("this" + "is a string")
print("this","is a string\n")

print()
print()

my_num = 5
my_string = "string"
my_num = str(my_num)
print(my_num+my_string)