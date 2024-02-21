from Spinner import *
def main():
    e = open("essay.txt","r")
    i = e.read()
    s = Spinner()
    s.makeDictionary("synonyms-simplified.txt")
    print (f"Original: {i}\nOption 1: {s.readInput(i)}\nOption 2: {s.readInput(i)}\nOption 3: {s.readInput(i)}")

if __name__ == "__main__":
    main()