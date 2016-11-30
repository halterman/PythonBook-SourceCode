
def count(lst, item):
    """  Counts the number of occurrences of item within the list
         lst.  Delegates the work to the recursive count_helper
         function, passing zero as the initial position (which is
         the index of the first element in the list).  """

    def count_helper(pos):
        """  Local function counts the number of occurrences of an
             item within a list.  
             pos represents the current position under examination 
                 within the list.  
             lst and item are nonlocal variables from the outer context. """
        if pos == len(lst):   # Are we past the end of the list?
            return 0         # Nothing can appear past the end
        else:
            # Count the occurrences in the rest of the list 
            # (all but the first element)
            count_rest = count_helper(pos + 1)   
            if lst[pos] == item:
                return 1 + count_rest
            else:
                return count_rest
     
    # Body of count function
    return count_helper(0)
 

def main():
        lst1 = [21, 19, 31, 22, 14, 31, 22, 6, 31]
        print(count(lst1, 31))
        lst2 = ['FRED', [2, 3], 44, 'WILMA', 'FRED', 8, 'BARNEY']
        print(count(lst2, 'FRED'))
        print(count(lst2, 'BETTY'))
        print(count([], 16))


if __name__ == '__main__':
    main()
