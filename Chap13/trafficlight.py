from tkinter import Canvas


class TrafficLight:
    """ Models a traffic light. """

    def __init__(self, x, y, width, canvas, initial_color="red"):
        """ Makes a new traffic light object.  The light's
            left-top corner is anchored at the point (x, y).
            The is width pixels wide.
            The light will render on the canvas drawing surface.
            The light's initial color is initial_color. """

        # Check to see if the supplied color is valid
        if initial_color not in ("red", "yellow", "green"):
            raise ValueError(initial_color + " is not a valid color")

        # Initialize instance variables
        self.canvas = canvas
        self.color = initial_color

        # Set the individual lamps initial fill colors
        red_fill = "red" if initial_color == "red" else "black"
        yellow_fill = "yellow" if initial_color == "yellow" else "black"
        green_fill = "green" if initial_color == "green" else "black"

        # 1/5 of the width will the be the basic unit for computing the height of
        # the traffic light and positioning the individual lamps.
        unit = width//5    # Ensure integer division 

        #  Traffic light frame
        canvas.create_rectangle(x, y, x + width, y + 13*unit, fill='gray')

        x = x + unit
        y = y + unit
        diameter = 3*unit   # Diameter (bounding box width) of each lamp

        #  Red lamp, currently on
        self.red_lamp = canvas.create_oval(x, y, x + diameter, y + diameter, fill=red_fill)
        y += 4*unit
        #  Yellow lamp, currently off
        self.yellow_lamp = canvas.create_oval(x, y, x + diameter, y + diameter, fill=yellow_fill)
        y += 4*unit
        #  Green lamp, currently off
        self.green_lamp = canvas.create_oval(x, y, x + diameter, y + diameter, fill=green_fill)

    def change(self):
        """ Changes the traffic light's color to the next color in
            the sequence. """
        if self.color == 'red':
            self.color = 'green'
            self.canvas.itemconfigure(self.red_lamp, fill='black')     # Turn red off
            self.canvas.itemconfigure(self.green_lamp, fill='green')   # Turn green on
        elif self.color == 'green':
            self.color = 'yellow'
            self.canvas.itemconfigure(self.green_lamp, fill='black')   # Turn green off
            self.canvas.itemconfigure(self.yellow_lamp, fill='yellow') # Turn yellow on
        elif self.color == 'yellow':
            self.color = 'red'
            self.canvas.itemconfigure(self.yellow_lamp, fill='black')  # Turn yellow off
            self.canvas.itemconfigure(self.red_lamp, fill='red')       # Turn red on
