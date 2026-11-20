n = 6
for i in range(n):
    for j in range(n - i):
        print("* ", end="")


    print()    


# I use nested loops to print the pattern. 
# The outer loop iterates over the number of rows (n), and the inner loop prints n - i asterisks followed by a space for each row, where i is the current row index. 
# This creates a decreasing number of asterisks in each subsequent row.