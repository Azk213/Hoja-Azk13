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
    def study(self)
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
        print(f"{self.name} is releasing , the tickets are only{self.tprice}")

movie_1 = Movie("MOVIE",100000)
movie_1.release()
print("________________________________________________________________________________")
# Class 5
class Game:
    def __inti__(self,name,price)
        self.name = name
        self.price = price
    def buy(self)
        print(f"(Purchase Successful)You bought {self.name} for {self.price}")

game_1 = Game("Hollow Knight",)