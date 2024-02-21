from string import *
from random import *
class Spinner:
    def __init__ (self):
        self.synonyms = {} # makes the synonym dictionary callable
    def makeDictionary(self, file):
        f = open(file,"r") # opens the file sent into the method
        for x in f: # reads each line
            values = [] # makes the values list and empties the old one
            l = x.replace(":",",") # makes the words easier to split
            line = l.split(",") # splits the words
            k = line[0] # assigns the first word as a key
            for y in range(1,len(line)):
                values.append(line[y].strip()) # strips and adds the word to the values list
            self.synonyms[k] = values # appends the key and values into the synonym dictionary
    def readInput(self,i):
        wordList = [] # makes the list and empties the old one
        self.i = i.translate(str.maketrans(" "," ",punctuation)) # removes punctuation
        p = i.split(" ") # splits the entire thing into words based on spaces
        for r in range(len(p)): # goes through the whole "essay"
            change = False # automatically sets change back to false at the beginning of each loop
            for s in self.synonyms.keys(): # goes through the previously made dictionary
                if p[r] == s: # checks the word against the dictionary keys
                    randomNumber = randint(1,100) # chooses a random number on a match
                    if randomNumber >= 50: # if the random number is 50 or more, the word changes
                        change = True # lets the list know later on not to add an additonal word
                        choices = (self.synonyms[p[r]]) # takes the values from the dictionary keys
                        randomChoice = randint(0,len(choices)-1) # chooses a random word's value from the dictionary values
                        wordList.append(choices[randomChoice]) # puts the chosen word into the list
                        break
            if change == False: # if the word doesn't change, the normal word gets added to the list
                wordList.append(p[r])
        spun = " ".join(wordList) # fuses the whole thing back into one "essay" for easy printing
        return (spun) # sends back the changed "essay"

