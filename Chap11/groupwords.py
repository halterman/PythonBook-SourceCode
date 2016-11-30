"""  Uses a dictionary to group the words in a text file according to
     their length (number of letters).  """

import sys     # For argv global command line arguments list


def main():
    """  Group the words by length in a text file.  """
    if len(sys.argv) < 2:   # Did the user not supply a file name?
        print('Usage:  python groupwords.py <filename>')
        print('     where <filename> is the name of a text file.')
    else:   # User provided file name
        filename = sys.argv[1]
        groups = {}        # Initialize grouping dictionary
        with open(filename, 'r') as f:  # Open the file for reading
            content = f.read()  # Read in content of the  entire file
            words = content.split() # Make list of individual words
            for word in words:
                word = word.upper()  # Make the word all caps
                # Compute the word's length
                size = len(word)
                if size in groups:
                    if word not in groups[size]:  # Avoid duplicates
                        groups[size] += [word]  # Add the word to its group
                else:
                    groups[size] = [word]   # Add the word to a new group
            # Show the groups
            for size, group in groups.items():
                print(size, ':', group)


if __name__ == '__main__':
    main()
