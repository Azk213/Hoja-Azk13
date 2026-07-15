print("________________________________________________________________________________")
#Question 1
class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        pass

class Dog(Animal):
    def bark(self):
        print(self.name,"is Barking")

a1 = Dog("K9")
a1.bark()
print("________________________________________________________________________________")
#Question 2
class Vehicle:
    def __init__(self,name):
        self.name = name
    
    def start(self):
        print(self.name,"is starting")
    
    def stop(self):
        print(self.name,"is stopping")

class Car(Vehicle):
    pass

c1 = Car("Audi R8")
c1.start()
c1.stop()
print("________________________________________________________________________________")
#Question 3
class Person:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print("Hello")

class Student(Person):
    def study(self):
        print(self.name,"is studying")

s1 = Student("Rahul")
s1.greet()
s1.study()
print("________________________________________________________________________________")
#Question 4
class BankAccount:
    def __init__(self,user,balance):
        self.user = user
        self.balance = balance
    
    def deposit(self):
        print(f"{self.user} is depositing {self.balance}.Rs")

class SavingsAccount(BankAccount):
    def interest(self):
        print("Interest is ",self.balance*0.25,"per year")
    
h1 = SavingsAccount("Rohit",23124)
h1.deposit()
h1.interest()
print("________________________________________________________________________________")
#Question 5
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        print(self.side**2)

sq1 =Square(23)
sq1.area()
print("________________________________________________________________________________")
#Question 6
class Mom:
    def cooking():
        print("Is cooking")

class Dad:
    def driving():
        print("Is driving")
        
class child(Dad,Mom):
    pass

child = child()
child.driving()
child.cooking()
print("________________________________________________________________________________")
#Question 7
class Grandfather:
    def work():
        print("Is working")
    
class Father(Grandfather):
    def teach():
        print("Is teaching")

class Son(Father):
    def play():
        print("Is playing")

son = Son()
son.work()
son.teach()
son.play()
print("________________________________________________________________________________")
#Question 8
class Bird:
    def fly():
        print("can fly")

class Penguin(Bird):
    def fly():
        print("cannot fly")

p1 = Penguin
p1.fly
print("________________________________________________________________________________")
#Question 9
class Employee:
    def __init__(self,salary):
        self.salary = salary
    
class Manager(Employee):
    def manage():
        print("Is managing")
print("________________________________________________________________________________")
#Question 10
class Device:
    def internet():
        print("using internet")

class Phone(Device):
    def call():
        print("Is calling")

class laptop():
    def code():
        print("Is coding")

