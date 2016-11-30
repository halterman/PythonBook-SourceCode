import tkinter as tk
import tkinter.ttk as ttk


class SignalLamp(ttk.Frame):
    """ Serves as one lamp within a traffic light object. """

    def __init__(self, parent, width, color="red", *args, **kwargs):
        """ Creates a new lamp to be used in a traffic light object.
            parent: The parent widget
            width: The width of the case of the circular lamp
            color: The lamp's initial color (defaults to "red")
            *args: Additional arguments to pass to the ttk.Frame
                superclass constructor
            **kwargs: Additional keyword arguments to pass to the 
                ttk.Frame superclass constructor """
        super().__init__(parent, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=width, height=width, bg="gray",
                                highlightthickness=0)
        self.canvas.pack()
        self.color = color
        offset = width//8
        self.lamp = self.canvas.create_oval(offset, offset, 
                                            7*offset, 
                                            7*offset, 
                                            fill='black')
        self.state = "off"

    def turn_on(self):
        """ Illuminates the lamp """
        self.state = "on"
        self.canvas.itemconfigure(self.lamp, fill=self.color)  

    def turn_off(self):
        """ Turns off the lamp """
        self.state = "off"
        self.canvas.itemconfigure(self.lamp, fill='black') 

    def resize(self, width):
        """ Adjusts the width of the lamp's frame """
        self.canvas.config(width=width, height=width)
        offset = width//8
        self.canvas.coords(self.lamp, offset, offset, 7*offset, 7*offset)


class TrafficSignal(ttk.Frame):
    """ Models a simple traffic light widget """

    def __init__(self, parent, wd, initial_color="red", *args, **kwargs):
        """ Makes a new traffic light object.  
            parent is the parent widget.
            wd is the pixels width.
            The light's initial color is initial_color. """

        super().__init__(parent, width=wd, *args, **kwargs)

        # Check to see if the supplied color is valid
        if initial_color not in ("red", "yellow", "green"):
            raise ValueError(initial_color + " is not a valid color")

        self.grid(row=0, column=0) # Only widget in a 1x1 grid
        # Initialize instance variables
        self.color = initial_color

        # Make lamp objects and store them a dictionary keyed by
        # their color
        self.lamps = dict(zip(('red', 'yellow', 'green'), 
                              (SignalLamp(self, wd, 'red'), 
                               SignalLamp(self, wd, 'yellow'), 
                               SignalLamp(self, wd, 'green'))))
        # Add the lamps to the frame
        self.lamps['red'].grid(row=0, column=0)
        self.lamps['yellow'].grid(row=1, column=0)
        self.lamps['green'].grid(row=2, column=0)

        # Turn on lamp for initial color
        self.lamps[self.color].turn_on()

    def change(self):
        """ Changes the traffic light's color to the next color in
            the sequence. """
        if self.color == 'red':
            new_color = 'green'
        elif self.color == 'green':
            new_color = 'yellow'
        elif self.color == 'yellow':
            new_color = 'red'
        self.lamps[self.color].turn_off()
        self.color = new_color
        self.lamps[self.color].turn_on()

    def resize(self, width):
        """ Changes the traffic light's frame width according to the
            parameter passed by the caller. """
        for lamp in self.lamps.values():
            lamp.resize(width)
