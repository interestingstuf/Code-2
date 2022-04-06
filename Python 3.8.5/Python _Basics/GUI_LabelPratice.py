from tkinter import *
#creates the window
root = Tk()
#creates label
myLabe1 = Label(root, text="Helaalo")
#sets position in the window
myLabe1.grid(row=10, column=100)

#creates a loop so the window is updated for changes
root.mainloop()