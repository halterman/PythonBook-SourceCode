from dot3x3logic import *


def show_player(p):
    '''  Determines the string to print in the context of a 
         square's owner.  p is a player. '''
    if p:
        return ' ' + p
    else:
        return '  '


def draw_game():
    '''  Draws the connect the dots game using text graphics '''
    #  0---1---2     ------------------------------------
    print('   0', end='')
    if check_line('Northwest_North'):
        print('---', end='')
    else:
        print('   ', end='')
    print('1', end='')
    if check_line('North_Northeast'):
        print('---', end='')
    else:
        print('   ', end='')
    print('2')

    #  |   |   |     ------------------------------------
    if check_line('Northwest_West'):
        print('   |', end='')
    else:
        print('    ', end='')
    print(show_player(square_owner('LeftTop')), end='')
    if check_line('North_Center'):
        print(' |', end='')
    else:
        print('  ', end='')
    print(show_player(square_owner('RightTop')), end='')
    if check_line('Northeast_East'):
        print(' |')
    else:
        print('  ')

    #  3---4---5     ------------------------------------
    print('   3', end='')
    if check_line('West_Center'):
        print('---', end='')
    else:
        print('   ', end='')
    print('4', end='')
    if check_line('Center_East'):
        print('---', end='')
    else:
        print('   ', end='')
    print('5')

    #  |   |   |     ------------------------------------
    if check_line('West_Southwest'):
        print('   |', end='')
    else:
        print('    ', end='')
    print(show_player(square_owner('LeftBottom')), end='')
    if check_line('Center_South'):
        print(' |', end='')
    else:
        print('  ', end='')
    print(show_player(square_owner('RightBottom')), end='')
    if check_line('East_Southeast'):
        print(' |')
    else:
        print('  ')

    #  6---7---8     ------------------------------------
    print('   6', end='')
    if check_line('Southwest_South'):
        print('---', end='')
    else:
        print('   ', end='')
    print('7', end='')
    if check_line('South_Southeast'):
        print('---', end='')
    else:
        print('   ', end='')
    print('8')


def make_line(move):
    '''  Determines the line between two dots specified in the string
         move.  The move parameter is one of '01', 12', '03', etc.
         representing a line connecting the dots in the pattern
             0---1---2
             |   |   |
             3---4---5
             |   |   |
             6---7---8
         The function returns the string that represents the 
         line position between the dots, one of 'Northwest_North', 
         'North_Center', etc.  If the dot1, dot2 pair represents an
         invalid combination, for example, (0, 4), the function
         returns the string 'NoLine'. '''
    if move == '01' or move == '10':
        return 'Northwest_North'
    elif move == '12' or move == '21':
        return 'North_Northeast'
    elif move == '03' or move == '30':
        return 'Northwest_West'
    elif move == '14' or move == '41':
        return 'North_Center'
    elif move == '25' or move == '52':
        return 'Northeast_East'
    elif move == '34' or move == '43':
        return 'West_Center'
    elif move == '45' or move == '54':
        return 'Center_East'
    elif move == '36' or move == '63':
        return 'West_Southwest'
    elif move == '47' or move == '74':
        return 'Center_South'
    elif move == '58' or move == '85':
        return 'East_Southeast'
    elif move == '67' or move == '76':
        return 'Southwest_South'
    elif move == '78' or move == '87':
        return 'South_Southeast'
    else:
        return 'NoLine'  #  Default return value


#  Start a new game
initialize_board()
draw_game()
winning_player = None  #  No winner at start
while not winning_player:
    prompt = 'Move for player ' + current_player() + ': '
    move = input(prompt)  #  Get the dots to connect
    if move == 'Q' or move == 'q':  #  'Q' quits the program
        break
    print()
    #  Add the line, if possible
    new_line = make_line(move)
    if new_line != 'NoLine' and add_line(new_line):
        draw_game()
    else:
        print('Connection not possible')
    winning_player = winner()  #  Check for win

#  Determine winner, if either player X or player Y
if winning_player == 'X':
    print('X won')
elif winning_player == 'Y':
    print('Y won')
else:
    print('Draw')
print('\n***  G A M E   O V E R  ***')
