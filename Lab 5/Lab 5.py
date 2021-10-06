def main():
    while(True):
        print("+---------------------+")
        print("|  Python Calculator  |")
        print("+---------------------+")
        print("| 1. Addition         |")
        print("| 2. Subtraction      |")
        print("| 3. Multiplication   |")
        print("| 4. Float Division   |")
        print("| 5. Integer Division |")
        print("| 6. Modulus          |")
        print("| 7. Exit Program     |")
        print("+---------------------+\n")
        operation = input("Please Select an Operation: ")
        if operation.isalpha() == False:
            operation = int(operation)
            if operation < 8:
                break
            else:
                print("Input a number less than 8!")
        else:
            print("Input a number less than 8!")
    if operation == 1:
        addition(getData(1),getData(2))
    elif operation == 2:
        subtraction(getData(1),getData(2))
    elif operation == 3:
        multiply(getData(1),getData(2))
    elif operation == 4:
        floatDiv(getData(1),getData(2))
    elif operation == 5:
        intDiv(getData(1),getData(2))
    elif operation == 6:
        mod(getData(1),getData(2))
    elif operation == 7:
        exit()
    else:
        print("Invalid input!")

def addition(x,y):
    z = x + y
    return print(str(x) + " + " + str(y) + " = " + str(z))

def subtraction(x,y):
    z = x - y
    return print(str(x) + " - " + str(y) + " = " + str(z))

def multiply(x,y):
    z = x * y
    return print(str(x) + " * " + str(y) + " = " + str(z))

def floatDiv(x,y):
    z = x / y
    return print(str(x) + " / " + str(y) + " = " + str(z))

def intDiv(x,y):
    z = x // y
    return print(str(x) + " // " + str(y) + " = " + str(z))

def mod(x,y):
    z = x % y
    return print(str(x) + " % " + str(y) + " = " + str(z))


def getData(x):
    while(True):
        if x == 1:
            firstNumber = input("First number: ")
            if firstNumber.isalpha() == False and firstNumber != "":
                firstNumber = int(firstNumber)
                return firstNumber
            else:
                print("Please enter a number!")
        elif x == 2:
            secondNumber = input("Second number: ")
            if secondNumber.isalpha() == False and secondNumber != "":
                secondNumber = int(secondNumber)
                return secondNumber
            else:
                print("Please enter a number!")

main()
go = True
while go == True:
    run = input("Would you like to do another calculation? (y/n)")
    if run.isalpha() == True and run != "" and run == "y" or run == "Y":
        go = True
        main()
    elif run.isalpha() == True and run != "" and run == "n" or run == "N":
        go = False
    else:
        print("Please enter Y or N!")

