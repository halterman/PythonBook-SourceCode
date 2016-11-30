from top import Top

class GraphicalObject(Top):
    """ A graphical object that allows the user to reposition
        it anywhere within the window using the mouse. 
        Contains all the code to manage the Turtle graphics
        environment. """
    def __init__(self, **kwargs):
        """ Initializes a GraphicalObject object
            Keyword args include:
              screen is the Turtle graphics screen. 
              turtle is the Turtle graphics pen. 
              initially appear at location (x, y). """
        super().__init__(**kwargs)   # See discussion about super constructor
        print("Initializing graphical object")
        self.screen = kwargs['screen']
        self.turtle = kwargs['turtle']
        self.x = kwargs['x']
        self.y = kwargs['y']
        self.screen.delay(0)     # Do not slowly trace drawing
        self.turtle.speed(0)     # Make turtle's actions as fast as possible
        self.turtle.hideturtle()            # Make the turtle invisible
        self.screen.onclick(self.do_click)  # Set mouse press handler
        self.move_to(x=kwargs['x'], y=kwargs['y'])

    def run(self):
        """ Run the graphical program. """
        self.screen.mainloop()

    def draw(self):
        """ Renders the object within the window. 
            Derived classes override this method to meet their specific
            needs. """
        pass

    def do_click(self, x, y):
        """ Called when the user presses the mouse button.
            (x, y) is the new location of the display. """
        self.move_to(x, y)      # Move to a new location
        self.draw()          # Redraw at new location

    def move_to(self, x, y):
        """ Relocates a Movable object to position (x, y). """
        self.x, self.y = x, y
