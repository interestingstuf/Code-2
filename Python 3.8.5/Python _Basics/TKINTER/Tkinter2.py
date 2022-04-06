import tkinter as tk

root = tk.Tk()

def openwin():
    top = tk.Toplevel()
   


btn = tk.Button(root, text="Click", command=openwin).pack()

tk.mainloop()