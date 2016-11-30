from random import randint

def rec(n, depth):
    """  Prints the value of the parameter n and local variable
         rand before and after the recursive call.
         n is the parameter of interest.
         depth represents the depth of the recursion.  """
    rand = randint(0, 1000)  # Make a random number
    print('  ' * depth, 'Entering: n =', n, '  rand =', rand)
    if n == 0:
        print('  ' * depth, '  *** Recursion over ***')
    else:
        rec(n - 1, depth + 1)
    print('  ' * depth, 'Exiting: n =', n, '  rand =', rand)


rec(10, 0)
