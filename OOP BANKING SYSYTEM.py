#Parent class
#Holds details about an user
#Has a function to show details
#Child Class :- bank
#Stores details about the account balance
#Store details about the amount
#Allows for deposits, withdrawls, check details and balance

#parent class

class user():
    def _init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details(self):
        print("Personal details")
        print("")
        print("Name:- ", self.name)
        print("Age:- ", self.age)
        print("Gender:- ", self.gender)

#Child class
class Bank(user):

    def _init__(self,name,age,gender):
        super()._init__(name,age,gender)
        self.balance=0
        
    def deposit(self,ammount):
        self.ammount=ammount
        self.balance=self.balance+self.ammount
        print("Your account balance has been updated.")
        print("Curent balance:- ", self.balance)

    def withdraw(self,ammount):
        self.ammount=ammount
        if self.ammount>self.balance:
            print("Insufficient funds| Balance Available = $", self.balance)
        else:
            self.balance=self.balance-self.ammount

    def view_balance(self):
        self.show_details()
        print("Account Details :- $", self.balance)
        



        
