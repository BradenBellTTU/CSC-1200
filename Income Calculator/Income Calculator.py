"""
Braden Bell
CSC-1200-001
Prof. Focht
Sep 20, 2021

This script asks for the user to input their monthly income and their monthly expenses.
Next, it checks to see if the user has enough income for the month.
If they do, then it lets user know and tells them how much they have left over for savings.
If they do not, then it tells the user how much more they need to cover their costs.
I also included a clearScreen function that 'clears' the console for better readibilty and also used
sleep statements to give the user a sense that the computer is doing something and for better flow.
I stored the numerical values as floats to calculate cents as well, and I used round() to make sure the math
is outputted to the user in a readible format.
"""

#Startup
from time import sleep
def clearScreen():
    x = 0
    for x in range(10):
        print("\n")

#Intro Screen
clearScreen()
print("+-------------------------------------------------+")
print("| Welcome to the Python Income Calculator!        |")
print("| Please make all inputs plain numbers with no $  |")
print("+-------------------------------------------------+")
print("\n")
sleep(3)

#Asks the user for their monthly income
clearScreen()
monthlyIncome = float(input("What is your monthly income?\n\n"))

#Asks the user for their monthly expenses by category
clearScreen()
print("What are your monthly expenses?")
print("(If you do not have a bill for the specified category, just enter the number 0)\n\n")
rent = float(input("Rent: "))
water = float(input("Water Bill: "))
electricity = float(input("Electricity Bill: "))
internet = float(input("Internet Bill: "))
phone = float(input("Phone Bill: "))
car = float(input("Car Payment: "))
gas = float(input("Gas Bill: "))
other = float(input("Misc. Expenses: "))

#Add them all together and stores them in monthlyExpenses
monthlyExpenses = (rent + water + electricity + internet + phone + car + gas + other)

#Calculates whether the user has enough money for the month and tells them how much they have left over, or how much they need
if monthlyIncome >= monthlyExpenses:
    print("\nYou should be good for this month! Good Job!\n")
    print("You will have $" + str(round(monthlyIncome - monthlyExpenses, 2)) + " left over for savings\n")

else:
    print("\nOh no, you don't have enough!")
    print("You still need $" + str(abs((round(monthlyIncome - monthlyExpenses, 2)))) + " to cover your expenses for this month!\n")

input("Press enter to close the program...")