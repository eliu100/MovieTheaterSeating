class Theater:
    rows = 10
    cols = 20
    currInd = (0, 0)
    resNoDict = {}
    seatsAvailable = rows * cols
    seatsLeft = [20] * 10

    def __init__(self):
        self.seats = [["" for x in range(self.cols)] for y in range(self.rows)]

    def indRow(self, ind):
        return chr(ind + 65)

    def prevRow(self, reservationNo, row, col):
        return row == 0 or self.seats[row - 1][col] == "" or self.seats[row - 1][col] == reservationNo

    def nextRow(self, reservationNo, row, col):
        return row == self.rows - 1 or self.seats[row + 1][col] == "" or self.seats[row + 1][col] == reservationNo

    def nextCols(self, reservationNo, row, col):
        if col >= self.cols - 3:
            return True
        for i in range(1, 4):
            if (self.seats[row][col + i] != "" and self.seats[row][col + i] != reservationNo):
                return False
        return True

    def prevCols(self, reservationNo, row, col):
        if col <= 2:
            return True
        for i in range(1, 4):
            if (self.seats[row][col - i] != "" and self.seats[row][col - i] != reservationNo):
                return False
        return True

    def safeSeat(self, reservationNo, row, col):
        return self.prevRow(reservationNo, row, col) and self.nextRow(reservationNo, row, col) and self.nextCols(reservationNo, row, col) and self.prevCols(reservationNo, row, col)


    def allocate(self, reservationNo, seatsToBook):
        r = 0
        while (r >= 0 and r < self.rows):
            if (self.seatsLeft[r] >= seatsToBook):
                c = 0
                while (seatsToBook > 0 and c < 20):
                    if (self.seats[r][c] == "" and self.safeSeat(reservationNo, r, c)):
                        self.seats[r][c] = reservationNo
                        if reservationNo not in self.resNoDict:
                            self.resNoDict[reservationNo] = [self.indRow(r) + str(c+1)]
                        else:
                            self.resNoDict[reservationNo].append(self.indRow(r) + str(c+1))
                        self.seatsLeft[r] -= 1
                        seatsToBook -= 1
                    c += 1
            r += 1

    def book(self, line):
        reservationNo = line[0]
        numRequested = line[1]
        numLeft = numRequested
        if (self.seatsAvailable >= numRequested):
            if (numLeft > 20):
                while (numLeft > 20):
                    self.allocate(reservationNo, 20)
                    numLeft -= 20
                self.allocate(reservationNo, numLeft)
            else:
                self.allocate(reservationNo, numLeft)
        reservedList = self.resNoDict.get(reservationNo, [])
        reservedString = ",".join(reservedList)
        return reservedString