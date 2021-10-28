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
    changeOutput = {"quarters" : 0, "dimes" : 0, "nickles" : 0, "pennies" : 0}
    print("Your total is $" + ('%.2f' % total))    
    payment = int(input("Please enter your payment amount: "))
    if payment == total:
        print("Thank you for your purchase, have a good day")
        print("Change: $0.00")
        exit()
    elif payment < total:
        print("You have not entered a sufficient amount, please restart your order.")
        exit()
    else:
        change = payment - total
        while change >= 0.25:
            change -= 0.25
            changeOutput["quarters"] += 1
        while change >= 0.10:
            change -= 0.10
            changeOutput["dimes"] += 1
        while change >= 0.05:
            change -= 0.05
            changeOutput["nickles"] += 1
        while change >= 0.01:
            change -= 0.01
            changeOutput["pennies"] += 1
        return changeOutput

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
    change = paymentProcess(total)
    print("Thank you for your purchase!")
    print("Your change is: ")
    for x in change:
        print(x + ": " + str(change[x]))

main()