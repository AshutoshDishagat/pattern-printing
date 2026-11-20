n = 6
for i in range(n):
    for j in range(i):
        print(j+1, end=" ")

    print()    

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n), i is the current row index, and the inner loop prints numbers from 1 to i for each row, 
# creating a triangular pattern of numbers.