import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
import copy

def print_house(h,sr,sc):
  th = copy.deepcopy(h)
  th[sr][sc] = "@"
  for i in th:
    print(''.join(str(x) for x in i), end='')

def build_house():
    print("Please enter the house file: ")
    house_file = input()
    housefp = open(os.path.join(__location__, house_file))
    myhouse = []
    line = housefp.readline()
    while line:
        myhouse.append(list(line))
        line = housefp.readline()
    return myhouse

def check_north(house, row, col):
    if house[row][col] == "*":
        print("You cannot move there!")
        return False
    elif house[row][col] == "" or house[row][col] == " ":
        return True

def check_east(house, row, col):
    if house[row][col] == "*":
        print("You cannot move there!")
        return False
    elif house[row][col] == "" or house[row][col] == " ":
        return True

def check_south(house, row, col):
    if house[row][col] == "*":
        print("You cannot move there!")
        return False
    elif house[row][col] == "" or house[row][col] == " ":
        return True

def check_west(house, row, col):
    if house[row][col] == "*":
        print("You cannot move there!")
        return False
    elif house[row][col] == "" or house[row][col] == " ":
        return True

def get_treasure(house, trow, tcol):
    if house[trow][tcol] == "t":
        house[trow][tcol] = " "
        return True
    else:
        return False

def main():
    house = build_house()
    #The player's start location
    startrow = 1
    startcol = 9
    num_treasures = 2
    tcount = 0
    while tcount < num_treasures:
        print_house(house, startrow, startcol)
        print("N, E, S, W")
        command = input("")
        if command == "w":
            trow = startrow-1
            tcol = startcol
        elif command == "d":
            trow = startrow
            tcol = startcol+1
        elif command == "s":
            trow = startrow+1
            tcol = startcol
        elif command == "a":
            trow = startrow
            tcol = startcol-1
        elif command == "q":
            break
        if house[trow][tcol] == "*":
            print("You cannot go that way!")
        if get_treasure(house, trow, tcol) == True:
            tcount +=1
            print("You found a treasure!")
            print("You have " + str(tcount) + " treasures")
        startrow = trow
        startcol = tcol

        if tcount == num_treasures:
            print("Congradulations, you collected all the treasures!")




main()
