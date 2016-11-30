def get_int_in_range(first, last):
    """
    Forces the user to enter an integer within a specified range.
    first is either a minimum or maximum acceptable value.
    last is the corresponding other end of the range, either a maximum or minimum value.
    Returns an acceptable value from the user.
    """
    # If the larger number is provided first, 
    # switch the parameters
    if  first > last:
        first, last = last, first
    # Insist on values in the range first...last
    in_value = int(input("Please enter values in the range " \
                         + str(first) + "..." + str(last) + ": "))
    while in_value < first or in_value > last:
        print(in_value, "is not in the range", first, "...", last)
        in_value = int(input("Please try again: "))
    # in_value at this point is guaranteed to be within range
    return in_value


def main():
    """ Tests the get_int_in_range function """
    print(get_int_in_range(10, 20))
    print(get_int_in_range(20, 10))
    print(get_int_in_range(5, 5))
    print(get_int_in_range(-100, 100))


main()   # Run the program
