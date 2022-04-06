from tkinter import *
import tkinter
#creates window
root = Tk()
#names the window
root.title('Hello Adhav')
#states the size like you wanted
root.geometry("600x400")

def update():
    mylabel.config(text="Parth Amradkar Has Been Arrested Thank You For Reporting His Crime")
mylabel = Label(root, text="Opening....")
mylabel.pack(pady=20)
mylabel.after(3000, update)


#Loop to update windows to changes
root.mainloop()