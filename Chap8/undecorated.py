from random import randrange


def max(x, y):
    """ Determine the maximum of x and y """
    return x if x > y else y

def gcd(m, n):
    """
    Uses Euclid's method to compute the greatest common divisor 
    (also called greatest common factor) of  m and n.
    Returns the GCD of m and n.
    """
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def summation(begin, end):
    """ Add up the integers in the range begin...end - 1, inclusive """
    sum = 0
    while begin != end:
        sum += begin
        begin += 1
    return sum

def star_rect(length, width):
    """ Draw a length x width rectangle with asterisks """
    for row in range(length):
        print('* ' * width)


print("The maximum of 20 and 30 is", max(20, 30))
print("The maximum of 30 and 20 is", max(30, 20))
print("The maximum of 20 and 20 is", max(20, 20))
print('------------------------')

print("The GCD of 20 and 30 is", gcd(20, 30))
print("The GCD of 30 and 20 is", gcd(30, 20))
print("The GCD of 20 and 20 is", gcd(20, 20))
print('------------------------')

print("The summation from 20 to 30 is", summation(20, 30))
print('------------------------')

star_rect(7, 3)
print('------------------------')
star_rect(4, 4)
print('------------------------')
star_rect(2, 5)
print('------------------------')

print(randrange(10, 21), "is a pseudorandom integer in the range 10 to 20, inclusive")
