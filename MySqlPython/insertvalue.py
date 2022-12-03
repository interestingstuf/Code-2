
import tkinter as tk



import mysql.connector
login=tk.Tk()
login.geometry("300x200")
l1=tk.Label(login,text="Username:")
l1.grid(row=0, column=0)
t1=tk.Entry(login)
t1.grid(row=0,column=1)
l2=tk.Label(login,text="Password:")
l2.grid(row=1, column=0)
t2=tk.Entry(login,show="*")
t2.grid(row=1,column=1)

def f1():
    mydb=mysql.connector.connect(
    host="localhost",
    database="Manager",
    user="root",
    password="tyu@3434",


    )
    cursor=mydb.cursor()
    print("Connection Successful")
   
    sql=("insert into Login (UserName,Password) values (%s, %s) ")
    val=(t1.get(), t2.get())
    cursor.execute(sql,val)
    mydb.commit()
    mydb.close()
b1=tk.Button(login,text="Sign Up",command=f1)
b1.grid(row=1,column=3)

login.mainloop()
