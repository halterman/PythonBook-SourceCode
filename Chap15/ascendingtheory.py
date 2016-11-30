from time import clock
from math import sqrt
from plotobj import Plotter


def main():
    """ Compares the theoretical performance of the is_ascending and 
        is_ascending2 functions on lists of various sizes. """
    data1, data2 = [], []

    # Compute results for sizes in the range 0...40,000
    max_size = 40000
    # Sizes used are 0**2 = 0, 20**2 = 400, 40**2 = 1600, 60**2 = 3600, 
    # etc. up to 200**2 = 40,000

    # Create a plotter object
    plt = Plotter(600, 600, 0, max_size, 0, 750000000)

    # Plot the curves
    plt.pen.width(4)
    data1 = [(x, (x**2 - x)/2) for x in 
                 (x**2 for x in range(0, round(sqrt(max_size)) + 1, 20))]
    data2 = [(x, x - 1) for x in 
                 (x**2 for x in range(0, round(sqrt(max_size)) + 1, 20))]

    plt.plot_data(data1, "green")
    plt.plot_data(data2, "brown")

    plt.interact()


if __name__ == '__main__':
    main()
