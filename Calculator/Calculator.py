"""
CALCULATOR
Features:
- Basic Calculator (Addition , Subtraction , Multiplication , Division)
- Scientific Calculator (Factorial , Modulus , Power , Square Root , Average , Percentage)
- History (view and clear)
"""
# Function to calculate factorial
def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result
# Main Calculator  Program
print("==================================================")
print("--------------------CALCULATOR--------------------")
print("==================================================")
while True:
    # Main Menu
    print("1:- BASIC CALCULATOR\n2:- SCIENTIFIC CALCULATOR\n3:-HISTORY\n4:- EXIT")
    while True:
        try:
            Choose = int(input("Enter Your Choice:--"))
            break
        except ValueError:
            print("Enter Valid Value:-")
    # Basic Calculator
    if (Choose==1):
        print("You choose Basic Calculator")
        while True:
            try:
                num1 = float(input("Enter Number:  "))
                break
            except ValueError:
                print("Enter Valid Value:-")
        result=num1
        f = open("History.txt", "a")
        f.write(f"{num1}")
        f.close()
        print("Addition '+' Subtraction '-' Multiplication '*' Division '/'")
        while True:
            operation = input("Enter Operation:  ")

            if (operation == "+"):
                while True:
                    try:
                        num2 = float(input("Enter Number:  "))
                        break
                    except ValueError:
                        print("Enter Valid Value")
                f = open("History.txt", "a")
                f.write(f" + {num2}")
                f.close()
                result = result + num2
            elif (operation == "-"):
                while True:
                    try:
                        num2 = float(input("Enter Number:  "))
                        break
                    except ValueError:
                        print("Enter Valid Value")
                f = open("History.txt", "a")
                f.write(f" - {num2}")
                f.close()
                result = result - num2
            elif (operation == "*"):
                while True:
                    try:
                        num2 = float(input("Enter Number:  "))
                        break
                    except ValueError:
                        print("Enter Valid Value")
                f = open("History.txt", "a")
                f.write(f" * {num2}")
                f.close()
                result = result * num2
            elif (operation == "/"):
                while True:
                    try:
                        num2 = float(input("Enter Number:  "))
                        break
                    except ValueError:
                        print("Enter Valid Value")
                if (num2 != 0):
                    f = open("History.txt", "a")
                    f.write(f" / {num2}")
                    f.close()
                    result = result / num2
                else:
                    print("Division by 0")
                    f = open("History.txt", "a")
                    f.write(f" / {num2} = Undefined\n")
                    f.close()
                    break

            elif (operation=="="):
                f = open("History.txt", "a")
                f.write(f" = {result}\n")
                f.close()
                print(result)
                break
            else:
                print("Enter Valid Operation")
    # Scientific Calculator
    elif (Choose==2):
        print("You choose Scientific Calculator")
        while True:
            try:
                num1=int(input("Enter Number:  "))
                break
            except ValueError:
                print("Enter integer Value")
        print("Factorial '!'  Modulus '%'  Power '^'  Square Root '>'  Average '<' Percentage'?'")
        operation=input("Enter Operation:  ")
        if (operation=="!"):
            if (num1>=0):
                result = factorial(num1)
            else:
                print("Enter non-negative number.")
                result="Invalid"
            f = open("History.txt", "a")
            f.write(f"{num1} ! ")
            f.close()
        elif (operation=="%"):
            while True:
                try:
                    num2 = int(input("Enter Number:  "))
                    break
                except ValueError:
                    print("Enter Valid Value")
            if (num2==0):
                print("Not defined")
                result="Invalid"
            else:
                result = num1 % num2
            f = open("History.txt", "a")
            f.write(f"{num1} % {num2} ")
            f.close()
        elif (operation=="^"):
            while True:
                try:
                    num2 = int(input("Enter Number:  "))
                    break
                except ValueError:
                    print("Enter Valid Value")
            result=pow(num1,num2)
            f = open("History.txt", "a")
            f.write(f"{num1} ^ {num2} ")
            f.close()
        elif (operation==">"):
            if(num1>=0):
                result = num1 ** 0.5
            else:
                print("Enter non-negative number")
                result="Invalid"
            f = open("History.txt", "a")
            f.write(f"sqrt({num1}) ")
            f.close()
        elif (operation=="<"):
            print("Write any character except integer to tell that you are done with entering.")
            total=num1
            count=1
            f = open("History.txt", "a")
            f.write(f"{num1} ")
            f.close()
            while True:
                try:
                    A=int(input("Enter Value:  "))
                    total=total+A
                    count=count+1
                    f = open("History.txt", "a")
                    f.write(f" , {A}")
                    f.close()
                except ValueError:
                    break
            result=total/count
            f = open("History.txt", "a")
            f.write(f" Average ")
            f.close()
        elif (operation=="?"):
            while True:
                try:
                    num2=int(input("Enter Percentage value:  "))
                    break
                except ValueError:
                    print("Enter Valid Value")
            result=num1*(num2/100)
            f = open("History.txt", "a")
            f.write(f"{num2} percent of {num1} ")
            f.close()
        else:
            print("Type valid operation")
            result="Invalid"
        print(result)
        f = open("History.txt", "a")
        f.write(f"= {result}\n")
        f.close()
    # History : View or Clear
    elif (Choose==3):
        print("Choose 1 to view History , Choose 2 to clear History")
        while True:
            try:
                choice=int(input("Enter your choice:- "))
                break
            except ValueError:
                print("Enter valid value")
        if(choice==1):
            L=[]
            f = open("History.txt", "r")
            for lines in f:
                L.append(lines)
            f.close()
            for i in L:
                print(i,end="")
        elif(choice==2):
            f = open("History.txt", "w")
            f.write(f" ")
            f.close()
        else:
            print("Enter valid value")
    # Exit the program
    elif (Choose==4):
        print("THANK YOU FOR USING THIS CALCULATOR")
        break
