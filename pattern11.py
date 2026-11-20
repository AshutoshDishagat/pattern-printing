n = 5
for i in range(1, n + 1):
    if i == 1:
        print("*")
    elif i == n:
        print("* " * n)
    else:
        print("* " + "  " * (i - 2) + "*")

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n), and the inner loop prints asterisks and spaces for each row, creating a right-aligned triangular pattern of asterisks. The first row has one asterisk, the last row has n asterisks, and the middle rows have asterisks at the beginning and end, with spaces in between.    


