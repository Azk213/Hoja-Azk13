balance = 5000

def show_menu():
    print("===ATM===")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

def check_balance():   
    print("Current Balance:",balance)

def deposit():
    global balance
    amount = float(input("Enter your deposit amount: "))
    balance += amount
    print("Amount deposited successfully")
    print("Current Balance:",balance)
    
    

def withdraw():
    global balance
    withdrawed_amount =float(input("Enter the amount to be withdrawed"))
    if withdrawed_amount > balance :
        print("Insufficient funds")
        print("Current Balance:",balance)
    else :
        balance -= withdrawed_amount
        print(withdrawed_amount," Successfully withdrawed")
        print("Current Balance:",balance)


while True:
    show_menu()

    choice = input("Enter your choice(1,2,3,4):")
    if choice != int:
        print("Choose a numbered option")
    elif choice == 1: 
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        print("Thank you for using this ATM")
        break
    else :
        print("Invalid choice")
    
    

    



    
