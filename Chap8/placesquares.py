import turtle


def draw_square(x, y):
    """ Draws a 10 x 10 square centered at the point (x, y). """
    turtle.penup()
    turtle.setheading(0)  # Ensure the pen is pointed the proper direction
    turtle.setposition(x - 5, y - 5)  # Center square
    turtle.pendown()
    for i in range(4):
        turtle.forward(10)
        turtle.left(90)
    turtle.update()


# Turn off animation
turtle.tracer(0)
turtle.hideturtle()

# Allow user to place 10 x 10 squares using the mouse
turtle.onscreenclick(draw_square)

# Start the graphics loop that listens for user input
turtle.mainloop()
