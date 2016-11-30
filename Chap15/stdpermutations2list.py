#  Use the standard permutations function to list
#  the possible arrangements of elements in a list.

from itertools import permutations


def main():
    a = [0, 1, 2]
    for p in permutations(a):
        print(list(p), end=' ')
    print()


main()
