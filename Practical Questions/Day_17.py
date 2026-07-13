import os
print("_____________________________________________________________________________________________")
# Question 1
file = open("name","w")
file.write(input("Enter your name : "))
file.close()
print("_____________________________________________________________________________________________")
# Question 2
file = open("movies","w+")
file.write("Up\nCars\nLion king")
print(file.readlines())
file.close()
print("_____________________________________________________________________________________________")
# Question 3
file.open("poem","a+")
file.write("The sun doth fade behind the gray")
print(file.readlines())
file.write("Cold shadows steal the light away")
print(file.readlines())
file.write("Each passing hour grows bleak and still")
print(file.readlines())
file.write("And silence bends to sorrows will")
print(file.readlines())
print("_____________________________________________________________________________________________")
# Question 4
print(file.readline())
file.close()
print("_____________________________________________________________________________________________")
# Question 5
file = open("TO DO","a")
file.write(input("Enter your tasksa : "))
print("_____________________________________________________________________________________________")
# Question 6
file =open("poem","r")
print(file.readlines())
lines =file.readlines()
print(len(lines))
file.close()
print("_____________________________________________________________________________________________")
# Question 7
with open("poem", "r") as file:
    words = file.read().split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
print("_____________________________________________________________________________________________")
# Question 8
try:
    with open("random","r") as file:
        file.read()
except FileNotFoundError:
    print("FIle not Found")
    print("_____________________________________________________________________________________________")
# Question 9
with open("poem","r") as file:
    copy = file.readline()
    print(copy)
file =open("copy","w")
file.write(copy)
print(copy)
print("_____________________________________________________________________________________________")
# Question 10
confirmation = input("Are u sure you want to remove all files?[yes,no] : ")
if confirmation.lower() == "yes":
    os.remove("name")
    os.remove("movies")
    os.remove("poem")
    os.remove("copy")
    os.remove("TO DO")
    print("Successfuly removed all files")
elif confirmation.lower() == "no":
    print("ok")
else :
    print("Invalid Choice")