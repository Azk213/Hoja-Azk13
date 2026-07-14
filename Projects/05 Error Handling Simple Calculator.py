a = 0 
b = 0
op = " "


def calculator(a,b,op):
    try:
        a = float(input("Enter first number : "))
        op = input("Enter operator [+,-,x,/]: ")
        b = float(input("Enter second number : "))
        
        if op == "+" :
            print(a,"+",b,"=",a+b)
        elif op == "-" :
            print(a,"-",b,"=",a+b)
        elif op == "x":
            print(a,"x",b,"=",a*b)
        elif op == "/":
            print(a,"/",b,"=",a/b)
        else :
            print("invalid operator")

    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("Value Error(Use numbers and operators properly)")
    else :
        print("Operation completed successfully!!!")
    finally:
        print("Program finished running,Thank you for using this calculator")

calculator(a,b,op)