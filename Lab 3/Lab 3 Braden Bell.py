"""
Braden Bell
CSC-1200-001
Prof. Focht
Sep 17, 2021

Lab 3 - Jukebox
"""

#create clear screen function
def clearScreen():
    for x in range(10):
        print("\n")

#Welcome Screen
clearScreen()
print("+--------------------------------+")
print("| Welcome to the Python Jukebox! |")
print("+--------------------------------+\n\n")

#Asks user what genre they want
print("Which genre do you want to listen to?\n")
print("1. Pop")
print("2. Classics")
print("3. Comedy\n")
category = input("Choice: ")
clearScreen()

#Display songs according to genre picked before
print("Here is our selection: \n")
if (category == "1"):
    print("1. The Outside")
    print("2. Uptown Funk")
    print("3. Havana\n")
    #Depending on their choice, assigns what's playing to nowPlaying
    song = input("Choice: ")
    if (song == "1"):
        nowPlaying = "The Outside by Twenty One Pilots"
    elif (song == "2"):
        nowPlaying = "Uptown Funk by Mark Ronson"
    elif (song == "3"):
        nowPlaying = "Havana by Camila Cabello"
    
elif(category == "2"):
    print("1. More Than a Feeling")
    print("2. Don't Stop Believing")
    print("3. I Love Rock n' Roll\n")
    song = input("Choice: ")
    if (song == "1"):
        nowPlaying = "More than a Feeling by Boston"
    elif (song == "2"):
        nowPlaying = "Don't Stop Believing by Journey"
    elif (song == "3"):
        nowPlaying = "I Love Rock n' Roll by Joan Jet & The Black Hearts"
    
elif(category == "3"):
    print("1. The Streak")
    print("2. The Mississippi Squirrel Revival")
    print("3. Never Gonna Give You Up\n")
    song = input("Choice: ")
    if (song == "1"):
        nowPlaying = "The Streak by Ray Stevens"
    elif (song == "2"):
        nowPlaying = "The Mississippi Squirrel Revival by Ray Stevens"
    elif (song == "3"):
        nowPlaying = "Never Gonna Give You Up by Rick Astley"
    
#if there is an invalid input, then the program complains and ends instead of erroring out.
else:
    print("Invalid entry, please try again!")
    exit()

#Final output and displays some crude ascii art and the nowPlaying varible
clearScreen()
print("Now playing:\n\n")
print(nowPlaying + "\n")
print("|--[]--------------------------------------|\n")
print(" Pause ||          Play >           Skip >>  \n")

