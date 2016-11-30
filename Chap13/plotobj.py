""" Provides the Plotter class that clients can use to 
    draw graphs of a mathematical functions on a Cartesian 
    coordinate plane. """

from turtle import Pen, Screen
from math import atan2, pi


class Plotter:
    """ A plotter object provides a graphical window for 
        plotting data and mathematical functions. """

    def __init__(self, width, height, min_x, max_x, min_y, max_y):
        """ Initializes the plotter with a window that is 
            width wide and height high.  Its x-axis ranges from
            min_x to max_x, and its y-axis ranges from
            min_y to max_y.  Establishes the global beginning and ending
            x values for the plot and the x_increment value.
            Draws the x- and y-axes. """

        self.pen = Pen()   #  The plotter object's pen
        self.screen = Screen()   #  The plotter object's screen

        self.pen.speed(0)            # Speed up rendering
        self.screen.tracer(0, 0)        # Do not draw pen while drawing
        # Establish global x and y ranges
        self.min_x, self.max_x = min_x, max_x
        self.min_y, self.max_y = min_y, max_y
        # Set up window size, in pixels
        self.screen.setup(width=width, height=height)
        # Set up screen size, in pixels
        self.screen.screensize(width, height)
        self.screen.setworldcoordinates(min_x, min_y, max_x, max_y)

        # x-axis distance that corresponds to one pixel in window distance
        self.x_increment = (max_x - min_x)/width
        self.draw_grid(20)
        self.draw_axes()
        self.screen.title("Plot")
        self.screen.update()

    def __del__(self):
        """ Called when the client no longer uses the plotter 
            object. """
        print("Done plotting")

    def draw_axes(self, grid=False):
        """ Draws the x and y axes within the plotting window. 
            The grid parameter controls the drawing of accessory
            horizontal and vertical lines. """
        if grid:
            self.draw_grid(20)
        self.pen.hideturtle()            # Make pen invisible
        prev_width = self.pen.width()
        self.pen.width(2)
        #  Draw x axis
        self.pen.color('black')
        self.draw_arrow(self.min_x, 0, self.max_x, 0) 
        #  Draw y axis
        self.draw_arrow(0, self.min_y, 0, self.max_y) 
        self.pen.width(prev_width)

    def draw_grid(self, n):
        """ Draws horizontal and vertical accessory reference 
            coordinate lines on the plot.  Parameter n controls 
            the frequency of the reference lines. """
        self.pen.up()
        #self.pen.setposition(self.min_x, self.min_y)
        inc = (self.max_x - self.min_x)/n
        self.pen.color("lightblue")
        x = self.min_x
        while x <= self.max_x:
            self.pen.setposition(x, self.min_y)
            self.pen.down()
            self.pen.setposition(x, self.max_y)
            self.pen.up()
            x += inc  # Next x
        inc = (self.max_y - self.min_y)/n
        y = self.min_y
        while y <= self.max_y:
            self.pen.setposition(self.min_x, y)
            self.pen.down()
            self.pen.setposition(self.max_x, y)
            self.pen.up()
            y += inc  # Next y

    def draw_arrow(self, x1, y1, x2, y2):
        """ Draws an arrow starting at (x1, y1) and ending at
            (x2, y2). """
        # Draw arrow shaft
        self.pen.up()
        self.pen.setposition(x1, y1) # Move the pen starting point
        self.pen.down()           # Draw line bottom to top
        self.pen.setposition(x2, y2) # Move the pen starting point
        # Draw arrow head
        dy = y2 - y1
        dx = x2 - x1
        angle = atan2(dy, dx) *180/pi
        self.pen.setheading(angle)
        self.pen.stamp()

    def plot_function(self, f, color, update=True):
        """ Plots function f on the Cartesian coordinate plane
            established by initialize_plotter. Plots (x, f(x)), 
            for all x in the range min_x <= x < max_x. 
            The color parameter dictates the curve's color. """
    
        #  Move pen to starting position
        self.pen.up()
        self.pen.setposition(self.min_x, f(self.min_x))
        self.pen.color(color)
        self.pen.down()
        # Iterate over the range of x values for min_x <= x < max_x
        x = self.min_x
        while x < self.max_x:
            self.pen.setposition(x, f(x))
            x += self.x_increment   # Next x

        if update:
            self.screen.update()

    def plot_data(self, data, color, update=True):
        """ Plots the (x, y) pairs of values in the data list.
            The curve's color is specified by the color parameter. """
        #  Move pen to starting position
        self.pen.up()
        self.pen.setposition(data[0][0], data[0][1])
        self.pen.color(color)
        self.pen.down()
        # Plot the points in the data set
        for x, y in data:
            self.pen.setposition(x, y)
        if update:
            self.screen.update()

    def update(self):
        """ Draws any pending plotting actions to the screen. """
        self.screen.update()

    def setcolor(self, color):
        """ Sets the current drawing color. """
        self.pen.color(color)

    def onclick(self, fun):
        """ This method assigns a function to call when the user
            clicks the mouse over the plotting window.  The
            function must accept two integer parameters that
            represent the (x, y) location of the mouse when the
            click occurred. """
        self.screen.onclick(fun)
    
    def interact(self):
        """ Places the plotting object in interactive mode so the
            user can provide input via the mouse or keyboard. """
        self.screen.mainloop()
