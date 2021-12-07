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
        if house[tcol][trow] == "*":
            print("You cannot go that way!")


main()
