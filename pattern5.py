n = 6
for i in range(n):
    for j in range(i):
        print(i, end=" ")

    print()    

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n), i is the current row index, and the inner loop prints the current row index (i) for each row, creating a triangular pattern of numbers where each row contains the same number repeated.         