from graphicalobject import GraphicalObject

class Dot(GraphicalObject):
    """ A simple, round circle graphical object """
    def __init__(self, **kwargs):
        """ Initializes a dot object with a given Turtle screen, pen,
            and (x, y) position """
        super().__init__(**kwargs)

    def draw(self):
        """ Renders the dot in the Turtle graphics window """
        self.turtle.penup()    # Move pen
        self.turtle.setpos(self.x, self.y)
        self.turtle.pendown()
        self.turtle.fillcolor("red")
        self.turtle.begin_fill()
        self.turtle.circle(20)
        self.turtle.end_fill()
