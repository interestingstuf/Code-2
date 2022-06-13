
import tkinter as tk



import mysql.connector
root=tk.Tk()
root.geometry("300x200")
l1=tk.Label(root,text="Username:")
l1.grid(row=0, column=0)
t1=tk.Entry(root)
t1.grid(row=0,column=1)
l2=tk.Label(root,text="Password:")
l2.grid(row=1, column=0)
t2=tk.Entry(root,show="*")
t2.grid(row=1,column=1)
def f1():
    mydb=mysql.connector.connect(
    host="localhost",
    database="studentattendance",
    user=t1.get(),
    password=t2.get(),
    

    )
    print("Connection Successful")
    
b1=tk.Button(root,text="Connect To Server",command=f1)
b1.grid(row=2,column=0)
root.mainloop()
