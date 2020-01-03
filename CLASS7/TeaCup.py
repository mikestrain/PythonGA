import os
os.system("clear")

class TeaCup():
    def __init__(self, capacity, level=0):
        self.capacity = capacity
        self.level = level
        print("Making a teacup:\n")

    def fill(self):
        print("The cup is now full.")
        self.level = self.capacity
    
    def empty(self):
        print("The cup is now empty.")
        self.amount = 0
    
    def drink(self,amount_to_drink):
        if self.level < amount_to_drink:
            print("You've tried to drink too much tea!")
            TeaCup.empty(self)
        else:
            self.level -= amount_to_drink
            print("level is",self.level)
    

myCup1 = TeaCup(75)
myCup1.empty()
myCup1.fill()
myCup1.drink(100)
