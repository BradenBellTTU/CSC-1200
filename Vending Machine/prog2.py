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

def paymentProcess(total):
    print("Your total is $" + ('%.2f' % total))    
    payment = input("Please enter your payment amount: ")
    if payment == total:
        print("Thank you for your purchase, have a good day")
        print("Change: $0.00")
        exit()
    elif payment < total:
        print("You have not entered a sufficient amount, please restart your order.")
        exit()
    else:
        change = payment - total
        

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
        total += 0
    else:
        print("Invalid input!")
        sleep(1)
    return total

def main():
    userInput = None
    total = 0
    while userInput != 0:
        userInput = int(menu())
        total = selection(userInput, total)
        if total == 0:
            print("You did not purchase anything!")
            print("Goodbye")
            exit()
        else:
            paymentProcess(total)

main()