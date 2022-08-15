from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import END, font
from tkinter import messagebox
from turtle import clear, up
import mysql.connector
from numpy import place
from time import sleep



root=tk.Tk()
root.geometry("800x500")
root.title("Race Builder")
l1=tk.Label(root,text="Enter Data", font=("times",14,"bold","underline"))
l1.place(x=300, y=5)
#form
l2=tk.Label(root,text="Full Name:")
l2.place(x=10,y=50)
t1=tk.Entry(root)
t1.place(x=125,y=50)
#name^^^
l3=tk.Label(root,text="Runner SID")
l3.place(x=10,y=85)
t2=tk.Entry(root)
t2.place(x=125,y=85)
#sid^^^
l4=tk.Label(root,text="Place")
l4.place(x=10,y=120)
t3=tk.Entry(root)
t3.place(x=125,y=120)
#place^^^

   

def add():
    
    ruid1=t2.get()
    rname1=t1.get()
    rplace1=t3.get()

    
    mydb=mysql.connector.connect(
    host="localhost",
    database="RB3",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("insert into runners (ruid,rname,rplace) values (%s, %s,%s) ")
    val=(ruid1,rname1,rplace1)
    cursor.execute(sql,val)
    
    print("Values Registrated")
    
    mydb.commit()
    
    mydb.close()
    print("Connection Closed")
def searchname():

    
    try:   
        rname1=t1.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select rname,ruid,rplace from runners where rname=%s")   
        val=(rname1,)
        cursor.execute(sql,val)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        
        
        records=cursor.fetchall()
        t1.insert(0,records[0][0])
        t2.insert(0,records[0][1])
        t3.insert(0,records[0][2])
        
        
        print(records)
    except:
        messagebox.showinfo("Information","Name Is Not Located In Database")  
def searchplace():
    try:   
        rplace1=t3.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select rname,ruid,rplace from runners where rplace=%s")   
        val=(rplace1,)
        cursor.execute(sql,val)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        
        
        records=cursor.fetchall()
        t1.insert(0,records[0][0])
        t2.insert(0,records[0][1])
        t3.insert(0,records[0][2])
        
        
        print(records)
    except:
        messagebox.showinfo("Information","Name Is Not Located In Database")  
def update():
    rname1=t1.get()
    ruid1=t2.get()
    rplace1=t3.get()
    
    mydb=mysql.connector.connect(
    host="localhost",
    database="RB3",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("update runners set rname=%s,rplace=%s where ruid=%s ")
    val=(rname1,rplace1,ruid1)
    cursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Information","Records Updated Succesfully")
    
def searchruid():
    try:   
        ruid1=t2.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="RB3",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select rname,ruid,rplace from runners where ruid=%s")   
        val=(ruid1,)
        cursor.execute(sql,val)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        
        
        records=cursor.fetchall()
        t1.insert(0,records[0][0])
        t2.insert(0,records[0][1])
        t3.insert(0,records[0][2])
        
        
        print(records)
    except:
        messagebox.showinfo("Information","RUID Is Not Located In Database")
def delete():
    ruid1=t1.get()
    rname1=t2.get()
    rplace1=t3.get()
    mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("DELETE FROM emp WHERE ruid=%s")
    val=(ruid1,)
    cursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Information","Records Deleted Succesfully")
    

    
    
    

def clearscreen():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    
        

#button to add
b1=tk.Button(root,text="Add", command=add)
b1.place(x=500,y=50)
b2=tk.Button(root,text="Search By Name",command=searchname)
b2.place(x=500,y=150)
b3=tk.Button(root,text="Search By Place",command=searchplace)
b3.place(x=500,y=100)
b4=tk.Button(root,text="Clear Data Entry",command=clearscreen)
b4.place(x=500,y=200)
b5=tk.Button(root,text="Update Via RUID", command=update)
b5.place(x=500,y=250)
b6=tk.Button(root,text="Search By RUID",command=searchruid)
b6.place(x=500,y=300)
b7=tk.Button(root,text="Delete By RUID",command=delete)
b7.place(x=500,y=300)



#MYSQL

root.mainloop()