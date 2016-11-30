from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
from random import choice, randrange

from trafficlight import TrafficLight

class RandomLightsWindow:
    """ Graphical window that displays multiple traffic lights
        of different sizes. """

    def __init__(self):
        root = Tk()      # Create the main window
        root.title("Multiple Traffic Lights")  # Set title bar text
        f = Frame(root)
        f.pack()
        #  Create a drawing surface within the window
        canvas = Canvas(f, width=800, height=600)
        # Make a list of random traffic light objects
        color_list = ["red", "yellow", "green"]
        self.light_list = []
        for i in range(50):
            self.light_list.append(TrafficLight(randrange(2, 700),
                                                randrange(2, 400),
                                                randrange(5, 120),
                                                canvas, 
                                                choice(color_list)))
        #  Create a graphical button and ensure it calls the do_button_press
        #  function when the user presses it
        button = Button(f, text='Change', command=self.do_button_press)
        #  Position button and canvas objects
        button.grid(row=0, column=0)
        canvas.grid(row=0, column=1)
        #  Start the GUI event loop
        root.mainloop()               

    def do_button_press(self):
        """  The window manager calls this function when the user
             presses the graphical button. """
        for light in self.light_list:
            light.change()


# Main program ---------------------------------------------------------------------

# Create and execute a traffic light window
RandomLightsWindow()
