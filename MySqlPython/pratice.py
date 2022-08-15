from glob import glob
import matplotlib.pyplot as pl
import io
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import END
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from tkinter import ttk
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
l4=tk.Label(root,text="Phone Number")
l4.place(x=10,y=120)
t3=tk.Entry(root)
t3.place(x=125,y=120)
#salary
l5=tk.Label(root,text="Salary:")
l5.place(x=10,y=155)
t4=tk.Entry(root)
t4.place(x=125,y=155)
#functions
def graph():
    mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Opened")
    cursor=mydb.cursor()


    sql=("select empname,empsal from emp ")
    
    cursor.execute(sql)
    data=cursor.fetchall()
    #print(data) 
    name=[]
    for i in data:
        #print(i[0])
        name.append(i[0])
    print(name)
    sal=[]
    for i in data:
        #print(i[0])
        sal.append(i[1])
    print(sal)
    pl.bar(name,sal)
    pl.show()
        
def selectfile():
    global path
    path=filedialog.askopenfilename(filetypes=[("all files",".*"),("all files",".*")])
    print(path)
def showpic():
    global l10
    empid=t1.get()
    mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    
    )
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("select empid,empname,empph,empsal,empimg from emp where empid=%s ")
    val=(empid,)
    cursor.execute(sql,val)
    data=cursor.fetchall()
    img=Image.open(io.BytesIO(data[0][4]))
    img1=img.resize((180,180),Image.ANTIALIAS)
    img2=ImageTk.PhotoImage(img1)
    l10=tk.Label(root, image=img2)
    l10.place(x=315,y=45)
    l10.image=img2
def add():
    def cbd(filename):
        with open(filename,"rb")as file:
            bd=file.read()
        return bd
    file=cbd(path)

    #prints file path
    #print(file)    
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
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("insert into emp (empid,empname,empph,empsal,empimg) values (%s, %s,%s, %s,%s) ")
    val=(empid1,empname1,empph1,empsalary1,file)
    cursor.execute(sql,val)
    
    print("Values Registrated")
    
    mydb.commit()
    showpic()
    myresult=cursor.fetchall()  
    for x in myresult:
        print(x)
    mydb.close()
    cleartable()
    show()
    print("Connection Closed")
    
def searchid():
    
    empida=t1.get() 
    mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    
    )
    cursor=mydb.cursor()
    sql=("select empid,empname,empph,empsal from emp where empid=%s")   
    val=(empida,)
    cursor.execute(sql,val)
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    
    records=cursor.fetchall()
    t1.insert(0,records[0][0])
    t2.insert(0,records[0][1])
    t3.insert(0,records[0][2])
    t4.insert(0,records[0][3])
    
    print(records)
    showpic()
def clearscreen():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
def searchname():
    try:   
        empnamea=t2.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="Employee",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select empid,empname,empph,empsal from emp where empname=%s")   
        val=(empnamea,)
        cursor.execute(sql,val)
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        t4.delete(0,END)
        
        records=cursor.fetchall()
        t1.insert(0,records[0][0])
        t2.insert(0,records[0][1])
        t3.insert(0,records[0][2])
        t4.insert(0,records[0][3])
        
        print(records)
        showpic()
    except:
        messagebox.showinfo("Information","Name Is Not Located In Database")  
def update():
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
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("update emp set empname=%s,empph=%s,empsal=%s where empid=%s ")
    val=(empname1,empph1,empsalary1,empid1)
    cursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Information","Records Updated Succesfully")
    cleartable()
    show()
    
    
    
    
def delete():
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
    print("Connection Opened")
    cursor=mydb.cursor()
   

    sql=("DELETE FROM emp WHERE empid=%s")
    val=(empid1,)
    cursor.execute(sql,val)
    mydb.commit()
    messagebox.showinfo("Information","Records Deleted Succesfully")
    cleartable()
    show()
def clearscreen():

    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END) 
    l10.after(0,l10.destroy())   
def show():
    try:   
        empnamea=t2.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="Employee",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select empid,empname,empph,empsal from emp")   
        
        cursor.execute(sql)
        records=cursor.fetchall()
        print(records)
        for i,(empid,empname,empph,empsal) in enumerate(records,start=1):
            list1.insert("","end",values=(empid,empname,empph,empsal))
            mydb.close()

    except:
        messagebox.showinfo("Information","Name Is Not Located In Database")
        
def cleartable():
    for item in list1.get_children():
        list1.delete(item)
def Value1(event):
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    rowsid=list1.selection()[0]
    select=list1.set(rowsid)
    t1.insert(0,select["empid"])
    t2.insert(0,select["empname"])
    t3.insert(0,select["empph"])
    t4.insert(0,select["empsal"])
    
def sortalpha():
    cleartable()
    try:   
        empnamea=t2.get() 
        mydb=mysql.connector.connect(
        host="localhost",
        database="Employee",
        user="root",
        password="tyu@3434"
        
        )
        cursor=mydb.cursor()
        sql=("select empid,empname,empph,empsal from emp order by empname")   
        
        cursor.execute(sql)
        records=cursor.fetchall()
        print(records)
        for i,(empid,empname,empph,empsal) in enumerate(records,start=1):
            list1.insert("","end",values=(empid,empname,empph,empsal))
            mydb.close()


    except:
        messagebox.showinfo("Information","Name Is Not Located In Database")
    



#button to add
b1=tk.Button(root,text="Add", command=add)
b1.place(x=500,y=30)
b2=tk.Button(root,text="Clear", command=clearscreen)
b2.place(x=500,y=50)
b3=tk.Button(root,text="Search By ID",command=searchid)
b3.place(x=500,y=70)
b4=tk.Button(root,text="Search By Name",command=searchname)
b4.place(x=500,y=90)
b5=tk.Button(root,text="Update Data Via ID",command=update)
b5.place(x=500,y=110)
b6=tk.Button(root,text="Delete From Database",command=delete)
b6.place(x=500,y=130)
b7=tk.Button(root,text="Sort By Alpha",command=sortalpha)
b7.place(x=500,y=150)
b8=tk.Button(root,text="Select The File",command=selectfile)
b8.place(x=500,y=170)
b9=tk.Button(root,text="Display Data In Graph Format",command=graph)
b9.place(x=500,y=190)
#MYSQL

cols=("empid","empname","empph","empsal")
list1=ttk.Treeview(root,columns=cols,show="headings")
for coll in cols:
    list1.heading(coll,text=coll)
    list1.grid(row=1,column=0,columnspan=2)
    list1.place(x=10,y=250)

show()
list1.bind('<Double-Button-1>',Value1)
root.mainloop()