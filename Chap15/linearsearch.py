def locate(lst, seek):
    """
    Returns the index of element seek in list lst,
    if seek is present in lst.
    Returns None if seek is not an element of lst.
    lst is the list in which to search.
    seek is the element to find.
    """
    for i in range(len(lst)):
        if lst[i] == seek:
            return i      # Return position immediately
    return None           # Element not found


def format(i):
    """
    Prints integer i right justified in a 4-space
    horizontal area.  Prints "****" if i > 9,999.
    """
    if i > 9999:
        print("****")      # Too big!
    else:
        print("{0:>4}".format(i))


def show(lst):
    """
    Prints the contents of list lst
    """
    for item in lst:
        print("{0:>4}".format(item), end='') # Print element right justifies in 4 spaces
    print()                           # Print newline


def draw_arrow(value, n):
    """
    Print an arrow to value which is an element in a list.
    n specifies the horizontal offset of the arrow.
    """
    print(('{0:>' + str(n) + '}').format("   ^   "))
    print(('{0:>' + str(n) + '}').format("   |   "))
    print(('{0:>' + str(n) + '}{1}').format("   +-- ", value))


def display(lst, value):
    """
    Draws an ASCII art arrow showing where
    the given value is within the list.
    lst is the list.
    value is the element to locate.
    """
    show(lst)                # Print contents of the list
    position = locate(lst, value)
    if position != None:
        position = 4*position + 7   # Compute spacing for arrow
        draw_arrow(value, position)
    else:
        print("(", value, " not in list)", sep='')
    print()
 

def main():
    a = [100, 44, 2, 80, 5, 13, 11, 2, 110]
    display(a, 13)
    display(a, 2)
    display(a, 7)
    display(a, 100)
    display(a, 110)


main()
