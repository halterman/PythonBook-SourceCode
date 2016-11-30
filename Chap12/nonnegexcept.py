def non_neg_int(n):
    """  Converts argument n into a nonnegative integer, if possible. 
         Raises a ValueError if the argument is not convertible
         to a nonnegative integer.  """
    result = int(n)
    if result < 0:
        raise ValueError(result)
    return result


while True:
    try:
        x = non_neg_int(input('Please enter a nonnegative integer:'))
        if x == 999:   # Secret number exits loop
            break
        print('You entered', x)
    except ValueError:
        print('The value you entered is not acceptable')
