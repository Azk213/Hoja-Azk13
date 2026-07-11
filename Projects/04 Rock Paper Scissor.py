import random
c_choice = 0
u_choice = 0 
def get_computer_choice():
    global c_choice
    c_choice = random.randit(1,3)

def get_player_choice():
    global u_choice
    u_choice = int(input("1.Rock 2. Paper 3.Scissor"))
    if u_choice == 0:
        print("Choose 1 or 2 or 3")
    elif u_choice > 3:
        print("Choose 1 or 2 or 3")

def check_winner()
    if u_choice == c_choice :
        print("Draw")
    elif u_choice =
        print("")


    