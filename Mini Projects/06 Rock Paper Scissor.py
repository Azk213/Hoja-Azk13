from random import randint

cpu = 0
user = 0
menu = 0

def get_cpu_choice():
    global cpu
    cpu = randint(1,3)

def get_user_choice():
    global user
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    try:
        user = int(input("Enter your choice (EX: 1,2,3) : "))
    except:
        print("Choose a Valid choice")
        get_user_choice()

def conversion(a):
    if a == 1:
        return "Rock"
    elif a == 2:
        return "Paper"
    elif a == 3:
        return "Scissor"

def check_winner():
    if user == cpu:
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
        print("Draw")
    elif user == 1 and cpu == 2:
        print("You Lost, CPU Wins")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
    elif user == 1 and cpu == 3:
        print("You Win, CPU Loses")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
    elif user == 2 and cpu == 1:
        print("You Won, CPU Loses")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
    elif user == 2 and cpu == 3:
        print("You Lost, CPU Wins")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
    elif user == 3 and cpu == 1:
        print("You Lose, CPU Wins")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))
    elif user == 3 and cpu == 2:
        print("You Win, CPU Loses")
        print("User chose", conversion(user), "and CPU chose", conversion(cpu))

def play_game():
    get_cpu_choice()
    get_user_choice()
    check_winner()

def main():
    while True:
        print("1. Start Rock Paper Scissor")
        print("2. Exit")
        menu = int(input("What's your choice 1/2 : "))

        if menu == 1:
            play_game()
        elif menu == 2:
            print("Thank you for playing")
            break
        else:
            print("Invalid")

main()

