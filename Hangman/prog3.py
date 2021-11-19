"""
Braden Bell
CSC-1200-001
Prof. Focht
Nov 17, 2021

Program 3: Hangman. I derived all of the added code from the psudo code from the assignment sheet and tried to keep to it to the T
"""

#Had to import the random library to pick a random word, and the os library to select the file
import random
import os

#Predefined functions:
def draw_hang_loser():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|        /|\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs_la():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |\   \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_legs():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|        / \   \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head_body_ll():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|          \   \n")
    print("|              \n")
    print("|              \n")   

def draw_hang_head_body():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_head():
    print(" _________     \n")
    print("|         |    \n")
    print("|         0    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hang_scaffold():
    print(" _________     \n")
    print("|         |    \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")
    print("|              \n")

def draw_hangman(state):
    if state == 0:
        draw_hang_scaffold()
    elif state == 1:
        draw_hang_head()
    elif state == 2:
        draw_hang_head_body()
    elif state == 3:
        draw_hang_head_body_ll()
    elif state == 4:
        draw_hang_head_body_legs()
    elif state == 5:
       draw_hang_head_body_legs_la()
    elif state == 6:
        draw_hang_loser()
        
def replace_all(orig, working, ch):
  done = False
  count = 0
  while not done:
    idx = orig.find(ch)
    if idx != -1:
      count = count + 1
      orig = orig[:idx] + "_" + orig[idx+1:]
      working = working[:idx] + ch + working[idx+1:]
    else:
      done = True
  return count != 0, orig, working 
  


#Code added for assignment:

def blanks_gone(s):
    #If "_" is not found in the 's' varible then return True
    if s.find("_") == 0:
        return True
    #If "_" is found, then return False
    elif s.find("_") == -1:
        return False

def main():
    #Initialize variables
    state = 0
    losing_state = 6
    places = ""
    winner = False

    """I Had to use this strange work around again to get python to read the file in Visual Studio Code.
       I was critizied for using it last time in Lab 7, but it is the *only* way I could get python to read this file in my IDE.
       For whatever reason the normal method does not work and returns a "file not found" error.
    """
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    sentence = random.choice(open(os.path.join(__location__, 'Words.txt')).read().split()).lower()

    #For every letter in 'sentence', add "_" to 'places'
    for x in sentence:
        places += "_"

    #Loop as long as the player is not a winner nor loser
    while winner == False and state != losing_state:
        draw_hangman(state)
        print(places)
        print("The word is: " + sentence) #Prints 'sentence' for the person debugging or grading
        char = input("Enter a character: ") #Get input from user and set it to 'char'
        

        output = replace_all(sentence, places, char) #take the tuple that replace_all outputs and sets it to 'output'
        success = output[0] #Set success to the first item in the 'output' tuple
        sentence = output[1] #Set sentence to the second item in the 'output' tuple
        places = output[2] #Set places to the third item in the 'output' tuple

        #Does appropriate action if the guess was right or wrong
        if success == False:
            state += 1
        if blanks_gone(places) == False:
            winner = True
    
    draw_hangman(state)
    if winner == True:
        print("CONGRATS! You Win!")
    else:
        print("Sorry, you lose :-(")
        
main()


    
