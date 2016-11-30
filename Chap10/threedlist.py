
#  Make a 3D matrix representing the intermediate state
#  of a 3D Tic-Tac-Toe game in progress.

matrix = [[['X', '.', '.', 'O'],
             ['.', '.', '.', '.'],
              ['.', '.', '.', '.'],
                ['.', '.', '.', '.']],
          [['.', '.', '.', 'O'],
             ['.', 'X', '.', '.'],
              ['.', '.', '.', '.'],
                ['.', '.', '.', '.']],
          [['.', '.', '.', '.'],
             ['.', '.', '.', '.'],
              ['.', '.', 'X', '.'],
                ['.', '.', '.', '.']],
          [['.', '.', '.', '.'],
             ['.', '.', '.', '.'],
              ['.', '.', '.', '.'],
                ['.', '.', '.', 'O']]]
 

# Pretty print the matrix
# Need the length of a row in order to adjust the indentation
row_length = len(matrix[0][0])
for layer in matrix:     # Process each layer
    for row in range(len(layer)):   # For each row by its index
        print('  ' * (row_length - row), end='')  # Print diminishing offset based on its index
        for column in range(len(layer[row])):   # For each element in a given row
            print('{:>4}'.format(layer[row][column]), end='')
        print()
    print()
