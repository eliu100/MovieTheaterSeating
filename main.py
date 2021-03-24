import sys
import theater

def main():
    if (len(sys.argv) != 2):
        print("You must pass an input file as the argument", file = sys.stderr)
        return
    try:
        with open(sys.argv[1], 'r') as inputFile:
            line = inputFile.read().splitlines()
            print(line)
    except FileNotFoundError:
        print("Input file %s does not exist" % sys.argv[1])



if __name__ == "__main__":
    main()