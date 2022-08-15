import mysql.connector

def cbd(filename):
    with open(filename,"rb")as file:
        bd=file.read()
    return bd
file=cbd("/Users/parthamradkar/Documents/Code 2/MySqlPython/mclaren_p1_gtr_mclaren_p1_mclaren_128793_1920x1080.jpg")
print(file)

mydb=mysql.connector.connect(
    host="localhost",
    database="Employee",
    user="root",
    password="tyu@3434"
    

    )
cursor=mydb.cursor()
print("Connection Successful")

sql=("insert into textimg (name,rolenumber,imge) values (%s, %s, %s) ")
val=("Rohan", "452",file)
cursor.execute(sql,val)
mydb.commit()
mydb.close()
