import os
os.system("clear")
# # You have a list of Disney characters and you want to find out if each of them contain i, o, or u in
# # their names. Loop through each character in the list and print out the following:

# If the name contains a "u," print out the name plus "U are so Uniquely U!"
# Otherwise if the name contains an "i," print out the name plus "I bet you're
# Impressively Intelligent!"
# Otherwise if the name contains an "o," print out the name plus "O My! How
# Original!"
# Otherwise, print the name plus "Ehh, a's and e's are so ordinary."

disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula",
"scar", "flotsam", "timon"]

for Name in disney_characters:
    print("\n")
    if "u" in Name.lower():
        print("U are so Uniquely U!")
    elif "i" in Name.lower():
        print(Name,"\nI bet you're Impressively Intelligent!")
    elif "o" in Name.lower():
        print("O My! How Original!")
    else:
        print(Name,"\nEhh, a's and e's are so ordinary.")



