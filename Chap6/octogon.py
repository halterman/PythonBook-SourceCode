# Draws in the window a spiral surrounded with an octagon

import turtle

# Draw a red octogon centered at (-45, 100)
turtle.pencolor('red')       # Set pen color
turtle.penup()               # Lift pen to move it
turtle.setposition(-45, 100) # Move the pen to coordinates (-45, 100)
turtle.pendown()             # Place pen to begin drawing 
for i in range(8):           # Draw the eight sides
    turtle.forward(80)       # Each side is 80 units long
    turtle.right(45)         # Each vertex is 45 degrees


# Draw a blue spiral centered at (0, 0)
distance = 0.2
angle = 40
turtle.pencolor('blue')      # Set pen color
turtle.penup()               # Left pen to move it
turtle.setposition(0, 0)     # Position the pen at coordinates (0, 0)
turtle.pendown()             # Set pen down to begin drawing
for i in range(100):
    turtle.forward(distance)
    turtle.left(angle)
    distance += 0.5

turtle.hideturtle()          # Make pen invisible
turtle.exitonclick()         # Quit program when user clicks mouse button
