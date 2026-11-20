n = 5
for i in range(1, n + 1):
    spaces = "  " * (n - i)
    stars = "* " * i
    print(spaces + stars)

# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n), and the inner loop prints    spaces followed by asterisks for each row, creating a right-aligned triangular pattern of asterisks.            