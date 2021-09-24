"""
Braden Bell
CSC-1200-001
Prof. Focht
Sep 24, 2021

Lab 4 - Loops
"""

def clearScreen():
    for x in range(10):
        print("\n")
#Part 1 - While Loop:
def partOne():
    binary = ""
    #Ask user for the number they would like to convert
    inputNumber = int(input("Please enter a positive integer that you would like to convert to binary: "))
    #Iterates though inputNumber and create the binary number in a string
    while inputNumber != 0:
        remainder = str(inputNumber % 2)
        inputNumber //= 2
        binary = remainder + binary
    #Final output
    print("\nYour binary number: " + binary + "\n")
    input("Press 'enter' to continue to part 2 of lab...")


def partTwo():
    output = ""
    #Ask user for inputs
    inputNumber = int(input("Please enter the number of lines you would like: "))
    inputCharacter = input("Please enter a single character you would like to use: ")
    #Iterate thourgh inputNumber and adds inputCharacter to ouput for every loop
    for x in range(inputNumber):
        output = output + inputCharacter + " "
        print(output)
    input("Press 'enter' to close the program")

#Run the functions and clears the screen in between them
clearScreen()
partOne()
clearScreen()
partTwo()