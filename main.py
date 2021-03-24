import sys
import theater

def main():
    if (len(sys.argv) != 2):
        print("You must pass an input file as the argument", file = sys.stderr)
        return
    try:
        movieTheater = theater.Theater()
        with open(sys.argv[1], 'r') as inputFile:
            outputFile = open("output.txt", 'w')
            allLines = inputFile.read().splitlines()
            sortedLines = []
            for line in allLines:
                input = line.split(" ")
                reservationNo = input[0]
                numRequested = int(input[1])
                sortedLines .append((reservationNo, numRequested))
            sortedLines.sort(key = lambda x: x[1], reverse=True)
            for line in sortedLines:
                outputList = movieTheater.book(line)
                if (len(outputList) > 0):
                    outputString = ",".join(outputList)
                    outputFile.write("%s %s\n" % (line[0], outputString))
            #print(movieTheater.seats)
            print("output.txt")
    except FileNotFoundError:
        print("Input file %s does not exist" % sys.argv[1])



if __name__ == "__main__":
    main()