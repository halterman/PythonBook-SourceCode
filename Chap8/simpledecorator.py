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


# Decorate the functions to provide information about their calls
# We can make up a new name
augmented_max = show_call_and_return_details(max)
# Or, more typically, simply redirect the original name to a new function!
gcd = show_call_and_return_details(gcd)
summation = show_call_and_return_details(summation)
star_rect = show_call_and_return_details(star_rect)
randrange = show_call_and_return_details(randrange)

augmented_max(20, 30)
print('------------------------')
augmented_max(30, 20)
print('------------------------')
augmented_max(20, 20)
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
