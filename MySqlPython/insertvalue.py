
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
l3=tk.Label(root,text="Database Name:")
l3.grid(row=2, column=0)
t3=tk.Entry(root)
t3.grid(row=2,column=1)
def f1():
    mydb=mysql.connector.connect(
    host="localhost",
    database="connection",
    user="root",
    password="tyu@3434",


    )
    cursor=mydb.cursor()
    print("Connection Successful")
    name=t3.get()
    sql=("insert into abc (NAME,ID) values (%s, %s) ")
    val=("Rohan", "787")
    cursor.execute(sql,val)
    mydb.commit()
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
    mydb.close()
b1=tk.Button(root,text="Connect To Server",command=f1)
b1.grid(row=3,column=0)
root.mainloop()
