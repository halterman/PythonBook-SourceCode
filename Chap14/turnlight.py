from tkinter import Canvas

from trafficsignal import SignalLamp
from movablelight import MovableLight


class TurnLamp(SignalLamp):
    def __init__(self, parent, width, *args, **kwargs):
        """ Creates a new lamp to be used in a traffic light object.
            parent: The parent widget
            width: The width of the case of the circular lamp
            *args: Additional arguments to pass to the ttk.Frame
                superclass constructor
            **kwargs: Additional keyword arguments to pass to the 
                ttk.Frame superclass constructor """
        super().__init__(parent, width, *args, **kwargs)
        self.color = 'turn'
        offset = width//8
        self.arrow_shaft = self.canvas.create_line(2*offset, 4*offset, 
                                                   6*offset, 4*offset, 
                                                   fill="black", width=6)
        self.arrow_top_wing = self.canvas.create_line(2*offset, 4*offset, 
                                                      4*offset, 2*offset, 
                                                      fill="black", width=6)
        self.arrow_bottom_wing = self.canvas.create_line(2*offset, 4*offset, 
                                                      4*offset, 6*offset,
                                                      fill="black", width=6)
        self.state = "off"

    def turn_on(self):
        """ Illuminates the lamp """
        self.state = "on"
        self.canvas.itemconfigure(self.arrow_shaft, fill="green")  
        self.canvas.itemconfigure(self.arrow_top_wing, fill="green")  
        self.canvas.itemconfigure(self.arrow_bottom_wing, fill="green")  

    def turn_off(self):
        """ Turns off the lamp """
        self.state = "off"
        self.canvas.itemconfigure(self.arrow_shaft, fill="black")  
        self.canvas.itemconfigure(self.arrow_top_wing, fill="black")  
        self.canvas.itemconfigure(self.arrow_bottom_wing, fill="black")  

    def resize(self, width):
        super().resize(width)
        offset = width//8
        self.canvas.coords(self.arrow_shaft, 2*offset, 4*offset, 
                           6*offset, 4*offset)
        self.canvas.coords(self.arrow_top_wing, 2*offset, 4*offset, 
                           4*offset, 2*offset)
        self.canvas.coords(self.arrow_bottom_wing, 2*offset, 4*offset, 
                           4*offset, 6*offset)



class TurnLight(MovableLight):
    """ Models a traffic light with a left turn arrow. """

    def __init__(self, parent, width, initial_color="red"):
        """ Makes a new traffic light object with left turn arrow.
            The is width pixels wide.
            The light's initial color is initial_color. """
        # Call superclass constructor
        super().__init__(parent, width, initial_color)

        # Add new turn lamp widget to the fourth row 
        self.lamps['turn'] = TurnLamp(self, width)
        self.lamps['turn'].grid(row=3, column=0)  # 4th row


    def change(self):
        """ Changes the traffic light's color to the next color in
            the sequence. """
        if self.color in ('yellow', 'green'):
            super().change()  # Yellow and green behave as before
        else:
            if self.color == 'red':
                new_color = 'turn'   # Red now changes to turn arrow
            elif self.color == 'turn':
                new_color = 'green'  # Turn arrow changes to green
            self.lamps[self.color].turn_off()
            self.color = new_color
            self.lamps[self.color].turn_on()
