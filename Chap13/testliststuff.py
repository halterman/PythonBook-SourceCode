from functiontester import FunctionTester

def max_of_three_bad(x, y, z):
    """ Attempts to determine and return the maximum of three 
        numeric values. """
    result = x
    if y > result:
        result = y
    elif z > result:
        result = z
    return result


def max_of_three_good(x, y, z): 
    """ Computes and returns the maximum of three numeric values. """
    result = x
    if y > result:
        result = y
    if z > result:
        result = z
    return result


def sum(lst):
    """ Attempts to compute and return the sum of all the elements in 
        a list of integers.  """
    total = 0
    for i in range(1, len(lst)):
        total += lst[i]
    return total


#  maximum has a bug (it has yet to be written!)
def maximum(lst):
    """ Computes the maximum element in a list of integers. """
    return 0   # maximum not yet implemented


def main():
    t = FunctionTester()  # Make a test object

    # Some test cases to test max_of_three_bad
    t.check("max_of_three_bad test #1", 4, max_of_three_bad, 2, 3, 4)
    t.check("max_of_three_bad test #2", 4, max_of_three_bad, 4, 3, 2)
    t.check("max_of_three_bad test #3", 4, max_of_three_bad, 3, 2, 4)

    # Some test cases to test max_of_three_good
    t.check("max_of_three_good test #1", 4, max_of_three_good, 2, 3, 4)
    t.check("max_of_three_good test #2", 4, max_of_three_good, 4, 3, 2)
    t.check("max_of_three_good test #3", 4, max_of_three_good, 3, 2, 4)

    # Some test cases to test maximum
    t.check("maximum test #1", 4, maximum, [2, 3, 4, 1])
    t.check("maximum test #2", 4, maximum, [4, 3, 2, 1])
    t.check("maximum test #3", 0, maximum, [-2, -3, 0, -21])

    # Some test cases to test sum
    t.check("sum test #1", 7, sum, [0, 3, 4])
    t.check("sum test #2", 2, sum, [-3, 0, 5])

    t.report_results()


main()
