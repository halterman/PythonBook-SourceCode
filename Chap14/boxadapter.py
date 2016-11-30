from graphicalobject import GraphicalObject
from box import Box

class BoxAdapter(GraphicalObject):
    """ A simple, square box graphical object.
        BoxAdapter is a GraphicalObject.
        BoxAdapter has a Box. """
    def __init__(self, **kwargs):
        """ Initializes an adapted box object with a given Turtle 
            screen, pen, and (x, y) position """
        self.box = Box(kwargs['screen'], kwargs['turtle'],
                       kwargs['x'], kwargs['y'], kwargs['width'])
        super().__init__(**kwargs)

    def move_to(self, x, y):
        """ Repositions the box to (x,y) """
        self.box.position(x, y)

    def draw(self):
        """ Renders the box in the Turtle graphics window """
        #self.box.position(self.x, self.y)
        self.box.render()
