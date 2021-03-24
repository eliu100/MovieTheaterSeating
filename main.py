import sys
import theater

def main():
    if (len(sys.argv) != 2):
        print("You must pass an input file as the argument", file = sys.stderr)
        return
    try:
        with open(sys.argv[1], 'r') as inputFile:
            outputFile = open("output.txt", 'w')
            allLines = inputFile.read().splitlines()
            for line in allLines:
                outputFile.write(theater.book(line) + "\n")
    except FileNotFoundError:
        print("Input file %s does not exist" % sys.argv[1])



if __name__ == "__main__":
    main()