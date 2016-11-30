""" Provides the plot function that draws the graph of a mathematical
    function on a Cartesian coordinate plane. """

import turtle


def initialize_plotter(width, height, min_x, max_x, min_y, max_y):
    """ Initializes the plotter with a window with dimensions
        width x height, the x-axis ranging from
        min_x to max_x, and the y-axis ranging from
        min_y to max_y.  Establishes the global beginning and ending
        x values for the plot and the global x_increment value.
        Draws the x- and y-axes. """

    # Global variables that the plot function must access
    global x_begin, x_end, x_increment

    #turtle.tracer(1, 0)            # Speed up rendering
    turtle.delay(0)            # Speed up rendering
    # Establish global x and y ranges
    x_begin, x_end = min_x, max_x
    # Set up window size, in pixels
    turtle.setup(width=width, height=height)
    # Set up screen size, in pixels
    turtle.screensize(width, height)
    turtle.setworldcoordinates(min_x, min_y, max_x, max_y)

    # x-axis distance that corresponds to one pixel in window distance
    x_increment = (max_x - min_x)/width

    turtle.hideturtle()            # Make pen invisible
    #  Draw x axis
    turtle.pencolor('black')
    turtle.penup()
    turtle.setposition(min_x, 0)   # Move the pen to the left, center 
    turtle.setheading(0)           # Aim the pen right 
    turtle.pendown()
    turtle.forward(max_x - min_x)  #  Draw a line left to right

    #  Draw y axis
    turtle.penup()
    turtle.setposition(0, min_y)   # Move the pen to the center, bottom 
    turtle.setheading(90)          # Aim the pen up 
    turtle.pendown()               # Draw line bottom to top
    turtle.forward(max_y - min_y)


def plot(f, color):
    """ Plots function f on the Cartesian coordinate plane
        established by initialize_plotter. Plots (x, f(x)), 
        for all x in the range x_begin <= x < x_end. 
        The color parameter dictates the curve's color. """

    #  Move pen to starting position
    turtle.penup()
    turtle.setposition(x_begin, f(x_begin))
    turtle.pencolor(color)
    turtle.pendown()
    # Iterate over the range of x values for x_begin <= x < x_end
    x = x_begin
    while x < x_end:
        turtle.setposition(x, f(x))
        x += x_increment   # Next x
    

def finish_plotting():
    turtle.exitonclick()


def quad(x):    #  Quadratic function (parabola)
    return 1/2 * x**2 + 3


def main():
    """ Provides a simple test of the plot function. """
    from math import sin
    initialize_plotter(600, 600, -10, 10, -10, 10)
    #  Plot f(x) = 1/2*x + 3, for -10 <= x < 100
    plot(quad, 'red')
    #  Plot f(x) = x, for -10 <= x < 100
    plot(lambda x: x, 'blue')
    #  Plot f(x) = 3 sin x, for -10 <= x < 100
    plot(lambda x: 3*sin(x), 'green')
    finish_plotting()


if __name__ == '__main__':
    main()
