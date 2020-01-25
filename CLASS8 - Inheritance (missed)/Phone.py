import os
os.system("clear")

class Phone:

    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling from",self.number,"to", other_number)
    
    def text(self, other_number, msg):
        print("Texting from", self.number, "to", other_number)
        print(msg)


class iPhone(Phone):

    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, fingerprint):
        self.fingerprint = fingerprint
    
    def unlock(self, fingerprint=None):

        if self.fingerprint == None:
            print("phone unlocked. no fingerprint needed.")
        elif fingerprint == self.fingerprint:
            print("phone unlocked. fingerprint matches.")
        else:
            print("phone locked. fingerprint doesn't match.")
        
my_iphone = iPhone(151)
my_iphone.unlock()
my_iphone.set_fingerprint("Mike's fingerprint")
my_iphone.unlock
my_iphone.unlock("Mike's fingerprint")

my_iphone.call(4135059582)
my_iphone.text(4135059582, "hello!")