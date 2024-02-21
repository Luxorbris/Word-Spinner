
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
        i.strip()