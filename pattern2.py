n = 6
for i in range(n):
    for j in range(i):
        print("* ", end="")

    print()    

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n),
# and the inner loop prints i asterisks followed by a space for each row, where i is the current row index.        