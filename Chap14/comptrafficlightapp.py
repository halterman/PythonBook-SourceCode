import tkinter as tk
import tkinter.ttk as ttk

from comptrafficlight import CompTrafficLight


class CompTrafficLightApp:
    """ Graphical window that displays a traffic light and change button. """

    def __init__(self):
        root = tk.Tk()      # Create the main window
        root.title("Traffic Light")  # Set title bar text
        # Create widget container
        frame = ttk.Frame(root)
        frame.pack()
        #  Create a graphical button and ensure it calls the do_button_press
        #  method when the user presses it
        button = ttk.Button(frame, text='Change', command=self.do_button_press)
        # Make a traffic light object instance variable
        self.light = CompTrafficLight(frame, 100, padding=25)
        #  Position button and canvas objects
        button.grid(row=0, column=0)
        self.light.frame.grid(row=0, column=1)
        #  Start the GUI event loop
        root.mainloop()               

    def do_button_press(self):
        """  The window manager calls this function when the user
             presses the graphical button. """
        self.light.change()


# Main program ---------------------------------------------------------------------

# Create and execute a traffic light window
CompTrafficLightApp()
