import unittest

###### The original functions from before ################################

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

###### Some new code to test  ###########################################

class ListManager(object):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

    def get(self, idx):
        return self.lst[idx] # Subject to range exception


###### The test class  ##################################################

class TestFunctionsEtc(unittest.TestCase):
    # Some test cases to test max_of_three_bad
    def test_max_of_three_bad_1(self):
        self.assertEqual(max_of_three_bad(2, 3, 4), 4)

    def test_max_of_three_bad_2(self):
        self.assertEqual(max_of_three_bad(4, 3, 2), 4)

    def test_max_of_three_bad_3(self):
        self.assertEqual(max_of_three_bad(3, 2, 4), 4)

    # Some test cases to test max_of_three_good
    def test_max_of_three_good_1(self):
        self.assertEqual(max_of_three_bad(2, 3, 4), 4)

    def test_max_of_three_good_2(self):
        self.assertEqual(max_of_three_bad(4, 3, 2), 4)

    def test_max_of_three_good_3(self):
        self.assertEqual(max_of_three_bad(3, 2, 4), 4)

    # Some test cases to test maximum
    def test_maximum_1(self):
        self.assertEqual(maximum([2, 3, 4, 1]), 4)

    def test_maximum_2(self):
        self.assertEqual(maximum([4, 3, 2, 1]), 4)

    def test_maximum_3(self):
        self.assertEqual(maximum([-2, -3, 0, -21]), 0)

    # Some test cases to test sum
    def test_sum_1(self):
        self.assertEqual(sum([0, 3, 4]), 7)

    def test_sum_2(self):
        self.assertEqual(sum([-3, 0, 5]), 2)

    # Some code that can throw an exception
    def test_list_manager_1(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(2), 3)

    def test_list_manager_2(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(3), 3)

    def test_list_manager_3(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(0), 1)

    def test_list_manager_4(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(0), 0)


if __name__ == '__main__':
    unittest.main()
