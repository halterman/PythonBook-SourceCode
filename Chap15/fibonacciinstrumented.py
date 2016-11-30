# This dictionary will keep track of the number of calls to the 
# fibonacci function.
call_counter = {}

def fibonacci(n):
    """ Returns the nth Fibonacci number. """
    # Count the call
    if n not in call_counter:
        call_counter[n] = 1 
    else:
        call_counter[n] += 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# Call fibonacci(5)
print("fibonacci(5) = ", fibonacci(5))
print()

# Report the total number of calls to the fibonacci function
print("Argument    Calls")
print("-----------------")
for args, calls in sorted(call_counter.items()):
    print("   ", args, "         ", calls);
