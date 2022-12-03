import collections
import tkinter as tk
from tkinter import Image, Label, StringVar, messagebox

from tkinter import IntVar

root = tk.Tk()

root.title('App')
root.minsize(550, 500)
root["bg"]= "#2ECCFA"
label1 = tk.Label(root, text="UserName", bg="Red", font="Times 14 bold")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
label2 = tk.Label(root, text="Password", bg="Red", font="Times 14 bold")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root, show="*")
entry2.grid(row=1, column=1)
#img1 = tk.PhotoImage(file = "/Users/parthamradkar/Documents/Python 3.8.5/giph1.gif")
#pic1 = tk.Label(root, image=img1)
#pic1.grid(row=2,column=0)
label4=tk.Label(root, text="Choice")
label4.grid(row=3, column=0)

#Making what happens to label 3 when option clicked
def output():
    selection ="You Choosed Name:"+str(out.get())
    label4.config(text=selection)
    #stores the radio button data in variable
out =StringVar()

#Both Radio Buttons
radio1 = tk.Radiobutton(root, text="Parth", variable=out,value="Parth", command=output)
radio1.grid(row=4,column=0)
radio2 = tk.Radiobutton(root, text = "Nikhil", variable=out, value="Nikhil",  command=output)
radio2.grid(row=5,column=0)


#making checkboxs
label5 = tk.Label(root, text="Harry_Status")
label5.grid(row=8,column=0)
checkbtn1 = IntVar()
checkbtn2 = IntVar()
def output1():
    if checkbtn1.get() == 1:
        label5.config(text="Harry Is There")
    else:
        label5.config(text= "Harry Is Not There")
def output2():
    if checkbtn2.get() == 1:
        label5.config(text="Rohan Is There")
    else:
        label5.config(text= "Rohan Is Not There")

check1 = tk.Checkbutton(root, text="Harry", bg="blue",fg = "red", variable = checkbtn1, onvalue=1, offvalue=0, height=2, width=10, command=output1)
check1.grid(row=6,column=0)

check2 =tk.Checkbutton(root, text="Rohan",bg="blue",fg = "red", variable = checkbtn2, onvalue=1, offvalue=0, height=2, width=10, command=output2)
check2.grid(row=7,column=0)
#making a function when button clicked
def clicked():
    out1="Parth Amradkar"
    out2 = "1892601"
    uname = entry1.get()
    pasw = entry2.get()
    if out1 == uname and pasw == out2:
        #print("Logged In Succesfully")
        tk.messagebox.showinfo("login", "Great, You Are logged In")
        root1= tk.Tk()
        root1.title("Main")
        root1["bg"]= "blue"
        root1 = Image()
        u7jjmu= Label(root, text ="My Student ID is: 1892601").pack()

        root1.mainloop()
         
        
    else:
     #    print("Login Crediantials Wrong")
        tk.messagebox.askretrycancel("try again", "Not Logged In")
button1 = tk.Button(root, text="Sign In", fg = "green", command=clicked)

    
button1.grid(row=2,column=0)



root.mainloop()