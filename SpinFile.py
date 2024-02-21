from Spinner import *
def main():
    e = open("essay.txt", "r") # opens the essay
    i = e.read() # assigns the entire essay string to i
    s = Spinner() # makes a new object
    s.makeDictionary("synonyms-simplified.txt") # converts the synonym file into a dictionary
    print (f"Original: {i}\nOption 1: {s.readInput(i)}\nOption 2: {s.readInput(i)}\nOption 3: {s.readInput(i)}")
    # ^ makes and formats different versions into the original as well as three options
if __name__ == "__main__":
    main() # starts the program