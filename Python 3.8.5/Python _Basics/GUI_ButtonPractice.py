from tkinter import *
import tkinter
#creates window
root = Tk()
root.title('Hello Adhav')
root.geometry("600x400")
#defines he function "myClick"
def myClick():
    myLabe1 = Label(root, text="Clicked")
    myLabe1.pack()
#creates a button with text "Click me" and when clicked the commands is MyClick which we have defined above in that statement    
myButton = Button(root, text="Click Me", command=myClick, fg="blue" )

myButton.pack()
#Loop to update windows to changes

root.mainloop()