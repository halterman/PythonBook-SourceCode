from plotobj import Plotter
from math import sin


def quad(x): 
    """ Quadratic function (parabola) """
    return 1/2 * x**2 + 3


def arrow_wheel(plotter, x, y, len, angle, color):
    """ Draws a collection of arrows extending radially from
        an (x, y) center point.  The arrows all are len long, the
        angle parameter specifes the angle between each adjacent
        arrow, and color specifies their color. """
    from math import cos, sin, radians
    COS_theta = cos(radians(angle))
    SIN_theta = sin(radians(angle))
    plotter.setcolor(color)
    xe, ye = len, 0.0
    for i in range(360//angle):
        xe, ye = xe*COS_theta - ye*SIN_theta, xe*SIN_theta + ye*COS_theta 
        plotter.draw_arrow(x, y, xe + x, ye + y)


def main():
    """ Provides a simple test of the plotting object. """
    from math import sin

    def run_test(x, y):
        """ Generate an arrow wheel centered at (x, y) with 
            random size and color. """
        #test_arrow(plt)
        from random import randrange
        colors = ["red", "green", "blue", "black"]
        arrow_wheel(plt, x, y, randrange(10) + 1, 10, colors[randrange(4)])

    # Create a plotter object
    plt = Plotter(600, 600, -10, 10, -10, 10)
    #  Plot f(x) = 1/2*x + 3, for -10 <= x < 100
    plt.plot_function(quad, 'red')
    #  Plot f(x) = x, for -10 <= x < 100
    plt.plot_function(lambda x: x, 'blue')
    #  Plot f(x) = 3 sin x, for -10 <= x < 100
    plt.plot_function(lambda x: 3*sin(x), 'green')

    # Execute the run_test function when the user clicks the mouse
    plt.onclick(run_test)
    #test_arrow(plt)

    plt.interact()


if __name__ == '__main__':
    main()
