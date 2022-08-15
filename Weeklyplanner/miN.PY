import tkinter as tk
import random



root=tk.Tk()
l1=tk.Label(root,text="Enter Dish")
l1.grid(row=1,column=2)
t1=tk.Entry(root)
t1.grid(row=1,column=3)
t2=tk.Entry(root)
t2.grid(row=2,column=3)
t3=tk.Entry(root)
t3.grid(row=3,column=3)
t4=tk.Entry(root)
t4.grid(row=4,column=3)
t5=tk.Entry(root)
t5.grid(row=5,column=3)
t6=tk.Entry(root)
t6.grid(row=6,column=3)
t7=tk.Entry(root)
t7.grid(row=7,column=3)
t8=tk.Entry(root)
t8.grid(row=8,column=3)
t9=tk.Entry(root)
t9.grid(row=9,column=3)
t10=tk.Entry(root)
t10.grid(row=10,column=3)


def add():
    global dishes
    dishes=[t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t7.get(),t8.get(),t9.get(),t10.get()]
def gen():
        i=1
        while i<=5:
            t=random.choices(dishes)
            
            print(i)
            print(t)
            i+=1    
    
    


root.geometry("800x500")

b1=tk.Button(root,text="Add",command=add)
b1.grid(row=12,column=4)
b2=tk.Button(root,text="Show Week",command=gen)
b2.grid(row=12,column=6)


root.mainloop()
