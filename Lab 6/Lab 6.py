from random import choice
def getData():
    songs = []
    user = ""
    print("Please enter the names of your songs or 'exit' to play them")
    while user.lower() != "exit":
        user = input("")
        songs.append(user)
    return songs

def clearScreen():
    for x in range(10):
        print("\n")
          
def playRandom():
    x = choice(getData())
    clearScreen()
    return x

def main():
    clearScreen()
    print("+--------------------------------------+")
    print("| Welcome to the Python Playlist Maker |")
    print("+--------------------------------------+")
    print("Now Playing: " + playRandom() + "\n")
    print("|--[]--------------------------------------|\n")
    print(" Pause ||          Play >           Skip >>  \n")

main()