#  Contains the definition of the is_prime function
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
    """  Experiments with the prime number generator """
    min_value = int(input("Enter start of range: "))
    max_value = int(input("Enter last of range: "))

    print('Print all the primes from', min_value, 'to', max_value)
    for value in prime_sequence(min_value, max_value):
        print(value, end=' ')   # Display the prime number
    print()  # Move cursor down to next line

    print('Print all the primes in that range that end with digit 3')
    for value in prime_sequence(min_value, max_value):
        if value % 10 == 3:         # See if value's ones digit is 3
            print(value, end=' ')   # Display the number
    print()  # Move cursor down to next line

    # Add up all the primes in the range
    sum = 0
    for value in prime_sequence(min_value, max_value):
        sum += value
    print('The sum of the primes in that range is', sum)

    # Decorate the output
    print('Fancier display')
    for value in prime_sequence(min_value, max_value):
        print('<' + str(value) + '>', end='')


if __name__ == '__main__':
    main()   # Run the program
