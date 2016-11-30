def perm(lst, begin, result, depth):
    """ Creates a list (result) containing all the permutations of the
        elements of a given list (lst), beginning with a
        specified index (begin).  
        Printing statements report the progression of the
        function's recursion.  The depth parameter indicates the
        depth of the recursion.
        This is a helper function for the permutations function.  """
    print('   ' * depth, 'begin =', begin)
    end = len(lst) - 1  # Index of the last element
    if begin == end:
        result += [lst[:]]   # Copy lst into result
        print('   ' * depth, '  *')
    else:
        for i in range(begin, end + 1):
            # Interchange the element at the first position 
            # with the element at position i
            lst[begin], lst[i] = lst[i], lst[begin] 
            print('   ' * depth, '  ', lst[begin], '<-->', lst[i], '  ', lst)
            # Recursively permute the rest of the list
            perm(lst, begin + 1, result, depth + 1)
            # Undo the earlier interchange
            lst[begin], lst[i] = lst[i], lst[begin] 


def permutations(lst):
    """  Returns a list containing all the permutations of the
         orderings of the elements of a given list (lst).
         Delegates the hard work to the perm function. """
    result = []
    perm(lst, 0, result, 0)  # Initial call with depth = 0
    return result


def main():
    a = list(range(3))
    print(permutations(a))


if __name__ == '__main__':
    main()
