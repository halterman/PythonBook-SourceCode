from tkinter import Tk, Button


count = 0   # Records the number of button presses


def update():
    """ Updates the count label within the graphical button """
    global count, b
    count += 1
    b.config(text="Click Count = " + str(count))
    print("Updating")


root = Tk()
b = Button(root)
b.configure(background="yellow", text="Click Count = 0", command=update)
b.pack()
root.mainloop()
