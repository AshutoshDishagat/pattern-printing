n = 5

for i in range(1, n + 1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)


for i in range(n - 1, 0, -1):
    spaces = "  " * (n - i)
    stars = "* " * (2 * i - 1)
    print(spaces + stars)


# I use nested loops to print the pattern.
# The outer loop iterates over the number of rows (n) in both ascending and descending  order, and the inner loop prints spaces followed by asterisks for each row, creating a diamond-shaped pattern of asterisks. 
#     