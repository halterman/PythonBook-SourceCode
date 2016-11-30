def gen(n):
    """ Generates the first n perfect squares, starting with zero:
        0, 1, 4, 9, 16,..., (n - 1)^2. """
    for i in range(n):
        yield i**2


for p in zip([10, 20, 30, 40, 50, 60], gen(4)):
    print(p, end=' ')
print()
