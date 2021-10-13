from random import choice
def getData():
    songs = []
    user = ""
    print("Please enter the names of your songs or 'exit' to play them")
    while True:
        user = input("")
        if user == "exit" or user == "Exit":
            return songs
        else:
            songs.append(user) 

          
def playRandom():
    x = choice(getData())
    return x

def main():
    print("+--------------------------------------+")
    print("| Welcome to the Python Playlist Maker |")
    print("+--------------------------------------+")
    getData()
    print("Now Playing: " + playRandom())

main()