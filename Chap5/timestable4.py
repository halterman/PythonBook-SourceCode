#  Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
#  Print a size x size multiplication table
#  First, print heading:  1  2  3  4   5   etc.
print("     ", end='')
#  Print column heading
for column in range(1, size + 1):
    print('{0:4}'.format(column), end='')  # Display column number
print()   # Go down to the next line
#  Print line separator:   +------------------
print("    +", end='')
for column in range(1, size + 1):
    print('----', end='')  # Display line
print()     # Drop down to next line

#  Print table contents
for row in range(1, size + 1):
    print('{0:3} |'.format(row), end='')       # Print heading for this row
    for column in range(1, size + 1):
        product = row*column                    # Compute product
        print('{0:4}'.format(product), end='')  # Display product
    print()                                     # Move cursor to next row
