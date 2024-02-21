from Spinner import *
def main():
    i = input("").lower()
    s = Spinner()
    s.makeDictionary("synonyms-simplified.txt")
    print (f"Original: {i}\nOption 1: {s.readInput(i)}\nOption 2: {s.readInput(i)}\nOption 3: {s.readInput(i)}")

main()