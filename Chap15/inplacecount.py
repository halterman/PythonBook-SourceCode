def count_helper(lst, pos, item):
    """  Counts the number of occurrences of item within the list
         lst.  pos represents the current position under
         examination within the list.  """
    if pos == len(lst):   # Are we past the end of the list?
        return 0         # Nothing can appear past the end
    else:
        # Count the occurrences in the rest of the list 
        # (all but the first element)
        count_rest = count_helper(lst, pos + 1, item)   
        if lst[pos] == item:
            return 1 + count_rest
        else:
            return count_rest
 

def count(lst, item):
    """  Counts the number of occurrences of item within the list
         lst.  Delegates the work to the recursive count_helper
         function, passing zero as the initial position (which is
         the index of the first element in the list).  """
    return count_helper(lst, 0, item)
 

def main():
        lst1 = [21, 19, 31, 22, 14, 31, 22, 6, 31]
        print(count(lst1, 31))
        lst2 = ['FRED', [2, 3], 44, 'WILMA', 'FRED', 8, 'BARNEY']
        print(count(lst2, 'FRED'))
        print(count(lst2, 'BETTY'))
        print(count([], 16))


if __name__ == '__main__':
    main()
