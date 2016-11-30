"""
Uses Python's file class to store data to and retrieve data from
a text file.
"""
def load_data(filename):
    """ Print the elements stored in the text file named filename.  """
    # Open file to read
    with open(filename) as f:   # f is a file object
        for line in f:          # Read each line as text
            print(int(line))    # Convert to integer and append to the list


def store_data(filename):
    """ Allows the user to store data to the text file named filename. """
    with open(filename, 'w') as f:          # f is a file object
        number = 0
        while number != 999:                # Loop until user provides magic number
            number = int(input('Please enter number (999 quits):'))
            if number != 999:
                f.write(str(number) + '\n') # Convert integer to string to save
            else:
                break                       # Exit loop


def main():
    """  Interactive function that allows the user to
         create or consume files of numbers. """
    done = False

    while not done:
        cmd = input('S)ave L)oad Q)uit: ')
        if cmd == 'S' or cmd == 's':
            store_data(input('Enter file name:'))
        elif cmd == 'L' or cmd == 'l':
            load_data(input('Enter filename:'))
        elif cmd == 'Q' or cmd == 'q':
            done = True


if __name__ == '__main__':
    main()
