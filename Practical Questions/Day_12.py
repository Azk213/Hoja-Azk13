print("_____________________________________________________________________________________________")
#Question 1
for i in range(1,101):
    print(i)
print("_____________________________________________________________________________________________")
#Question 2
for j in range(0,51,2):
    print(i)
print("_____________________________________________________________________________________________")
#Question 3
num = [1,2,3,4]
print(num)
print(sum(num))
print("_____________________________________________________________________________________________")
#Question 4
text = "hello"
vowels = "aeiou"
count = 0
for k in range(len(text)):
    for l in range(len(vowels)):
        if text[k].lower() == vowels[l]:
            count += 1
print(count)  
print("_____________________________________________________________________________________________")
#Question 5
num1 = int(input("Enter a number to be multiplied"))
for s in range(1,11):
    print(num1,"x",s,"=",num1*s)
print("_____________________________________________________________________________________________")
#Question 6
for p in range(1,6):
    print("*"*p,end=" \n")
print("_____________________________________________________________________________________________")
#Question 7
text1 = input("Enter word to be reversed")
reversed_text = text1[::-1]
print(reversed_text)   
print("_____________________________________________________________________________________________")
#Question 8
for n in range(1,101):
    if n % 3 == 0:
        print(n,"is divisible by 3 or 5")
    elif n % 5 == 0:
        print(n,"is divisible by 3 or 5")
print("_____________________________________________________________________________________________")
#Question 9
x = int(input("Enter a number between 1 and 50"))
while x != 31:
    x = int(input("Guess again"))

print("You guessed correct")
print("_____________________________________________________________________________________________")
#Question 10
num_list = [2,31,4,2,3,1,3,4,86]
print(num_list)
num2 = 0
for h in range(len(num_list)):
    if num2 < num_list[h]:
        num2 = num_list[h]
        print(num2)
        print(num_list[h])
        print(num2,"is smaller than",num_list[h])
    else:
        print(num2,"is bigger than",num_list[h])
