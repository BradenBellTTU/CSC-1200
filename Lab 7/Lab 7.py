import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

dictionary = {}
def main():
    with open(os.path.join(__location__, 'BeeMovie.txt')) as file:
        for line in file:
            for word in line.split():
                print(word)

main()

