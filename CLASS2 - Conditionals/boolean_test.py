true_boolean = True
false_boolean = False

#mention of "truth tables"

my_int = 12
print(my_int == 5)
print(my_int >0)
print(my_int <0)
print(my_int * 5 > 0)

print(not my_int == 3)
print(my_int != 3)

print(False == "")
print(True == "a non empty string")
print(False == 0)
print("\n\n\n\n\n")

bread = "Thick"

if bread == "Thick":
    print("dunking the bread twice")

if my_int > 2 and my_int < 20:
    print("my integer is greater than 10 and less than 20")

if 20 > my_int > 2:
    print("my integer is greater than 10 and less than 20")

if my_int > 10 and my_int < 20 or my_int <0:
    print("hello?")

print("\n\n\n")

temperature = 30

if temperature >= 90:
    print("It's too damn hot!")
elif temperature >= 80:
    print("Wow, it's hot out here.")
else:
    print("Temperature is ok.")
