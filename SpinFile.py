from Spinner import *
def main():
    i = input("")
    s = Spinner()
    s.makeDictionary("test-synonyms.txt")
    print(s.synonyms)

main()