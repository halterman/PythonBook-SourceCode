#  Use the standard permutations function to list
#  the possible arrangements of elements in a list.

from itertools import permutations


def main():
    a = [0, 1, 2]
    for p in permutations(a):
        print(p, end=' ')
    print()


main()
