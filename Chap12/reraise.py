def is_prime(n):
    """  Returns True if nonnegative integer n is prime; 
         otherwise, returns false.
         Raises a TypeError exception if n is not
         an integer.  """
    from math import sqrt
    if n == 2:                     # 2 is the only even prime number
        return True
    if n < 2 or n % 2 == 0:        # Handle simple cases immediately
        return False               # Raises a TypeError if n is not an integer
    trial_factor = 3
    root = sqrt(n) + 1
    while trial_factor <= root:
        if n % trial_factor == 0:  # Is trial factor a factor?
            return False           # Yes, return right away
        trial_factor += 2          # Next potential factor, skip evens
    return True                    # Tried them all, must be prime


def non_neg(n):
   """  Determines if n is nonnegative.
        Raises a TypeError if n is not an integer.  """
   return n > 0



def count_elements(lst, predicate):
    """  Counts the number of integers in list lst that are 
         acceptable to a given predicate (Boolean function).  
         Prints an error message and raises a type error if
         the list contains an element incompatible with 
         the predicate.  """
    count = 0
    for x in lst:
        try:
            if predicate(x):
                count += 1
        except TypeError:
            print(x, 'is a not an acceptable element')
            raise    # Re-raise the caught exception
    return count


def main():
    print(count_elements([3, -71, 22, -19, 2, 9], non_neg))
    print(count_elements([2, 3, 4, 5, 6, 8, 9], is_prime))
    print(count_elements([2, 4, '6', 8, 'x', 7], is_prime))


if __name__ == '__main__':
    main()
