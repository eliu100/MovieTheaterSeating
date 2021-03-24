import theater

testTheater = theater.Theater()
print("****** TESTING ******")

assert(len(testTheater.book(("R01", 0))) == 0)
print("Test 1 Passed, No reservation made for zero seats")

assert(testTheater.book(("R02", 10)) == ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10'])
print("Test 2 Passed, Successfully reserved 10 seats in the first row.")

assert(len(testTheater.book(("R03", 1000))) == 0)
print("Test 3 Passed, Didn't reserve seats when the request was greater than the number of seats available.")

assert(len(testTheater.book(("R04", 40))) == 40)
print("Test 4 Passed, Successfully reserved seats when needing more than one row for a group.")


testTheater.book(("R05", 30))
testTheater.book(("R06", 20))
testTheater.book(("R07", 10))
for r in range(testTheater.rows):
    for c in range(testTheater.cols):
        resNo = testTheater.seats[r][c]
        if (resNo != ""):
            assert(r == 0 or testTheater.seats[r-1][c] == "" or testTheater.seats[r-1][c] == resNo)
            assert(r == testTheater.rows - 1 or testTheater.seats[r + 1][c] == "" or testTheater.seats[r + 1][c] == resNo)
            if c < testTheater.cols - 3:
                for i in range(1, 4):
                    assert(testTheater.seats[r][c + i] == "" or testTheater.seats[r][c + i] == resNo)
            if c > 2:
                for i in range(1, 4):
                    assert(testTheater.seats[r][c - i] == "" or testTheater.seats[r][c - i] == resNo)
print("Test 5 Passed, A buffer of 3 seats and/or 1 row exists.")