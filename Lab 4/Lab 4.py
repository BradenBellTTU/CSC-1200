"""
Braden Bell
CSC-1200-001
Prof. Focht
Sep 24, 2021

Lab 4 - Loops
"""

def partOne():
    binary = ""
    inputNumber = int(input("Please enter a number: "))
    if inputNumber < 0:
        print("\nEnter a number greater than 0!\n")
        input("Press 'Enter' to exit")
        exit()

    while inputNumber != 0:
        remainder = str(inputNumber % 2)
        inputNumber //= 2
        binary = remainder + binary
    print(binary)


def partTwo():
    inputNumber = int(input("Please enter a number: "))
    inputCharacter = input("Please enter a character: ")
    output = ""

    for x in range(inputNumber):
        output = output + inputCharacter + " "
        print(output)


partOne()
partTwo()