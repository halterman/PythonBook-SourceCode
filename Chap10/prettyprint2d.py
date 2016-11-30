matrix = [[100,  14,   8,  22,  71],
          [  0, 243,  68,   1,  30],
          [ 90,  21,   7,  67, 112],
          [115, 200,  70, 150,   8]]

for row in matrix:     # Process each row
    for elem in row:   # For each element in a given row
        print('{:>4}'.format(elem), end='')
    print()
