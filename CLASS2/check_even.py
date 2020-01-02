number = 0
remainder = number % 2

if remainder == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("\n\n\n")

x = 8
y = 0
a = "Hello"
b = "test"

if x and b:
    print("Both of these are true.")

if not y or not a:
    print("One of these is false.")
if x or y == False:
    print("Another one of these is false")
    if x > y:
        print("x is greater than y.")