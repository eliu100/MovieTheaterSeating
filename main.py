import sys
import theater

def main():
    if (len(sys.argv) != 2):
        print("You must pass an input file as the argument", file = sys.stderr)
        return
    try:
        inputFile = open(sys.argv[1])
    except FileNotFoundError:
        print("Input file %s does not exist" % sys.argv[1])



if __name__ == "__main__":
    main()