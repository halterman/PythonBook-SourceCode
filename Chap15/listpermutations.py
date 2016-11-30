def perm(lst, begin, result):
    """ Creates a list (result) containing all the permutations of the
        elements of a given list (lst), beginning with a
        specified index (begin).  
        This is a helper function for the permutations function.  """
    end = len(lst) - 1  # Index of the last element
    if begin == end:
        result += [lst[:]]   # Copy lst into result
    else:
        for i in range(begin, end + 1):  # Consider all indices
            # Interchange the element at the first position 
            # with the element at position i
            lst[begin], lst[i] = lst[i], lst[begin] 
            # Recursively permute the rest of the list
            perm(lst, begin + 1, result)
            # Undo the earlier interchange
            lst[begin], lst[i] = lst[i], lst[begin] 


def permutations(lst):
    """  Returns a list containing all the permutations of the
         orderings of the elements of a given list (lst).
         Delegates the hard work to the perm function. """
    result = []
    perm(lst, 0, result)
    return result


def main():
    """  Tests the permutations function.  """
    a = list(range(3))  # Make list [0, 1, 2]
    print('List:', a)   # Print the list
    # Generate and print all permutations of the list
    print('Permutations:', permutations(a))


if __name__ == '__main__':
    main()
