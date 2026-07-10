def odd_or_even(num):
    if num % 2 == 0:
        print(num,"is Even")
    else :
        print(num,"is Odd")
                
while True :
    num =int(input("Enter a number : "))
    if num == 0:
        break
    odd_or_even(num)
    
