from random import randrange


def max(x, y):
    """ Determine the maximum of x and y """
    call_string = "max({}, {})".format(x, y)
    print(">>> Calling " + call_string)
    result = x if x > y else y
    print("<<< Returning {} from ".format(result) + call_string)
    return result

def gcd(m, n):
    """
    Uses Euclid's method to compute the greatest common divisor 
    (also called greatest common factor) of  m and n.
    Returns the GCD of m and n.
    """
    call_string = "gcd({}, {})".format(m, n)
    print(">>> Calling " + call_string)
    if n == 0:
        result = m
    else:
        result = gcd(n, m % n)
    print("<<< Returning {} from ".format(result) + call_string)
    return result

def summation(begin, end):
    """ Add up the integers in the range begin...end - 1, inclusive """
    call_string = "summation({}, {})".format(begin, end)
    print(">>> Calling " + call_string)
    sum = 0
    while begin != end:
        sum += begin
        begin += 1
    print("<<< Returning {} from ".format(sum) + call_string)
    return sum
 
def star_rect(length, width):
    """ Draw a length x width rectangle with asterisks """
    call_string = "star_rect({}, {})".format(length, width)
    print(">>> Calling " + call_string)
    for row in range(length):
        print('* ' * width)
    print("<<< Returning {} from ".format(None) + call_string)

# This time just call the functions, and let each function print its
# parameter and result details.
max(20, 30)
print('------------------------')
max(30, 20)
print('------------------------')
max(20, 20)
print('------------------------')

gcd(20, 30)
print('------------------------')
gcd(30, 20)
print('------------------------')
gcd(20, 20)
print('------------------------')

summation(20, 30)
print('------------------------')

star_rect(7, 3)
print('------------------------')
star_rect(4, 4)
print('------------------------')
star_rect(2, 5)
print('------------------------')

print(randrange(10, 21), "is a pseudorandom integer in the range 10 to 20, inclusive")
