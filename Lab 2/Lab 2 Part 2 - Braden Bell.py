"""
Braden Bell
CSC-1200-001
Prof. Focht
Sep 10, 2021

This script asks the user for their name, age, address, and phone number and outputs it back to them in a friendly way.
It also has a clearScreen() function that prints 10 blank lines to 'clear' the console for better readability
"""
name = input("What is your name? \n")

age = int(input("\nWhat is your age?\n"))

address = input("\nWhat is your address?\n")

phone = input("\nWhat is your phone number?\n")

print("\n\nHello, " + name + "!")
print("You are " + str(age) + " years old")
print("You live at " + address)
print("And your phone numer is " + phone + "\n")
input ("Press enter to end the program...")
