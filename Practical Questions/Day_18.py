print("________________________________________________________________________________")
#Question 1
num = float(input("Input number to be squared  : "))
try :
    print(num,"squared is :",num**2)
except ValueError:
    print("Enter a number")
print("________________________________________________________________________________")
#Question 2
num_1 = float(input("Input number 1 to be divided  : "))
num_2 = float(input("Input number 2 to be divided  : "))
try :
    print(num_1,"Divided by",num_2,"=",num_1/num_2)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter Numerical Values")
print("________________________________________________________________________________")
#Question 3
try:
    file = open(input("Enter file to be opened : "),"r")
except FileNotFoundError:
    print("File not found")
print("________________________________________________________________________________")
#Question 4
age = float(input("Enter your age : "))
if age < 0:
    raise ValueError("Age cannot be negative")
print("________________________________________________________________________________")
#Question 5
try:
    a = float(input("Enter first number : "))
    op = input("Enter operator [+,-,x,/]: ")
    b = float(input("Enter second number : "))
        
    if op == "+" :
        print(a,"+",b,"=",a+b)
    elif op == "-" :
        print(a,"-",b,"=",a+b)
    elif op == "x":
        print(a,"x",b,"=",a*b)
    elif op == "/":
        print(a,"/",b,"=",a/b)
    else :
        print("invalid operator")

except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Value Error(Use numbers and operators properly)")
else :
    print("Operation completed successfully")
finally:
    print("Program finished running,Thank you for using this calculator")
print("________________________________________________________________________________")
#Question 6
try:
    print(int(input("Enter number to be doubled : "))*2)
except ValueError:
    print("Use numbers")
else :
    print("No errors!Everthing went fine.")
print("________________________________________________________________________________")
#Question 7
print("Was done in Question 5 Calculator")
print("________________________________________________________________________________")
#Question 8
s = input("Enter number to turned into a integer : ")
try:
    print(int(s))
except ValueError:
    print("Write a number")
print("________________________________________________________________________________")
#Question 9
try:
    file = open(input("Enter file to be opened : "),"r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Operation completed")
print("________________________________________________________________________________")
#Question 10
withdrawed_amount =float(input("Enter the amount to be withdrawed"))
if withdrawed_amount > 5000 :
    print("Insufficient funds")
    