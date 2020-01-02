import os
os.system("clear")

#Homework Assignment 2
#Wite a function that takes a name as input and creates a dictionary where the keys are unique
#letters from your name and the values associated with the keys are the number of times that letter
#appears in the name
#
#For example: makeDictionaryFromName(“vivek”) (edited)
#will return {“v”:2, “i”:1, “e”:1, “k”:1}



def name_dictionary(name):
    myName = {}
    for letter in name:

        try:
            myName[letter.upper()] = myName[letter.upper()] + 1
        except:
            myName[letter.upper()] = 1

    return myName

x = name_dictionary("Mmmmmmmike Strain")
print(x)