# Draws a ractangular box in the window 

from turtle import Turtle, mainloop

t = Turtle()        # Create a turtle object named t
t.pencolor('red')   # t's pen color is red
t.forward(200)      # Move turtle t forward 200 units (create bottom of rectangle
t.left(90)          # Turn turtle left by 90 degrees
t.pencolor('blue')  # Change t's pen color to blue
t.forward(150)      # Move turtle t forward 150 units (create right wall)
t.left(90)          # Turn turtle left by 90 degrees
t.pencolor('green') # Change t's pen color to green
t.forward(200)      # Move turtle t forward 200 units (create top)
t.left(90)          # Turn turtle left by 90 degrees
t.pencolor('black') # Change t's pen color to black
t.forward(150)      # Move turtle t forward 150 units (create left wall)
t.hideturtle()      # Make turtle t invisible
mainloop()          # Await user input
