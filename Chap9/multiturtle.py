"""  Uses two Turtle objects to draw on the screen  """

from turtle import *

#  Part 1
t1 = Turtle()        # Create a turtle object named t1
t2 = Turtle()        # Create a second turtle object named t2
t1.pencolor('red')   # t1's pen color is red
t2.pencolor('blue')  # t2's pen color is blue
t2.left(90)          # Point t2 up (t1 autoatically points to the right)
t1.forward(100)      # Move turtle t1 forward 100 units
t2.forward(50)       # Move turtle t2 forward 50 units

# Part 2
t2 = t1              # Make the second turtle just like the first?
t2.right(45)         # Turn turtle 2 (but not turtle 1?)
t2.forward(50)       # Move turtle 2 (why does turtle1 move instead?)

done()
