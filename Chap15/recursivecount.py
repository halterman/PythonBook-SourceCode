def count(lst, item):
    """  Counts the number of occurrences of item within the list lst """
    if len(lst) == 0:    # Is the list empty?
        return 0         # Nothing can appear in an empty list
    else:
        # Count the occurrences in the rest of the list 
        # (all but the first element)
        count_rest = count(lst[1:], item)   
        if lst[0] == item:
            return 1 + count_rest
        else:
            return count_rest
 

def main():
        lst1 = [21, 19, 31, 22, 14, 31, 22, 6, 31]
        print(count(lst1, 31))
        lst2 = ['FRED', [2, 3], 44, 'WILMA', 'FRED', 8, 'BARNEY']
        print(count(lst2, 'FRED'))
        print(count(lst2, 'BETTY'))
        print(count([], 16))


if __name__ == '__main__':
    main()
