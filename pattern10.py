n = 5
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* "  *  n)
    else:
        print("* " +  "  " * (n - 2)  + "*")


# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n), and the inner loop prints asterisks and spaces for each row, creating a hollow square pattern of asterisks. The first and last rows are filled with asterisks, while the middle rows have asterisks only at the beginning and end, with spaces in between.   
#         