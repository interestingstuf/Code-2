from math import pi
from os import linesep
from sys import warnoptions
"""
NewFile = open("myfirstfile.txt", "w+")
#NewFile.write("Hey I have Started Useing File Handling")
Lines = ["Hello Everyone\n", "How Are You\n", "This Is Third Line" ]
NewFile.writelines(Lines)

NewFile.close()
NewFile1 = open("myfirstfile.txt", "r")
print(NewFile1.readline())
splt = NewFile1.readline()
for i in splt:
    print(i)
    words = i.split()
    print(words)

#NewFile1.close()
"""
import pickle as pi


"""
list1 = [1, "Raj", "Liitle School", 19]

newfile3 = open("mysecondbinary.dat", "wb")

pi.dump(list1, newfile3)

newfile3.close()
"""
newfile4 = open("mysecondbinary.dat", "rb")
data = pi.load(newfile4)
newfile4.close()


print(data)
list1 = [1, "Raj", "Liitle School", 19]

newfile3 = open("mysecondbinary.dat", "wb")

pi.dump(list1, newfile3)

#newfile3.close()
entry1 = input("Enter Your Name")
entry2 = input("Enter Your RollNo")
data = [entry1, entry2]
print(data)
pi.dump(data, newfile3)
