from time import clock
from random import randrange


def fibonacci(n):
    """ Returns the nth Fibonacci number recursively. """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Dictionary for caching the results of the fibonacci2 function
ans = {0:0, 1:1}  # Precompute the results for 0 and 1

def fibonacci2(n):
    """ Returns the nth Fibonacci number.  Caches a
        recursively computed result to be used when needed
        in the future.  Provides a huge performance improvement
        over the recursive version.  """
    if n not in ans.keys():
        result = fibonacci2(n - 2) + fibonacci2(n - 1)
        ans[n] = result
    return ans[n]


def time_it(f, ns):
    """ f is a function that accepts a single parameter.
        ns is a list.
        Measures the time for function f to process each element in ns.
        Returns the cumulative elapsed time. """ 
    start_time = clock()
    for i in ns:
        #print("{:>4}: {:>8}".format(i, f(i)))
        print(f(i), end=" ")
    end_time = clock()
    return end_time - start_time  #  Return elapsed time


def main():
    """ Tests the performance of the fibonacci and fibonacci2 functions. """

    # Make a list of pseudorandom integers in the range 1...50
    numbers = []
    for i in range(10):
        numbers.append(randrange(40) + 1)
    
    # Print the numbers
    print(numbers)
    
    # Compare the two Fibonacci functions
    print("Time:", time_it(fibonacci, numbers))
    print("------------------")
    print("Time:", time_it(fibonacci2, numbers))


if __name__ == "__main__":
    main()
