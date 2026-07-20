from functools import reduce

print("________________________________________________________________________________")
#Question 1
def greet(name = "User"):
    print("Hello ",name)

greet(input("Enter your name : "))
print("________________________________________________________________________________")
#Question 2
def introduce(name,age,place):
    print(f"Hello {name} from {place}, You are {age}years old.")

name = input("Enter your name : ")
age = input("Enter your age : ")
place = input("Enter where you are from : ")
introduce(name,age,place)
print("________________________________________________________________________________")
#Question 3
def sum_all(*args):
    print(sum(args))

num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print(num)
sum_all(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
print("________________________________________________________________________________")
#Question 4
def show_profile(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print(name)
print(age)
print(place)
show_profile(name= name ,age = age ,place = place)
print("________________________________________________________________________________")
#Question 5
def show(name,age,place):
    return name,age,place

a,b,c = show(name,age,place)
print(a)
print(b)
print(c)
print("________________________________________________________________________________")
#Question 6
square = lambda x: x*x
square(int(input("Input number to be squared : ")))
print("________________________________________________________________________________")
#Question 7
num = [1,2,3,4,5,6,7,8,9,10]
print(num)
num_squared = list(map(lambda x: x*x ,num))
print(num_squared)
print("________________________________________________________________________________")
#Question 8
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num)
num_even = list(filter(lambda x : x % 2  == 0 , num))
print("________________________________________________________________________________")
#Question 9
num = [1,2,3,4,5]
print(num)
num_mulitplied =  reduce(lambda a,b : a*b  ,num)
print(num_mulitplied)
print("________________________________________________________________________________")
#Question 10
def decorator(func):
    def wrap():
        print("Start")
        func()
        print("End")
    return wrap

@decorator
def say_hello():
    print("Hello")

say_hello()

