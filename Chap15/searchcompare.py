"""
Compares the running times of linear search and
binary search on lists of various sizes.
"""

def binary_search(lst, seek):
    """
    Returns the index of element seek in list lst,
    if seek is present in lst.
    lst must be in sorted order.
    Returns None if seek is not an element of lst.
    lst is the list in which to search.
    seek is the element to find.
    """
    first = 0            # Initially the first element in list
    last = len(lst) - 1  # Initially the last element in list
    while first <= last: 
        # mid is middle of the list
        mid = first + (last - first + 1)//2  # Note: Integer division
        if lst[mid] == seek:
            return mid       # Found it
        elif lst[mid] > seek:
            last = mid - 1   # continue with 1st half
        else:  # v[mid] < seek
            first = mid + 1  # continue with 2nd half
    return None    # Not there


def ordered_linear_search(lst, seek):
    """
    Returns the index of element seek in list lst,
    if seek is present in lst.
    lst must be in sorted order.
    Returns None if seek is not an element of lst.
    lst is the list in which to search.
    seek is the element to find.
    """
    i = 0
    n = len(lst)
    while i < n and lst[i] <= seek:
        if lst[i] == seek:
            return i      # Return position immediately
        i += 1
    return None           # Element not found


def run_search(lst, seeks, search, trials):
    """
    Searches for all the elements in an ordered list (lst)
    using search function search.  Averages the running time over
    trials runs.  Returns the average time.
    """
    from time import clock
    n = len(lst)
    elapsed = 0
    start = clock()    # Start the clock
    for i in range(trials):
        for elem in seeks:
            i = search(lst, elem)
            if i != lst[i]:
                print("error")
    stop = clock()     # Stop the clock
    elapsed += stop - start
    return elapsed/trials    # Average time for search


def test_searches(lst, seeks, trials):
    """
    Measures the running times of ordered linear search and binary
    search on a given list.  Averages the times over n runs.
    """
    # Find each element using ordered linear search
    lin = run_search(lst, seeks, ordered_linear_search, trials)
    # Find each element using binary search
    bin = run_search(lst, seeks, binary_search, trials)
    # Print the results
    print('{0:6} {1:10.5f} {2:10.5f} {3:8.1f}'\
              .format(len(lst), lin, bin, lin/bin))


def make_search_set(n):
    """
    Make a list of elements to seek
    """
    from random import randrange
    result = []
    for i in range(n):
        result += [randrange(n)]
    return result


def main():
    """
    Makes a table comparing the running times of ordered linear
    search vs. binary search on lists of various sizes.
    """
    # Number of trials over which to average the results
    trials = 10


    # Print table header
    print('   Size    Linear     Binary    Speedup')
    print('-----------------------------------------')
    # Small lists: 10 to 100, in steps of 10
    for size in range(10, 100, 10):
        test_list = list(range(size))
        seek_list = make_search_set(size)
        test_searches(test_list, seek_list, trials)
    # Medium lists: 100 to 1,000, in steps of 100
    for size in range(100, 1000, 100):
        test_list = list(range(size))
        seek_list = make_search_set(size)
        test_searches(test_list, seek_list, trials)
    # Large lists: 1,000 to 5,000, in steps of 500
    for size in range(1000, 5001, 500):
        test_list = list(range(size))
        seek_list = make_search_set(size)
        test_searches(test_list, seek_list, trials)


if __name__ == '__main__':
    main()
