from turtle import *
from tkinter import messagebox 


# Gain access to the game engine functions
from dot3x3logic import *

# Some global variables supporting the graphical interface

# The first dot selected by a player when creating a line
initial_dot = None

dot_radius = 10  # Can adjust for larger or smaller dots


def square_to_point(sq):
    """ Compute the (x, y) coordinates of the center of a square. 
        Used to properly place the square's owner when it becomes
        captured. """
    if sq == "LeftTop":
        return (200, 400)
    elif sq == "RightTop":
        return (400, 400)
    elif sq == "LeftBottom":
        return (200, 200)
    elif sq == "RightBottom":
        return (400, 200)


def hit(x, y):
    """ Returns the dot (if any) that the point (x, y) is within.
        Returns None if the point (x, y) does not overlap any dot.
        Used when a player clicks the mouse over the board to 
        determine which dot (if any) was selected. """
    dot = None  # Default result
    if 90 < x < 110 and 490 < y < 510:
        dot = "Northwest"
    elif 290 < x < 310 and 490 < y < 510:
        dot = "North"
    elif 490 < x < 510 and 490 < y < 510:
        dot = "Northeast"
    elif 90 < x < 110 and 290 < y < 310:
        dot = "West"
    elif 290 < x < 310 and 290 < y < 310:
        dot = "Center"
    elif 490 < x < 510 and 290 < y < 310:
        dot = "East"
    elif 90 < x < 110 and 90 < y < 110:
        dot = "Southwest"
    elif 290 < x < 310 and 90 < y < 110:
        dot = "South"
    elif 490 < x < 510 and 90 < y < 110:
        dot = "Southeast"
    return dot

def dot_to_point(dot):
    """ Maps a dot to its location on the board.  Used to
        render a dot in its proper place. """
    if dot == "Northwest":
        return 100, 500
    elif dot == "North":
        return 300, 500
    elif dot == "Northeast":
        return 500, 500
    elif dot == "West":
        return 100, 300
    elif dot == "Center":
        return 300, 300
    elif dot == "East":
        return 500, 300
    elif dot == "Southwest":
        return 100, 100
    elif dot == "South":
        return 300, 100
    elif dot == "Southeast":
        return 500, 100


def draw_dot(name, col="black"):
    """ Draws a graphical dot within the graphical window.
        col specifies the dot's color (black by default). """
    global dot_radius

    pensize(1)
    penup()
    x, y = dot_to_point(name)
    setposition(x, y - dot_radius)
    pendown()
    color(col)
    begin_fill()
    circle(dot_radius)
    end_fill()
    update()


def draw_line(x1, y1, x2, y2): 
    """ Draws a line segment with endpoints (x1, y1) and (x2, y2).  """
    penup()
    setposition(x1, y1)
    pendown()
    setposition(x2, y2)
    update()


def draw_X(x, y):
    """  Draws player X's mark at position (x,y). """
    color("blue")
    pensize(10)
    draw_line(x - 40, y - 40, x + 40, y + 40)
    draw_line(x - 40, y + 40, x + 40, y - 40)


def draw_Y(x, y):
    """  Draws player Y's mark at position (x,y). """
    color("blue")
    pensize(10)
    draw_line(x - 40, y + 40, x, y)
    draw_line(x + 40, y + 40, x, y)
    draw_line(x, y, x, y - 40)


def draw_square(sq, owner):
    """ Draws the owner of a square in the square, if the square
        has an owner. """
    # Coordinates the square
    x, y = square_to_point(sq)
    if owner == "X":
        draw_X(x, y)
    elif owner == "Y":
        draw_Y(x, y)
    # Else do not draw anything--the square has no owner


def check_squares():
    """ Checks all squares to determine if any are complete.
        Draws the square owner's mark in a completed square.
        If all squares are owned, the function declares a winner
        or announces a draw. """
    # Check the ownership of each potential square
    draw_square("LeftTop", square_owner("LeftTop"))
    draw_square("RightTop", square_owner("RightTop"))
    draw_square("LeftBottom", square_owner("LeftBottom"))
    draw_square("RightBottom", square_owner("RightBottom"))
    # Determine 
    win = winner()
    if win == "X":
        messagebox.showinfo("Game Over", "X wins")
    elif win == "Y":
        messagebox.showinfo("Game Over", "Y wins")
    elif win == "Draw":
        messagebox.showinfo("Game Over", "Tie Game")


def mouse_click(x, y):
    """ Responds to the user clicking the mouse when the cursor
        is over the window.  Determines if the user clicked on
        a dot.  Activates an initial dot if the initial dot is not 
        already active.  Establishes a line to a terminal dot if
        possible.  If the move is illegal, the function produces a
        message box alerting the player. """
    global initial_dot
    print("initial_dot =", initial_dot)

    print("clicked at x =", x, "  y =", y)
    dot = hit(x, y)  # Did the player click on a dot?
    if dot:
        print(dot)
        if not initial_dot:
            initial_dot = dot
            draw_dot(initial_dot, "red")
        elif dot != initial_dot:
            if add_line(line_name(initial_dot, dot)):
                # Draw the added line
                color("black")
                pensize(5)
                x1, y1 = dot_to_point(initial_dot)
                x2, y2 = dot_to_point(dot)
                draw_line(x1, y1, x2, y2)
                # Adjust title bar to current player
                title("3x3 Connect the Dots   Current Player: " 
                      + current_player())
                # Check to see if the move captured a square
                # and/or ended the game
                check_squares()
            # Clear the initial dot and redraw both connecting dots
            draw_dot(initial_dot)
            initial_dot = None  # Initial dot no longer in play
            draw_dot(dot)
    else:
        if initial_dot:
            draw_dot(initial_dot)
            initial_dot = None


def reset_game():
    """ Reinitialize the game's state for the start of a new game.  """
    clearscreen()
    initialize()


def line_name(dot1, dot2):
    """ Returns the name of the line that connects the 
        Dot objects dot1 and dot2.  Derives the line's name
        from the names of the two dot objects.  Displays
        an error message box if the two dots do not 
        participate in a valid line. """
    if (dot1 == "Northwest" and dot2 == "North") or \
            (dot1 == "North" and dot2 == "Northwest"):
        return "Northwest_North"
    elif (dot1 == "North" and dot2 == "Northeast") or \
            (dot1 == "Northeast" and dot2 == "North"):
        return "North_Northeast"
    elif (dot1 == "Northwest" and dot2 == "West") or \
            (dot1 == "West" and dot2 == "Northwest"):
        return "Northwest_West"
    elif (dot1 == "North" and dot2 == "Center") or \
            (dot1 == "Center" and dot2 == "North"):
        return "North_Center"
    elif (dot1 == "Northeast" and dot2 == "East") or \
            (dot1 == "East" and dot2 == "Northeast"):
        return "Northeast_East"
    elif (dot1 == "West" and dot2 == "Center") or \
            (dot1 == "Center" and dot2 == "West"):
        return "West_Center"
    elif (dot1 == "Center" and dot2 == "East") or \
            (dot1 == "East" and dot2 == "Center"):
        return "Center_East"
    elif (dot1 == "West" and dot2 == "Southwest") or \
            (dot1 == "Southwest" and dot2 == "West"):
        return "West_Southwest"
    elif (dot1 == "Center" and dot2 == "South") or \
            (dot1 == "South" and dot2 == "Center"):
        return "Center_South"
    elif (dot1 == "East" and dot2 == "Southeast") or \
            (dot1 == "Southeast" and dot2 == "East"):
        return "East_Southeast"
    elif (dot1 == "Southwest" and dot2 == "South") or \
            (dot1 == "South" and dot2 == "Southwest"):
        return "Southwest_South"
    elif (dot1 == "South" and dot2 == "Southeast") or \
            (dot1 == "Southeast" and dot2 == "South"):
        return "South_Southeast"
    else:
        print('Not a valid dot link')
        messagebox.showerror("Invalid Link", "You may not connect those two dots")
        return None


def initialize():
    """ Initializes the graphical presentation and game engine. """
    # Global dot objects

    # Initialize game engine
    initialize_board()

    # Specify the dimensions of the window
    screensize(600, 600)
    # Move origin (0, 0) to the left bottom of the window
    setworldcoordinates(0, 0, 599, 599)

    # Apply the usual tricks to speed up the image rendering
    tracer(0)
    hideturtle()

    # Register callback functions with the Turtle graphics framework
    onscreenclick(mouse_click)  # What to do on a mouse click
    onkeyrelease(reset_game, "q") # What to do when user presses the Q key

    # Permit window to receive keypress events
    listen()

    # Set initial widow title
    title("3x3 Connect the Dots   Current Player: " 
          + current_player())

    # No initial dot has been selected
    initial_dot = None

    # Draw all the dots
    for dot in ("Northwest", "North", "Northeast", 
                "West", "Center", "East",
                "Southwest", "South", "Southeast"):
        draw_dot(dot)

    update()  # Force the window to show drawing


if __name__ == "__main__":
    initialize()   # Set up the game
    mainloop()     # Start game running
