lst = [10, 20, 30, 40, 50]
t = 100, 200, 300, 400, 500
d = {"A": 4, "B": 18, "C": 0, "D": 3}
s = {1000, 2000, 3000, 4000, 5000}
print(lst)
print(t)
print(d)
print(s)
for x in enumerate(lst):
    print(x, end=" ")
print()
for x in enumerate(t):
    print(x, end=" ")
print()
for x in enumerate(d):
    print(x, end=" ")
print()
for x in enumerate(s):
    print(x, end=" ")
print()


def gen(n):
    """  Generate n, n - 2, n - 3, ..., 0. """
    for i in range(n, -1, -2):
        yield i


for x in enumerate(gen(20)):
    print(x, end=" ")
print()

# Optionally specify beginning index
for x in enumerate(t, 1):
    print(x, end=" ")
print()
