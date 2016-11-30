from random import randrange

def show_call_and_return_details(f):
    """ Decorates a function f so its call will display the
        parameter values and return value. """ 
    func_name = f.__name__   # Get the function's name
    def execute_augmented(x, y):
        call_string = "{}({}, {})".format(func_name, x, y)
        print(">>> Calling " + call_string)
        result = f(x, y)
        print("<<< Returning {} from ".format(result) + call_string)
        return result
    return execute_augmented

@show_call_and_return_details
def max(x, y):
    """ Determine the maximum of x and y """
    return x if x > y else y

@show_call_and_return_details
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

@show_call_and_return_details
def summation(begin, end):
    """ Add up the integers in the range begin...end - 1, inclusive """
    sum = 0
    while begin != end:
        sum += begin
        begin += 1
    return sum

@show_call_and_return_details
def star_rect(length, width):
    """ Draw a length x width rectangle with asterisks """
    for row in range(length):
        print('* ' * width)


# Decorate the randrange function as before; we cannot alter its
# source code
randrange = show_call_and_return_details(randrange)

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
