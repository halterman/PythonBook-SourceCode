from random import randint

def nonrec(n, depth):
    """  Prints the value of the parameter n and local variable
         rand before and after the recursive call.
         n is the parameter of interest.
         depth represents the depth of the recursion.  """
    history = []
    while n != 0:
        rand = randint(0, 1000)  # Make a random number
        history += [(n, depth, rand)]  # Remember original values of n and depth
        print('  ' * depth, 'Entering: n =', n, '  rand =', rand)
        n -= 1
        depth += 1
    print('  ' * depth, '  *** Recursion over ***')
    while len(history) > 0:
        n, depth, rand = history[-1]
        del history[-1]
        print('  ' * depth, 'Exiting: n =', n, '  rand =', rand)


nonrec(10, 0)
