"""  Draws in the window a spiral surrounded with an octogon  """

from turtle import *

def octogon(t, x, y, color):
    """  Draws with turtle t an octogon centered at (x, y) 
         with the specified color  """
    t.pencolor(color)   # Set pen color
    t.penup()           # Lift pen to move it
    t.setposition(x, y) # Move the pen to coordinates (x, y)
    t.pendown()         # Place pen to begin drawing 
    for i in range(8):  # Draw the eight sides
        t.forward(80)  
        t.right(45)  


def spiral(t, x, y, color):
    """  Draws with turtle t a spiral centered at (x, y) 
         with the specified color  """
    distance = 0.2
    angle = 40
    t.pencolor(color)   # Set pen color
    t.penup()           # Left pen to move it
    t.setposition(x, y) # Position the pen at coordinates (x, y)
    t.pendown()         # Set pen down to begin drawing
    for i in range(100):
        t.forward(distance)
        t.left(angle)
        distance += 0.5


t = Turtle()        # Create a turtle object named t
octogon(t, -45, 100, 'red')
spiral(t, 0, 0, 'blue')
t.hideturtle()      # Make turtle t invisible
done()
