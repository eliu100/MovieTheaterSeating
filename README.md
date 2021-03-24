# Eric Liu Movie Theater Seating Challenge

### Language Used: Python

The algorithm uses the following rules:
1. The reservations are seated in descending order of seats requested
2. Customers are seated starting from the first row.
3. There is always a buffer of 3 seats and/or 1 row between customers in different groups.
4. Seat as many customers as possible

### Assumptions Made:
1. The reservation numbers are unique
2. It is safe for customers in the same group to be seated together.
3. The buffer between different groups must be maintained.
4. Customers have no preference in terms of row position.

### Customer Satisfaction:
1. For customers, the main priority is to get a seat. Since this algorithm attempts to maximize the number of customers that get seats, we are maximizing the number of customers that are satisfied.
2. A secondary priority is for customers of the same reservation to be grouped together. This algorithm attempts to seat groups together whenever possible, so that seated groups will be satisfied with their seats.

### Customer Safety:
1. This algorithm prioritizes customer safety by always maintaining a buffer of 3 seats and/or 1 row between different groups. As such, there will be minimal contact between different groups which will maximize the safety of seated customers.

### Steps for Running:
1. Ensure that Python3 is installed.
2. Download the repository.
3. Place input files inside the /inputs directory.
4. In the command line, run the command ```python main.py inputs/NAME_OF_INPUT.txt```.
5. Output will be written to ```output.txt```.
6. To run the tests, run the command ```python test.py``` in the command line.
