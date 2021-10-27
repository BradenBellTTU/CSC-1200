from time import sleep
def menu():
    print("+---------------------------------------+")
    print("| Welcome to the Python Vending Machine |")
    print("+---------------------------------------+")
    print("|                 Menu                  |")
    print("+---------------------------------------+")
    print("|        1.) KitKat             | $1.50 |")
    print("|        2.) Snickers           | $1.50 |")
    print("|        3.) Dr. Pepper         | $1.00 |")
    print("|        4.) Cheetos            | $1.00 |")
    print("|        5.) Starbursts         | $1.25 |")
    print("+---------------------------------------+")
    print("|            0.) Checkout               |")
    print("+---------------------------------------+")
    return input("Please make a selection: ")

def selection(userInput, total):
    if userInput == 1:
        total += 1.50
    elif userInput == 2:
        total += 1.50
    elif userInput == 3:
        total += 1
    elif userInput == 4:
        total += 1
    elif userInput == 5:
        total += 1.25
    elif userInput == 0:
        None
    else:
        print("Invalid input!")
        sleep(5)
    return total


userInput = None
while userInput != 0:
    userInput = int(menu())
    selection(userInput, 0)
    
