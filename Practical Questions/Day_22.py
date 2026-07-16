print("________________________________________________________________________________")
#Question 1
class Car:
    def start():
        print("Car is starting...")

class Bike:
    def start():
        print("Bike is Starting...")

bike = Bike
bike.start()

car = Car
car.start()
print("________________________________________________________________________________")
#Question 2
class Animal:
    def sound():
        print("Animal Sounds...")
    
class Lion(Animal):
    def sound():
        print("Roars...")

class Elephant(Animal):
    def sound():
        print("Trumpets")

lion = Lion
lion.sound()

elephant = Elephant
elephant.sound()

print("________________________________________________________________________________")
#Question 3
def show_area(shape):
    shape.area()

class Square:
    def area(s):
        print("Area of Square : ",s * s)

class Circle:
    def area(s):
        print("Area of circle : ",3.14 * s ** 2)

square = Square(21)
show_area(square)

circle = Circle(12)
show_area(circle)

print("________________________________________________________________________________")
#Question 4
class EnglishGreeting:
    def greet():
        print("Hello")

class SpanishGreeting:
    def greet():
        print("Hola")

def greeter(s):
    s.greet()
 
hello = EnglishGreeting
greeter(hello)

hola = SpanishGreeting
greeter(hola)

print("________________________________________________________________________________")
#Question 5
string = "STRING"
print("Lenght of string : ",len(string))

list = [1,2,3,3,3,3,3,3,2,3,4]
print("Lenght of list : ",len(list))

tuple = (1,3,4,4,4,3,3,4,2,3)
print("Lenght of tuple : ",len(tuple))
print("________________________________________________________________________________")
#Question 6
class Laptop:
    def price():
        print("₹45,000/₹65,000")
    
class Buisness(Laptop):
    def price():
        print("₹80,000/₹1,20,000")

class Gaming(Laptop):
    def price():
        print("₹90,000/₹2,00,000")
print("________________________________________________________________________________")
#Question 7
class Dog:
    def speak():
        print("Barks....")

class Cat:
    def speak():
        print("Meows...")

class Cow:
    def speak():
        print("Moos...")

Animals = [Dog,Cat,Cow]
 
for animals in Animall:
    animals.speak

print("________________________________________________________________________________")
#Question 8
class Shape:
    def draw():
        print("Draws")

class Circle(Shape):
    def draw():
        print("Draws Circle")

class Triangle(Shape):
    def draw():
        print("Draws Triangle")

Shapes = [Shape,Circle,Triangle]
Shapes.draw()
print("________________________________________________________________________________")
#Question 6
class Apple:
    def show():
        print("Apple")

class Pear:
    def show():
        print("Pear")

def shows(x):
    x.show()

shows(Apple)
shows(Pear)
print("________________________________________________________________________________")
#Question 10
class PDFViewer:
    def open():
        print("PDF opened.")

class ImageViewer:
    def open():
        print("Image opened.")

PDF = PDFViewer
IMG = ImageViewer

PDF.open()
IMG.open()