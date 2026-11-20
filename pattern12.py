n = 5

for i in range(1, n + 1):

    left = "* " * i
    spaces = "  " * (2 * (n - i))
    right = "* " * i

    print(left + spaces + right)


for i in range(n - 1, 0, -1):

    left = "* " * i
    spaces = "  " * (2 * (n - i))
    right= "* " * i

    print(left + spaces + right)


# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n) in both ascending and descending order, and the inner loop prints asterisks, spaces, and asterisks for each row, creating a diamond-shaped pattern of asterisks with spaces in the middle.
#     