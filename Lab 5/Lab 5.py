def main():
    while(True):
        operation = input("Please Select an Operation?")
        if operation.isalpha() == False:
            operation = int(operation)
            if operation < 8:
                break
            else:
                print("Input a number less than 8!")
        else:
            print("Input a number less than 8!")
    if operation == 1:
        addition(getData())
    elif operation == 2:
        subtraction(getData())
    elif operation == 3:
        multiply(getData())
    elif operation == 4:
        floatDiv(getData())
    elif operation == 5:
        intDiv(getData())
    elif operation == 6:
        mod(getData())
    elif operation == 7:
        exit()
    else:
        print("Invalid input!")

def getData():
    while(True):
        x = input("First #: ")
        y = input("Second #: ")
        if x.isalpha() == False and y.isalpha() == False:
            x = int(x)
            y = int(y)
            numbers = [x,y]
            break
        else:
            print("Input a number!")
    return numbers

def addition(x,y):
    z = x + y
    return z

def subtraction(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def floatDiv(x,y):
    z = x / y
    return z

def intDiv(x,y):
    z = x // y
    return z

def mod(x,y):
    z = x % y
    return z

