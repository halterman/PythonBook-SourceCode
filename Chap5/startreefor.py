#  Get tree height from user
height = int(input('Enter height of tree: '))

#  Draw one row for every unit of height
for row in range(height):
    # Print leading spaces; as row gets bigger, the number of
    # leading spaces gets smaller
    for count in range(height - row):
        print(end=' ')

    # Print out stars, twice the current row plus one:
    #   1. number of stars on left side of tree 
    #      = current row value
    #   2. exactly one star in the center of tree
    #   3. number of stars on right side of tree 
    #      = current row value
    for count in range(2*row + 1):
        print(end='*')
    # Move cursor down to next line
    print()
