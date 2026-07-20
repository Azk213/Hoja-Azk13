from abc import ABC, abstractmethod

print("________________________________________________________________________________")
# Question 1
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
# Question 2
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CardPayment(Payment):
    def pay(self):
        print("Payed with Card")

class UPIPayment(Payment):
    def pay(self):
        print("Payed with UPI")

card = CardPayment()
card.pay()
upi = UPIPayment()
upi.pay()

print("________________________________________________________________________________")
# Question 3
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
        self.__load_os()
        self.__check_hardware()

p = Phone()
p.boot()

print("________________________________________________________________________________")
# Question 4
class ThePhone:
    def load_os(self):
        print("Loading Operating system")

    def check_hardware(self):
        print("Checking Hardware...")

    def boot(self):
        print("Booting")

ph = ThePhone()
ph.load_os()
ph.check_hardware()
ph.boot()

print("________________________________________________________________________________")
# Question 5
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

sa = SavingAccount()
ca = CurrentAccount()
sa.calculate_interest()
ca.calculate_interest()

print("________________________________________________________________________________")
# Question 6
class LoginSystem(ABC):
    @abstractmethod
    def login(self):
        pass

class UserLogin(LoginSystem):
    def login(self):
        self.__verify_user()
        self.__check_password()

    def __verify_user(self):
        print("Verifying User...")

    def __check_password(self):
        print("Checking password")

l = UserLogin()
l.login()

print("________________________________________________________________________________")
# Question 7
class CoffeeMachine:

    def make_coffee(self):
        self.__grind_beans()
        self.__heat_water()
        self.__brew()

    def __grind_beans(self):
        print("Grinding Beans...")

    def __heat_water(self):
        print("Heating Water...")

    def __brew(self):
        print("Brewing Coffee...")

cm = CoffeeMachine()
cm.make_coffee()

print("________________________________________________________________________________")
# Question 8
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

class Triangle(Shape):
    def area(self):
        print("Area of Triangle")

class Circle(Shape):
    def area(self):
        print("Area of Circle")

s = Square()
s.area()
c = Circle()
c.area()
t = Triangle()
t.area()

print("________________________________________________________________________________")
# Question 9
class ReportGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class Report(ReportGenerator):

    def generate(self):
        self.__gather()
        self.__compile()

    def __gather(self):
        print("Gathering Info...")

    def __compile(self):
        print("Compiling Info...")

r = Report()
r.generate()

print("________________________________________________________________________________")
# Question 10
class Car:

    def check_fuel(self):
        print("Checking Fuel Amounts...")

    def check_engine(self):
        print("Checking Engine Function...")

    def check_coolant(self):
        print("Checking Coolant Amounts...")

    def start(self):
        print("Car is starting")

c = Car()
c.check_fuel()
c.check_engine()
c.check_coolant()
print("Did not call start")
