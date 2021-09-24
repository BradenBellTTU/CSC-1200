binary = ""
inputNumber = int(input("Please enter a number: "))
if inputNumber < 0:
    print("Please enter a number greater than 0")
    input("Press 'Enter' to exit")
    exit()

while inputNumber != 0:
    remainder = str(inputNumber % 2)
    inputNumber //= 2
    binary = remainder + binary

print(binary)
