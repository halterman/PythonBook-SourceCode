from time import clock
from math import sqrt
from plotobj import Plotter


def is_ascending(lst):
    """ Returns True if lst contains elements
        in nondecreasing order as determined by
        the < operator.  Returns False if the 
        elements of lst are not in order.  Throws
        an exception if lst is not a list or its
        elements are not compatible with the <
        operator. """
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                return False
    return True


def is_ascending2(lst):
    """ Returns True if lst contains elements
        in nondecreasing order as determined by
        the < operator.  Returns False if the 
        elements of lst are not in order.  Throws
        an exception if lst is not a list or its
        elements are not compatible with the <
        operator. """
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
 

def compute_time(size, data1, data2):
    """ Compares the performance of the is_ascending and 
        is_ascending2 functions on a list of a given size. 
        Prints the results of the executions and appends the
        results to the data1 and data2 lists for further processing. """

    print("List size:", size)
    my_list = list(range(size))   #  Make list [0, 1, 2, 3, ..., size - 1]
    start = clock()               # Start the clock
    ans = is_ascending(my_list)   # Compute answer
    elapsed1 = clock() - start    # Stop the clock
    print("  is_ascending:  {} Elapsed: {:12.7f}".format(ans, elapsed1))
    start = clock()               # Start the clock
    ans = is_ascending2(my_list)  # Compute answer
    elapsed2 = clock() - start    # Stop the clockt
    print("  is_ascending2: {} Elapsed: {:12.7f}".format(ans, elapsed2))
    print("  Speedup: {:6.1f}".format(elapsed1/elapsed2)) # Compute speedup
    print()
    data1.append((size, elapsed1))
    data2.append((size, elapsed2))


def main():
    """ Compares the performance of the is_ascending and 
        is_ascending2 functions on lists of various sizes. """
    data1, data2 = [], []

    # Compute results for sizes in the range 0...40,000
    max_size = 40000
    # Sizes used are 0**2 = 0, 20**2 = 400, 40**2 = 1600, 60**2 = 3600, 
    # etc. up to 200**2 = 40,000
    for size in (x**2 for x in range(0, round(sqrt(max_size)) + 1, 20)):
        compute_time(size, data1, data2)

    # Create a plotter object
    plt = Plotter(600, 600, 0, max_size, 0, 120)

    # Plot the curves
    plt.pen.width(4)
    plt.plot_data(data1, "blue")
    plt.plot_data(data2, "red")

    # Wait for user interaction
    plt.interact()


if __name__ == '__main__':
    main()
