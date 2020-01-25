import os
os.system("clear")



class Dog:
    #variables listed directly after this is a property of the class itself.
    #this is called a "class variable"
    total_dogs = 0

    # double underscore __init__ is a default property of a class
    # __add__ is another default function like this.
    # these __ functions exist whether or not we define them..

    # "self" is a keyword that must exist.
    # similar to "this" in javascript
    def __init__(self, age, breed='', color='black', size=12,owner = 'Mike', **kwargs):
        # self.properties = kwargs
        for k, v in kwargs.items():
            self.k = v
        self.breed = breed
        self.color = color
        self.size = size
        self.age = age
        self.owner = owner

        Dog.total_dogs += 1

    def bark(self):
        if Dog.total_dogs > 1:
            print("Dog is whispering...")
        print("Woof woof. My color is", self.color)

    def sit(self):
        print("I am now sitting. I am a good boy.")
        # if self.height:
            # print("the owner supplied my height!")
    
    def birthday(self):
        self.age += 1
        self.size += 2
    
    def new_owner(self,new_owner):
        self.owner = new_owner


dog1 = Dog(breed = 'lab', age = 10, height = 100)

#you can access the type of class that "dog1" is:
print(type(dog1))
    
dog1.bark()
dog1.sit()

dog2 = Dog('lab','white',10)
print(dog2.age)

# new dogs
dog3 = Dog(age = 2, breed = "dalmation", color = "white", size = 10)
dog3.birthday()
dog3.new_owner("John")

print(dog3.age)
print(dog3.size)
print(dog3.owner)
dog4 = Dog(age = 1)
dog4.bark()
dog5 = Dog(age = 1)
dog5.bark()

print("Total number of dogs is",Dog.total_dogs)