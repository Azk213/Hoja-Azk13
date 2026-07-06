import random
answer = 0
guess = 0
attempts = 6
menu =" "
def generate_number():
    global answer
    answer = random.randint(1, 100)

def get_guess():
    global guess
    guess = int(input("Guess a number between 1-100: "))

def check_guess():
    global status
    if guess == answer:
        print("You Win")
        return True
    elif guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    else :
        print("Invalid guess")
    return False

def play_game():
    global attempts
    attempts = 6
    generate_number()
    while attempts > 0:
        print("Attempt:",attempts,"Out of 6")
        get_guess()
        if check_guess():
            main()
            return
        attempts -= 1
    print("Ran out of attempts")
    print("Answer was ",answer)
    main()
        
        
def main():
    global menu
    print("1. Start number guessing game")
    print("2. Exit")
    menu =int(input("What's your choice 1/2 : "))
    if menu == 1:
        play_game()
    elif menu ==2:
        print("Thank you for playing")
    else:
        print("Invalid")

main()









    

    

    



    
    