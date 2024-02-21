from string import *
from random import *
class Spinner:
    def __init__ (self):
        self.synonyms = {}
    def makeDictionary(self, file):
        f = open(file,"r")
        for x in f:
            values = []
            l = x.replace(":",",")
            line = l.split(",")
            k = line[0]
            for y in range(1,len(line)):
                values.append(line[y].strip())
            self.synonyms[k] = values
    def readInput(self,i):
        wordList = []
        self.i = i.translate(str.maketrans(" "," ",punctuation))
        p = i.split(" ")
        for r in range(len(p)):
            change = False
            for s in self.synonyms.keys():
                if p[r] == s:
                    randomNumber = randint(1,100)
                    if randomNumber >= 50:
                        change = True
                        choices = (self.synonyms[p[r]])
                        randomChoice = randint(0,len(choices))
                        wordList.append(choices[randomChoice])
                        break
            if change == False:
                wordList.append(p[r])
        spun = " ".join(wordList)
        return (spun)

