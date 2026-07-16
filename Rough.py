from random import randint

while 1:
    try:
        u=int(input("1.Rock\n2.Paper\n3.Scissor\n4.Exit\n>"))
        if u==4:break
        c=randint(1,3)
        print("CPU:",["Rock","Paper","Scissor"][c-1])
        print("You",["Lose","Win","Draw"][(u-c)%3])
    except:
        print("Invalid")