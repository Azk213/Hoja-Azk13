from package import math_tools, string_tools, farewell, greet, converter
import random ,os
import datetime as dt
from math import sqrt,pow


print("________________________________________________________________________________")
# Question 1
radius = 12
print("Radius is", radius, "so area of the circle is", math_tools.areaofcircle_r(radius))

print("________________________________________________________________________________")
# Question 2
text = input("Enter a text: ")
print(string_tools.up(text))
print("________________________________________________________________________________")
# Question 3
print(random.randint(1,10))
print("________________________________________________________________________________")
# Question 4
num = int(input("Enter a Number : "))
print(num,"'s square root is ",sqrt(num))
exp = int(input("Enter a exponent"))
print(num," raised to ",exp," is ",pow(num,exp))
print("________________________________________________________________________________")
# Question 5
farewell.farewell()
greet.greet()
print("________________________________________________________________________________")
# Question 6
print(dt.datetime.now())
print("________________________________________________________________________________")
# Question 7
print(num)
print(exp)
print(num,"+",exp,"=",math_tools.add(num,exp))
print(num,"-",exp,"=",math_tools.sub(num,exp))
print("________________________________________________________________________________")
# Question 8
print(num)
print(math_tools.odd_or_even(num))
print("________________________________________________________________________________")
# Question 9
print(os.getcwd())
print("________________________________________________________________________________")
# Question 10
print(num,"KM")
print(exp,"Miles")
print(num,"KM is ",converter.km_to_miles(num),"Miles")
print(exp,"Miles is",converter.miles_to_km(exp),"KM")