n = 5
for i in range(n, 0, -1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n) in reverse order, and the inner loop prints spaces followed by asterisks for each row, creating an inverted centered triangular pattern of asterisks. 
# 
#     