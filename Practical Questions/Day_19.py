#Question : Make 10 Classes
print("________________________________________________________________________________")
# Class 1
class Cars:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def turn_on(self):
        print(self.brand,self.model,"is turning on...")

car_1 = Cars("Audi","R8")
car_1.turn_on()
print("________________________________________________________________________________")

# Class 2
class Animal:
    def __init__(self,species,gender):
        self.species = species
        self.gender = gender

    def sleep(self):
        print(f"A {self.gender} {self.species} is sleeping")

animal_1 = Animal("Lion","Male")
animal_1.sleep()
print("________________________________________________________________________________")

# Class 3
class Student:
    def __init__(self,grade,name):
        self.grade = grade
        self.name = name

    def study(self):
        print(f"{self.name} from Grade{self.grade} is studying")
    
student_1 = Student(8,"NAME")
student_1.study()
print("________________________________________________________________________________")

# Class 4
class Movie:
    def __init__(self,name,tprice):
        self.name = name
        self.tprice = tprice

    def release(self):
        print(f"{self.name} is releasing , the tickets are only {self.tprice}")

movie_1 = Movie("MOVIE",100000)
movie_1.release()
print("________________________________________________________________________________")

# Class 5
class Game:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f"(Purchase Successful)You bought {self.name} for {self.price}")

game_1 = Game("Hollow Knight:Silksong",1664)
game_1.buy()
print("________________________________________________________________________________")

# Class 6
class Fruit:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f")You bought {self.name} for {self.price}")
    
fruit_1 = Fruit("Mango",10)
fruit_1.buy()
print("________________________________________________________________________________")

# Class 7
class Meat:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f")You bought {self.name} for {self.price}")

meat_1 = Meat("Chicken",100)
meat_1.buy()
print("________________________________________________________________________________")

# Class 8
class Toy:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f")You bought a {self.name} for {self.price}")

toy_1 = Toy("Rubix Cube",234)
toy_1.buy()
print("________________________________________________________________________________")

# Class 9
class Bottle:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def buy(self):
        print(f")You bought a {self.name} bottle for {self.price}")

bottle_1 = Bottle("Milton",542)
bottle_1.buy()
print("________________________________________________________________________________")

# Class 10
class Shirt:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def buy(self):
        print(f")You bought a {self.brand} Shirt for {self.price}")
    
shirt_1 = Shirt("Allen Soly",1000)
shirt_1.buy()
