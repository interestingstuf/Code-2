import tkinter as tk
import random as rand
from typing import Text
import time
#Creates window
root = tk.Tk()
#creates window name
root.title("Password Generator")
#Creates min size of window
root.minsize(500, 600)
#creates label1 with text Enter length
label1= tk.Label(root, text="Enter Length Of Password")
#puts label1 on the grid 
label1.grid(row=0, column=0)
#creates input1 with the module
input1 = tk.Entry(root)
#puts input1 on the grid
input1.grid(row=0, column=1)
#creates the output
output2 = tk.Text(root, height=2, width=25, )
#puts output on the grid
output2.grid(row=1, column=0)
def clicked1():
    Digt1 = "ABCDEFGHIJKLMNOP1234abcdefghigklmnop!$%@#"
    password = ""
    for i in range(int(input1.get())):
        password = rand.choice(Digt1)
        output2.insert(0.0,password)       


      
        


Button1 = tk.Button(root,text="Generate Password", command=clicked1)
Button1.grid(row=2, column=1)
root.mainloop()

