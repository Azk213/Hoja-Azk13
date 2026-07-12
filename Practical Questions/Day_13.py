print("________________________________________________________________________________")
# Question 1
def greet():
    print("Hello")

greet()

print("________________________________________________________________________________")
# Question 2
name = input("What is your name? ")
def greet_user(name):
    print("Hello", name, "!")

greet_user(name)

print("________________________________________________________________________________")
# Question 3
a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
def add(a,b):
    print(a,b)
    print("Sum of", a, "and", b, "=", a + b)

add(a,b)
print("________________________________________________________________________________")
#Question 4
num = float(input("Input number"))
def check_even_odd(num):
    print(num)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(num)
print("________________________________________________________________________________")
#Question 5
def square(num):
     print(num)
     print(num**2)
square(num)
print("________________________________________________________________________________")
#Question 6
def find_max(a,b):
    print(a,b)
    if a > b:
        print(a,"is larger")
    elif b > a:
        print(b,"is larger")
    else:
        print(a,"and",b,"are equal")
print("________________________________________________________________________________")
#Question 7
num_list=[1,2,3,4,5]
print(num_list)
def sum_list(num_list):
    print(sum(num_list))
sum_list(num_list)
print("________________________________________________________________________________")
#Question 8

print("________________________________________________________________________________")
#Question 9
n = int(input("Enter number to be factorialed"))
def factorial(n):
    s =1
    for i in range(1,n+1):
        s = s * i
        print(s)
factorial(n)
print("________________________________________________________________________________")
#Question 10
text =" "
def reverse_string(text):
    text = input("Enter word to be reversed")
    print(text[::-1])
reverse_string(text)






 
    

    
    