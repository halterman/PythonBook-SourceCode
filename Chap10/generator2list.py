from math import sqrt

def is_prime(n):
    """  Returns True if nonnegative integer n is prime; 
         otherwise, returns false """
    if n == 2:                      # 2 is the only even prime number
        return True
    if n < 2 or n % 2 == 0:         # Handle simple cases immediately
        return False                # No evens and nothing less than 2
    trial_factor = 3
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:   # Is trial factor a factor?
            return False            # Yes, return right away
        trial_factor += 2           # Next potential factor, skip evens
    return True                     # Tried them all, must be prime


def prime_sequence(begin, end):
    """  Generates the sequence of prime numbers between begin and end.  """
    for value in range(begin, end + 1):
        if is_prime(value):         # See if value is prime
            yield value             # Produce the prime number


def main():
    """  Make a list from a generator """
    # Build the list of prime numbers in the range 20 to 50
    primes = list(prime_sequence(20, 50))
    print(primes)


if __name__ == '__main__':
    main()   # Run the program
