from cProfile import label
import io
import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
root=tk.Tk()
root.geometry("2000x2000")
root.title("Showimg")
mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    

    )
cursor=mydb.cursor()
print("Connection Successful")

sql=("select * from textimg")

cursor.execute(sql)
record=cursor.fetchall()
img=Image.open(io.BytesIO(record[0][2]))
img1=ImageTk.PhotoImage(img)


lb1=tk.Label(root,image=img1)
lb1.grid(column=0,row=0)

root.mainloop()