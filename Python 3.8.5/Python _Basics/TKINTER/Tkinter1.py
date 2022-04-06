import tkinter as tk

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
def clicked():
    out1="Parth"
    out2 = "189"
    uname = entry1.get()
    pasw = entry2.get()
    if out1 == uname and pasw == out2:
        print("Logged In Succesfully")
        label3 = tk.Label(root, text = "Login Succesful")
        
    else:
        print("Login Crediantials Wrong")

button1 = tk.Button(root, text="Sign In", fg = "green", command=clicked)

    
button1.grid(row=2,column=0)



root.mainloop()