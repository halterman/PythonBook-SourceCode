from time import clock

sum = 0          # Initialize sum accumulator
start = clock()  # Start the stopwatch
for n in range(1, 100000001):   #  Sum the numbers
    sum += n
elapsed = clock() - start  #  Stop the stopwatch
print("sum:", sum, "time:", elapsed)  # Report results
