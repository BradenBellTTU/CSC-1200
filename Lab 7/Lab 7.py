import os
import string
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    dictionary = {}
    with open(os.path.join(__location__, 'BeeMovie.txt')) as file:
        for line in file:
            for word in line.split():
                dictionary = count(word,dictionary)
    return dictionary


def count(word,dictionary):
    word = word.lower()
    word = word.strip()
    word = word.translate(str.maketrans('', '', string.punctuation))
    wordFound = False
    for x in dictionary:
        if x == word:
            dictionary[x] += 1
            wordFound = True
    if wordFound == False:
        dictionary.update({word : 1})
    return dictionary

print("One moment please...")
output = main()   
for x in output:
    print(x + " : " + str(output[x]))
