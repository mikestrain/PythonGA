class Dog:
    # double underscore __init__ is a default property of a class
    # __add__ is another default function like this.
    # these __ functions exist whether or not we define them..

    # "self" is a keyword that must exist.
    # similar to "this" in javascript
    def __init__(self, breed='', color='black', size=12):
        self.breed = breed
        self.color = color
        self.size = size

    def bark(self):
        print("Woof woof. My color is", self.color)
