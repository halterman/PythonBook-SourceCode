import turtle

def report_position(x, y):
    """ Simply prints the values of x and y. """
    print("x =", x, "  y =", y, flush=True)

# Establish a function the framework should call when the user clicks the mouse
turtle.onscreenclick(report_position)

# Start the graphics loop that listens for user input
turtle.mainloop()
