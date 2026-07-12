print("________________________________________________________________________________")
#Question 1
num =(int)(input("Enter a number: "))
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
print("________________________________________________________________________________")
#Question 2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to apply")
else :
    print("You are too young to apply")
print("________________________________________________________________________________")
#Question 3
time = int(input("Enter your time: "))
if time <= 12 :
    print("Good Morning")
else :
    print("Good Evening")
print("________________________________________________________________________________")
#Question 5
Grade = int(input("Enter your Grade: "))
if Grade >= 90:
    print("A")
elif Grade >= 70:
    print("B")
elif Grade >= 50:
    print("C")
else :
    print("Fail")
print("________________________________________________________________________________")
#Question 5
num1 = int(input("Enter a number: "))
if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")
print("________________________________________________________________________________")
#Question 6
age2 = int(input("Enter your age: "))
if age2 <= 5 :
    print("You're ticket is free!")
elif age2 <= 18 :
    print("You're ticket is 50 rupeees")
else :
    print("You're ticket is 100 rupeees")