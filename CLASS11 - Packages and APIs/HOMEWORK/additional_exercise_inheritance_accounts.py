import os
os.system("clear")

class BankAccount():

    # initiate the class variables
    interest_rate = 0.02

    # initiate the instance variables
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        if amount <=0: print("False. Please try again.")
        else: self.balance += amount
        # print("After deposit, your balance is $"+str(self.balance))
    
    def withdraw(self,amount):
        if amount <=0: print("False. Please try again.")
        else: self.balance -= amount
        # print("You have withdrawn ${} and your balance is ${}".format(amount,self.balance))
    
    def accumulate_interest(self):
        self.balance = self.balance*(1+self.interest_rate)

class ChildrensAccount(BankAccount):

    # initiate the class variables
    interest_rate = 0 # overwrite the original super class variable?
    interest_flat = 10

    # initiate the instance variables
    def __init__(self, balance=0):
        super().__init__(balance=balance)
    
    def accumulate_interest(self):
        self.balance += self.interest_flat
        
class OverdraftAccount(BankAccount):

    overdraft_penalty = 40

    def __init__(self, balance=0):
        super().__init__(balance=balance)
    
    def withdraw(self, amount):
        if amount >= self.balance:
            # print("___overdraft fee deducted___")
            self.balance -= self.overdraft_penalty
        else: self.balance -= amount
        # print("After deposit, your balance is $"+str(self.balance))

    def accumulate_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+self.interest_rate)

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print("\n")

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print("\n")

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))

