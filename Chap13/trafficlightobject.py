from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame

from trafficlight import TrafficLight


class TrafficLightWindow:
    """ Graphical window that displays a traffic light and change button. """

    def __init__(self):
        root = Tk()      # Create the main window
        root.title("Traffic Light")  # Set title bar text
        # Create widget container
        frame = Frame(root)
        frame.pack()
        #  Create a graphical button and ensure it calls the do_button_press
        #  method when the user presses it
        button = Button(frame, text='Change', command=self.do_button_press)
        #  Create and add a drawing surface within the window
        canvas = Canvas(frame, width=200, height=300)
        # Make a traffic light object instance variable
        self.light = TrafficLight(50, 20, 100, canvas)
        #  Position button and canvas objects
        button.grid(row=0, column=0)
        canvas.grid(row=0, column=1)
        #  Start the GUI event loop
        root.mainloop()               

    def do_button_press(self):
        """  The window manager calls this function when the user
             presses the graphical button. """
        self.light.change()


# Main program ---------------------------------------------------------------------

# Create and execute a traffic light window
TrafficLightWindow()
