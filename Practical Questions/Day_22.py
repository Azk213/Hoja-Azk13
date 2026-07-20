from abc import ABC,abstractmethod

print("________________________________________________________________________________")
#Question 1
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts")

car = Car()
car.start()
bike = Bike()
bike.start()

print("________________________________________________________________________________")
#Question 2
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        print('Payed with Card')

class UPIPayment(Payment):
    def pay(self):
        print("Payed with UPI")

card = CardPayment()
card.pay()
upi = UPIPayment()
upi.pay()

print("________________________________________________________________________________")
#Question 3
class Device(ABC):
    @abstractmethod
    def boot(self):
        pass

class Phone(Device):
    def __load_os(self):
        print("Loading Operating System...")
    
    def __check_hardware(self):
        print("Checking hardware...")
    
    def boot(self):
        self.__load_os
        self.__check_hardware

p = Phone
p.boot()

print("________________________________________________________________________________")
#Question 4
class ThePhone:
    def load_os():
        print('Loading Operating system')
    
    def check_hardware():
        print("Checking Hardware...")
    
    def boot():
        print("Booting")

ph = ThePhone()
ph.load_os()
ph.check_hardware()
ph.boot()
print("________________________________________________________________________________")
#Question 5
class Account(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingAccount(Account):
    def calculate_interest(self):
        print("Calculating Saving Account's Interest")

class CurrentAccount(Account):
    def calculate_interest(self):
        print("Calculating Current Account's Interest")

sa =SavingAccount()
ca = CurrentAccount()
sa.calculate_interest()
ca.calculate_interest()
print("________________________________________________________________________________")
#Question 6
class LoginSystem(ABC):

    def login(self):
        self.__verify_user()
        self.__check_password()
    
    def __verify_user(self):
        print("Verifying User...")
    
    def __check_password(self):
        print("Checking password")

l = LoginSystem()
l.login()
print("________________________________________________________________________________")
#Question 7
class CoffeeMachine(ABC):

    def make_coffee(self):
        self.__grind_beans()
        self.__heat_water()
        self.__brew()
    
    def __grind_beans(self):
        print("Grinding Beans...")

    def __heat_water(self):
        print("Heating Water...")
    
    def  __brew(self):
        print("Brewing Coffee...")

cm = CoffeeMachine()
cm.make_coffee
    
