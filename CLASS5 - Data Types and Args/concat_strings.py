import os
os.system("clear")

def concat_strings(*args): #using the *args function allows you to include an unlimited amount of inputs

    output = ""
    for word in args:
        output = output + word

    print(output)

concat_strings("hello","world","how","are","you?")