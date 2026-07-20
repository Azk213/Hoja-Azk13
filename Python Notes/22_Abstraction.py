from abc import ABC,abstractmethod #Importing Abstract Method (Vital Step)

class Animal(ABC): # Animal is Abstract class
    
    @abstractmethod
    def sound(self): # Sound is Abstract Method
        pass

class Dog(Animal): #Inherits sound
    def sound(self):
        return "Bark"# User only sees "Bark"

d = Dog()

print(d.sound())

class Payment(ABC): # Parent class is Abstract class
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment): 
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class Card(Payment):
    def pay(self,amount):
        print(f"Paid {amount} using Card")
    
#Two child classes inherit same abstact method

#ATM example with Abstraction
class ATM(ABC):
    @abstractmethod
    def withdraw():
        pass

class Bank(ATM):
    def __verify_pin(self):
        print("Verifying Pin...")
    
    def __check_balance(self):
        print("Checking Balance...")
    
    def __update_server(self):
        print("Updating Server...")
    
    def withdraw(self):
        self.__verify_pin()
        self.__check_balance
        self.__update_server

a = Bank()
a.withdraw()

#ATM example without Abstraction

class TheBank:
    def verify_pin(self):
        print("Verifying Pin...")
    
    def check_balance(self):
        print("Checking Balance...")
    
    def update_server(self):
        print("Updating Server...")
    
    def withdraw(self):
        print("Cash withdrawed succesfully.")

a2 = TheBank()         #All methods have to be called manually
a2.verify_pin()
a2.check_balance()
a2.update_server()
a2.withdraw()