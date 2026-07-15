print("________________________________________________________________________________")
#Question 1
class security:
    def __init__(self):
        self.public = "PUBLIC"
        self._protected = "PROTECTED"
        self.__private = "PRIVATE"

    def show(self):
        print(self.public)
        print(self._protected)
        print(self.__private)

print("________________________________________________________________________________")
#Question 2
class Student:
    def __init__(self,marks):
        self.__marks = marks
    
    def show(self):
        return print(self.__marks)
student = Student(123)
student.show()
print("________________________________________________________________________________")
#Question 3
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self):
        return print(self.__balance,"Deposited")
    
    def withdrawed(self):
        return print(self.__balance,"Wtihdrawed")
print("________________________________________________________________________________")
#Question 4
class Car:
    def __init__(self,speed):        
        self._speed = speed
    
    def access_speed(self):
        return print("Speed Increase from",self._speed)

car_1 = Car(21)
car_1.access_speed()
print("________________________________________________________________________________")
#Question 5
class Demo:
    def __init__(self,value):
        self.__value = value

    def show(self):
        print(self.__value)
        return print(self.__value)

print("________________________________________________________________________________")
#Question 6
class Example:
    def __secret():
        print("This is a secret")
    
    def show():
        pass
print("________________________________________________________________________________")
#Question 7
class Pass:
    def __init__(self,password):
        self.__password = password
    
    def check_password(self):
        return print(self.__password)
pass_1 = Pass("Password")
pass_1.check_password()
print("________________________________________________________________________________")
#Question 8
class Bonus:
    def _calculate_bonus():
        print("Calculating Bonus")
    
class Show_Bonus(Bonus):
    pass

bonus_1 = Show_Bonus()
bonus_1._calculate_bonus()
print("________________________________________________________________________________")
#Question 9
class Update:
    def __init__(self,value):
        self.__value = value
    
    def get(self):
        return print(self.__value)
    
    def set(self,name):
        self.name = name

s1 = Update("PRIVATE")
s1.get()
s1.set("NEW PRIVATE")
s1.get()
print("________________________________________________________________________________")
#Question 10
class ATM:
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self,deposit):
        self.__balance += deposit
    
    def withdraw(self,withdraw):
        if self.__balance  > withdraw :
            self.balance -= withdraw 
        else :
            print("Insufficient funds")
    
    def check_balance(self):
        return self.__balance
    
atm = ATM(1000)
print(atm.check_balance())
atm.deposit(int(input("Enter amount to be deposited : ")))
print(atm.check_balance())
atm.withdraw(int(input("Enter amount to be withdrawed : ")))
print(atm.check_balance())