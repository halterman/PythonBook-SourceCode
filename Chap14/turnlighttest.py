import tkinter as tk
import tkinter.ttk as ttk

from turnlight import TurnLight

class TurnLightTest:
    """ Graphical window that displays multiple traffic lights
        of different sizes. """

    def __init__(self):
        root = tk.Tk()      # Create the main window
        root.title("Movable Traffic Light Test")  # Set title bar text
        width, height = 800, 600
        f = ttk.Frame(root, width=width, height=height)
        f.pack()
        # Place traffic light at the center of the window frame
        print("Frame width:", f.winfo_width())
        self.light = TurnLight(f, height//10, "green")
        f.bind("<Button-1>", self.mouse_pressed)
        f.bind("<Key>", self.key_pressed)
        f.focus_set()
        print("width//2 =", width//2, "  height//2 =", height//2)
        self.light.move_to(width//2, height//2)
        self.size = height//10
        #  Start the GUI event loop
        root.mainloop()               

    def mouse_pressed(self, event):
        """  The window manager calls this function when the user
             presses the graphical button. """
        self.light.move_to(event.x, event.y)
        print("Mouse pressed at", event.x, ",", event.y)

    def key_pressed(self, event):
        """  The window manager calls this function when the user
             presses the graphical button. """
        ch = event.char
        if ch == ">" or ch == ".":
            print("Resize not implemented")
            self.size += 1
            self.light.resize(self.size)
        elif ch == "<" or ch == ",":
            print("Resize not implemented")
            self.size -= 1
            self.light.resize(self.size)
        elif ch == "C" or ch == "c":
            self.light.change()
        print("Key pressed")


# Main program ---------------------------------------------------------------------

# Create and execute a traffic light window
TurnLightTest()
