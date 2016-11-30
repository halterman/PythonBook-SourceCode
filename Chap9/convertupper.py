"""
convertupper.py
"""
def capitalize(filename):
    """  Creates a new file with the prefix 'upper_'
         added to the name of the original file.  
         All the alphabetic characters in the new 
         are capitalized.  This function does not
         disturb the contents of the original file. """
    with open(filename, 'r') as infile:
        with open('upper_' + filename, 'w') as outfile:
            for line in infile:
                line = line.strip().upper()
                print(line, file=outfile)
