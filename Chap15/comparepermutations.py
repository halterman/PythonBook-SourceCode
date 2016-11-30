from random import randrange

#  Randomly permute a list
def permute(lst):
    """
    Randomly permutes the contents of list lst
    """
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(i, n)    # i <= pos < n
        lst[i], lst[pos] = lst[pos], lst[i]


#  Randomly permute a list?
def faulty_permute(lst):
    """
    An attempt to randomly permute the contents of list lst
    """
    n = len(lst)
    for i in range(n):
        pos = randrange(0, n)   # 0 <= pos < n 
        lst[i], lst[pos] = lst[pos], lst[i]


def classify(a):
    """
    Classify a list as one of the six permutations
    """
    sum = 100*a[0] + 10*a[1] + a[2]
    if sum == 123:   return 0
    elif sum == 132: return 1
    elif sum == 213: return 2
    elif sum == 231: return 3
    elif sum == 312: return 4
    elif sum == 321: return 5
    else: return -1


def report(a):
    """
    Report the accumulated statistics
    """
    print("1,2,3: ", a[0])
    print("1,3,2: ", a[1])
    print("2,1,3: ", a[2])
    print("2,3,1: ", a[3])
    print("3,1,2: ", a[4])
    print("3,2,1: ", a[5])


def run_test(perm, runs):
    """
    Uses a permutation function to generate the permutations
    of the list [1,2,3]
    perm: the permutation function to test
    runs: the number permutations to perform
    """
    # The list to permute
    original = [1, 2, 3]

    # permutation_tally list keeps track of each permutation pattern
    # permutation_tally[0] counts {1,2,3}
    # permutation_tally[1] counts {1,3,2}
    # permutation_tally[2] counts {2,1,3}
    # permutation_tally[3] counts {2,3,1}
    # permutation_tally[4] counts {3,1,2}
    # permutation_tally[5] counts {3,2,1}
    permutation_tally = 6 * [0]  # Clear all the counters
    for i in range(runs):    # Run runs times
        # working holds a copy of original is gets permuted and tallied
        working = original[:]
        # Permute the list with the permutation algorithm
        perm(working)
        # Count this permutation
        permutation_tally[classify(working)] += 1
    report(permutation_tally)   # Report results


def main():
    # Each test performs one million permutations
    runs = 1000000

    print("--- Random permute #1 -----")
    run_test(permute, runs)

    print("--- Random permute #2 -----")
    run_test(faulty_permute, runs)


main()
