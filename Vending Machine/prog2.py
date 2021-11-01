"""
Braden Bell
CSC-1200-001
Prof. Focht
Nov 1, 2021

This program is a vending machine that adhears to all the requirements for the assignment. It has an ASCII art menu for easy readability and
updates the total as the user makes selections.
The user enters a value from 1-5 depending on what they want to purchase. They can purchase as many items as they want, and when they
are finished they enter 0 to checkout. The user then enters the amount they want to pay and the program either dispenses the correct change
in quarters, nickles, dimes, and pennies, or cancels the order if the user does not enter enough. 
"""


from time import sleep

#This function displays the menu and returns the user input
def menu(total):
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
    print("|        0.) Checkout    Total: | $" + ('%.2f' % total) + " |")
    print("+---------------------------------------+")
    return input("Please make a selection: ")

#This function handles all of the payment processes
def paymentProcess(total):
    changeOutput = {"quarters" : 0, "dimes" : 0, "nickles" : 0, "pennies" : 0}
    print("Your total is $" + ('%.2f' % total))    
    payment = float(input("Please enter your payment amount: "))
    #If user enters exact change then thank the user and exit
    if payment == total:
        print("Thank you for your purchase, have a good day")
        print("Change: $0.00")
        exit()
    #If user does not enter enough, cancel the order
    elif payment < total:
        print("You have not entered a sufficient amount, please restart your order.")
        exit()
    #If the user enters anything above the total, calculate change and update the change dictionary accordingly
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

#This function adds the choice the user made to the total
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

#This is the main function and it calls all the other functions and defines all important variables
def main():
    userInput = None
    total = 0
    while userInput != 0:
        userInput = float(menu(total))
        total = selection(userInput, total)
        if total == 0:
            print("You did not purchase anything!")
            sleep(1)
            print("Goodbye")
            exit()
    change = paymentProcess(total)
    print("Thank you for your purchase!")
    sleep(1)
    print("Your change is: ")
    for x in change:
        print(x + ": " + str(change[x]))

main()