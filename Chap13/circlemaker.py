from turtle import Turtle, Screen, mainloop, delay, clear
from circle import Circle

t = Turtle()                     # Global turtle
circ = Circle((0, 0), 100)       # Global circle object

def draw_circle(t, circle):
    x, y = circle.get_center()   # Unpack center's coordinates
    radius = circle.get_radius()
    t.penup()                    # Lift pen
    t.setposition(x, y)          # Move pen to (x,y)
    t.pendown()                  # Place pen
    t.dot()                      # Draw a dot at the circle's center
    t.penup()                    # Lift pen
    t.setposition(x, y - radius) # Position pen to draw rim of circle
    t.pendown()                  # Place pen to draw
    t.circle(radius)             # Draw the circle
    t.penup()                    # Lift pen


def do_click(x, y):
    circ.move((x, y))            # Move the circle to a new location
    redraw()


def do_up():
    circ.grow()                   # Make the circle bigger
    redraw()


def do_down():
    circ.shrink()                 # Make the circle smaller
    redraw()


def redraw():
    t.clear()                     # Clear the drawing screen
    draw_circle(t, circ)          # Draw the circle object


def main():
    delay(0)                      # Do not slowly trace drawing
    t.speed(0)                    # Make turtle's actions as fast as possible
    t.hideturtle()                # Make the turtle invisible
    screen = Screen()             # Create Screen object to receive user input
    screen.listen()               # Set focus for keystrokes
    screen.onclick(do_click)      # Set mouse press handler
    screen.onkey(do_up, 'Up')     # Set "up" cursor key handler
    screen.onkey(do_down, 'Down') # Set "down" cursor key handler
    mainloop()


if __name__ == '__main__':
    main()
