from stopwatch import Stopwatch # Our Stopwatch class from before
from random import choice
from turtle import *

def LCS(X, Y):
    """ Computes the longest common subsequence of strings X and Y. """

    result = ''  # No symbols in common unless determined otherwise
    if len(X) > 0 and len(Y) > 0:  #  No symbols in common if either string is empty
        Xrest = X[1:]   #  String X without its first symbol
        Yrest = Y[1:]   #  String Y without its first symbol
        if X[0] == Y[0]:  # Do the first symbols of both strings match?
            # An LCS will include this shared symbol plus the LCS of rest 
            # of both strings
            result = X[0] + LCS(Xrest, Yrest)
        else:
            # Compare string X to the string Y, excluding Y's first symbol
            X_Y1 = LCS(X, Yrest)
            # Compare string X, excluding X's first symbol, to string Y
            X1_Y = LCS(Xrest, Y)
            #  Choose longer of the two computed sequences
            result = X_Y1 if len(X_Y1) > len(X1_Y) else X1_Y   
    return result


def LCS_memoized(X, Y):
    """ Computes the longest common subsequence of strings X and Y. 
        Caches intermediate results in a memoization dictionary so they
        do not need to be recomputed over and over again. """

    memo = {}   # Start with empty memoization storage

    def LCS(X, Y):
        """ Computes the longest common subsequence of strings X and Y. """
        nonlocal memo  # Memoization storage for computed results
        # Check first to see if we already have computed
        if (X, Y) in memo:  
            result = memo[X, Y]   # LCS of X and Y already computed, so use previous value
        else:
            result = ''   # No symbols in common unless determined otherwise
            if len(X) > 0 and len(Y) > 0:  #  No symbols in common if either string is empty
                Xrest = X[1:]   #  String X without its first symbol
                Yrest = Y[1:]   #  String Y without its first symbol
                if X[0] == Y[0]:  # First symbols of both strings match
                    result = X[0] + LCS(Xrest, Yrest)
                else:
                    X_Y1 = LCS(X, Yrest)
                    X1_Y = LCS(Xrest, Y)
                    #  Choose longest
                    result = X_Y1 if len(X_Y1) > len(X1_Y) else X1_Y   
            # Remember this result for X and Y to avoid recomputing it in the future
            memo[X, Y] = result
        return result

    result =  LCS(X, Y)
    print("******** Stored memos:", len(memo))
    return result


def highlight(seq1, seq2):
    """ Highlights the characters of seq2 within seq1. """
    pos1, pos2 = 0, 0
    print(seq1)  # Print the string on one line
    while pos1 < len(seq1):
        if pos2 < len(seq2) and seq1[pos1] == seq2[pos2]:
            print('^', end='')  # Print "^" if characters match
            pos2 += 1
        else:
            print(' ', end='')  # Print a space to move to the next position
        pos1 += 1
    print()
    

def compare_LCS(seq1, seq2):
    """ Computes the longest common subsequence of seq 1 and seq2 in
        two different ways and compares the execution times of the two
        approaches. """
    timer_std = Stopwatch()     # Each function has its own stopwatch
    timer_memo = Stopwatch()    # to keep track of elapsed time independently
    timer_std.start()           # Time the standard LCS function
    subseq_std = LCS(seq1, seq2)
    timer_std.stop()
    timer_memo.start()          # Time the memoized LCS function
    subseq_memo = LCS_memoized(seq1, seq2)
    timer_memo.stop()
    # Report results
    print(seq1)
    print(seq2)
    print(subseq_std, len(subseq_std), '(Standard: {:f})'.format(timer_std.elapsed()))
    print(subseq_memo, len(subseq_memo), '(Memoized: {:f})'.format(timer_memo.elapsed()))
    print()
    # Show the computed longest common subsequences
    highlight(seq1, subseq_std)
    highlight(seq2, subseq_std)
    print()
    highlight(seq1, subseq_memo)
    highlight(seq2, subseq_memo)

    return timer_std.elapsed(), timer_memo.elapsed()

    
def build_random_string(n, symbols):
    """ Builds a string of length n with characters selected 
        pseudorandomly from the string parameter symbols. """
    result = ""
    while len(result) < n:
        result = result + choice(symbols)  # Add a random character from symbols
    return result


def plot(data):
    """ Plots the data from the LCS vs. Memoized LCS experiments. """

    # Compute bounds for the graphing
    w = window_width()
    h = window_height()
    x_origin = -w/2 + 15
    y_origin = -h/2 + 15
    
    xrange = len(data)   # Number of data points
    # Determine the range of y values
    yrange = max(max(data, key=lambda d0: d0[0])[0], 
                 max(data, key=lambda d1: d1[1])[1])

    # These scaling factors ensure the points will fit onto the plot
    xscale = 0.9*w/xrange
    yscale = 0.9*h/yrange

    def plot_curve(index, color):
        """ Local function to plot data from one of the functions.
            index refers to the slice of the data.
            color is the line and point color.  """
        penup()
        pencolor(color)
        setposition(x_origin, y_origin)
        pendown()
        for length, times in enumerate(data):
            setposition(x_origin + xscale*length, 
                        y_origin + yscale*times[index])
            dot()
            #print("Plotting", length, x_origin + xscale*length, 
            #      y_origin + yscale*times[index])


    hideturtle()  # Do not show the pen
    delay(0)      # No need to animate the drawing

    title("Longest Common Subsequence vs. Memoized LCS") 
    # Draw axes
    pencolor("black")
    pensize(3)
    penup()

    # x axis
    setposition(x_origin, y_origin)
    pendown()
    forward(w - 30)
    penup()
    # y axis
    setposition(x_origin, y_origin)
    left(90)
    pendown()
    forward(h - 30)
    pensize(2)

    # Draw first curve
    plot_curve(0, "blue")

    # Draw second curve
    plot_curve(1, "red")

    exitonclick()

def main():
    N = 10           # Number of times to perform a series of experiments
    max_length = 18  # Maximum string length for experiments

    #  Make a list of tuples for measuring the time to compute the
    #  LCS two different ways; initialize all the times to zero
    data = [(0, 0) for _ in range(max_length)]

    # Perform the series of experiments N times to produce
    # more reliable results
    for runs in range(N):
        # The series of experiments consists of computing the LCS
        # of two strings of increasing length
        for i in range(max_length):
            print(">>> Run", runs, "  String length", i)
            #  Construct two random DNA base sequences
            seq1 = build_random_string(i, "ACGT")
            seq2 = build_random_string(i, "ACGT")

            # Perform an experiment to time the two LCS functions
            lcs_time, memo_time = compare_LCS(seq1, seq2)
            # Accumulate the times
            data[i] = data[i][0] + lcs_time, data[i][1] + memo_time

    print(data)
    plot(data)


if __name__ == '__main__':
    main()
