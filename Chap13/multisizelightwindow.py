from tkinter import * #Tk, Canvas
from tkinter.ttk import Button, Frame
from random import choice, randrange

from functools import partial

from trafficlight import TrafficLight

class MultisizeLightWindow:
    """ Graphical window that displays multiple traffic lights
        of different sizes. """

    def do_button_press(self, idx):
        """  The window manager calls this function when the user
             presses the graphical button. """
        self.lights[idx].change()

    def __init__(self):
        root = Tk()      # Create the main window
        root.title("Multiple Traffic Lights")  # Set title bar text
        self.lights = []
        # The outer frame holds the nine inner frames that each contain
        # a canvas and a button.
        outer_frame = Frame(root)
        outer_frame.pack()
        #  Create nine drawing surfaces within the window
        for i in range(1, 10):
            f = Frame(outer_frame, borderwidth=2, relief=GROOVE)
            f.grid(row=0, column=i)
            c = Canvas(f, width=20*i, height=250)
            c.grid(row=0, column=0)
            self.lights.append(TrafficLight(5*i, 10, 10*i, c))
            #b = Button(f, text="Change", command=lambda x=i: lights[x - 1].change())
            b = Button(f, text="Change", command=partial(self.do_button_press, i - 1))
            b.grid(row=1, column=0)
        #  Start the GUI event loop
        root.mainloop()               


# Main program ---------------------------------------------------------------------

# Create and execute a traffic light window
MultisizeLightWindow()
