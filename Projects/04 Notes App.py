choice = " "
notes = " "

file = open("Notes", "a")
file.close()


def write():
    global notes
    print("=====Notes=====")
    notes = input("Enter your notes:\n")

    file = open("Notes", "a") 
    file.write(notes + "\n")
    file.close()


def view():
    file = open("Notes", "r")
    print("\n=====Your Notes=====")
    print(file.read())
    file.close()


def main():
    global choice

    while True:
        print("\n=====Notes=====")
        print("1. Write new notes")
        print("2. View notes")
        print("3. Exit")

        choice = input("Enter your choice [1,2,3]: ")

        if choice == "1":
            write()
        elif choice == "2":
            view()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()