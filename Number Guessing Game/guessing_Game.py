from random import randint
number = randint(0,100)

def clearScreen():
    for x in range(10):
        print("\n")
clearScreen()
print("Guess the number between 0-100")
while(True):
    guess = int(input("Guess: "))
    if guess > number:
        clearScreen()
        print("Lower\n")
    elif guess < number:
        clearScreen()
        print("Higher\n")
    elif guess == number:
        print("You guessed it!")
        play = input("Try again (Y/N)?")
        if play == "Y" or play == "y":
            number = randint(0,100)
        elif play =="N" or play == "n":
            break
        