class Box:
    """ A square box object """
    def __init__(self, screen, pen, x, y, width):
        """ Initializes a box object with a given Turtle screen, pen,
            (x, y) position, and width """
        self._screen = screen
        self._pen = pen
        self._x_val = x
        self._y_val = y
        self._width = width
        
    def position(self, x, y):
        """ Positions the box at (x,y) """
        self._x_val = x
        self._y_val = y

    def render(self):
        """ Renders the box in the Turtle graphics window """
        self._pen.penup()    # Move pen
        self._pen.setpos(self._x_val - self._width/2, 
                        self._y_val - self._width/2)
        self._pen.setheading(0)
        self._pen.pendown()
        self._pen.fillcolor("blue")
        self._pen.begin_fill()
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.forward(self._width)
        self._pen.left(90)
        self._pen.end_fill()
