from time import clock

max_value = 10000
count = 0
start_time = clock()   # Start timer
#  Try values from 2 (smallest prime number) to max_value
for value in range(2, max_value + 1):
    # See if value is prime
    is_prime = True  # Provisionally, value is prime
    # Try all possible factors from 2 to value - 1
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False    # Found a factor
            break               # No need to continue; it is NOT prime
    if is_prime:
        count += 1              # Count the prime number
print()  # Move cursor down to next line
elapsed = clock() - start_time  # Stop the timer
print("Count:", count, "  Elapsed time:", elapsed, "sec")
