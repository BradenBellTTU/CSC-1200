import os
import string
#Uses the OS library to get the location of BeeMovie.txt. It works as long as the file is in the same dir as the script
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

"""main() function defined, iterates through the file and stores each word in 'word' for processing, and calls on the count() function
and ultimately returns 'dictionary'"""
def main():
    dictionary = {}
    with open(os.path.join(__location__, 'BeeMovie.txt')) as file:
        for line in file:
            for word in line.split():
                dictionary = count(word,dictionary)
    return dictionary

#Defines count() and imports 'word' and 'dictionary' into the function
def count(word,dictionary):
    #word sanitization
    word = word.lower()
    word = word.strip()
    #removes punctuation using the translate library
    word = word.translate(str.maketrans('', '', string.punctuation))
    wordFound = False
    #Adds word to dictionary if it is a new word, if it is not, then it incriments the value of the word in the dictionary
    for x in dictionary:
        if x == word:
            dictionary[x] += 1
            wordFound = True
    if wordFound == False:
        dictionary.update({word : 1})
    return dictionary

#Calls main() function and lets the user know an output is being processed if it takes time to process
print("Loading, one moment please...")
output = main()
#Iterates through 'output' and prints each one to the user in the desired format
for x in output:
    print(x + " : " + str(output[x]))
