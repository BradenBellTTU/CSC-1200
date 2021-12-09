import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
import copy

def clear_screen():
    for x in range(0, 20):
        print("\n")

def print_house(h,sr,sc):
    th = copy.deepcopy(h)
    th[sr][sc] = "@"
    for i in th:
        print(''.join(str(x) for x in i), end='')

def build_house():
    print("Please enter the house file: ")
    house_file = input("")
    housefp = open(os.path.join(__location__, house_file))
    myhouse = []
    line = housefp.readline()
    while line:
        myhouse.append(list(line))
        line = housefp.readline()
    return myhouse

def check_north(house, row, col):
    if house[row-1][col] == "*":
        return False
    else:
        return True

def check_east(house, row, col):
    if house[row][col+1] == "*":
        return False
    else:
        return True

def check_south(house, row, col):
    if house[row+1][col] == "*":
        return False
    else:
        return True

def check_west(house, row, col):
    if house[row][col-1] == "*":
        return False
    else:
        return True

def get_treasure(house, trow, tcol):
    if house[trow][tcol] == "t":
        house[trow][tcol] = " "
        return True
    else:
        return False

def is_door(house, row, col):
    if house[row][col] == "5" or house[row][col] == "6" or house[row][col] == "7" or house[row][col] == "8" or house[row][col] == "9":
        return True
    else:
        return False

def can_unlock(house, unlocked, row, col):
    if unlocked[int(house[row][col]) - 5] == True:
        return True
    else:
        return False


def get_key(house, unlocked, row, col):
    if house[row][col] == "0" or house[row][col] == "1" or house[row][col] == "2" or house[row][col] == "3" or house[row][col] == "4":
        unlocked[int(house[row][col])] = True
        house[row][col] = " "

def main():
    unlocked = [False, False, False, False, False]
    house = build_house()
    #The player's start location
    startrow = 1
    startcol = 9
    trow = startrow
    tcol = startcol
    num_treasures = 2
    tcount = 0
    while tcount < num_treasures:
        print_house(house, startrow, startcol)
        print("Directions: Use WASD to move")
        command = input("")
        if command == "w" and check_north(house, trow, tcol) == True:
            trow = startrow-1
            tcol = startcol
        elif command == "d" and check_east(house, trow, tcol) == True:
            trow = startrow
            tcol = startcol+1
        elif command == "s" and check_south(house, trow, tcol) == True:
            trow = startrow+1
            tcol = startcol
        elif command == "a" and check_west(house, trow, tcol) == True:
            trow = startrow
            tcol = startcol-1
        elif command == "q":
            break
        else:
            print("You cannot go that way!")
        if is_door(house, trow, tcol) == True:
            if can_unlock(house, unlocked, trow, tcol) == False:
                print("Sorry, the door is locked! You need to find a key.")
            elif can_unlock(house, unlocked, trow, tcol) == True:
                print("You unlocked the door.")
                house[trow][tcol] = " "
                startrow = trow
                startcol = tcol
        elif get_key(house, unlocked, trow, tcol) == True:
            print("You found a key!")
        
        else:
            startrow = trow
            startcol = tcol
            if get_treasure(house, trow, tcol) == True:
                tcount +=1
                print("You found a treasure!")
                print("You have " + str(tcount) + " treasures")

        if tcount == num_treasures:
            print("Congradulations, you collected all the treasures!")



main()
