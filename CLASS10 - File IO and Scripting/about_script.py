
my_name = input("What is your name?")
my_food = input("What is your favorite food?")

with open("about_me.txt","w") as about_me:
# about_me.write(my_name+"\n")
# about_me.write(my_food)

    my_stats = [my_name, my_food]
    about_me.writelines(my_stats)
    # print(type(my_stats))

# about_me.close()
# https://stackoverflow.com/questions/12377473/python-write-versus-writelines-and-concatenated-strings

with open("IMG_0604.jpg","rb") as my_image: # RB reads the file as a raw binary file, not expecting text!!
    print(my_image.read())
