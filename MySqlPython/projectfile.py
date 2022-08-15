from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import font
import mysql.connector
from numpy import place

root=tk.Tk()
root.geometry("800x500")
root.title("Employee Database")
l1=tk.Label(root,text="REGISTRATION FORM", font=("times",14,"bold","underline"))
l1.place(x=300, y=5)
#form
l2=tk.Label(root,text="Employee ID:")
l2.place(x=10,y=50)
t1=tk.Entry(root)
t1.place(x=125,y=50)
#name
l3=tk.Label(root,text="Employee Name:")
l3.place(x=10,y=85)
t2=tk.Entry(root)
t2.place(x=125,y=85)
#ph
l4=tk.Label(root,text="Phone Number:")
l4.place(x=10,y=120)
t3=tk.Entry(root)
t3.place(x=125,y=120)
#salary
l5=tk.Label(root,text="Salary:")
l5.place(x=10,y=155)
t4=tk.Entry(root)
t4.place(x=125,y=155)
#functions
def add():
    empid1=t1.get()
    empname1=t2.get()
    empph1=t3.get()
    empsalary1=t4.get()
    mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Made")
    
    
#button to add
b1=tk.Button(root,text="Add", command=add)
b1.place(x=500,y=50)
#MYSQL

root.mainloop()