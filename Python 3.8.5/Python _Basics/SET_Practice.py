from os import name


A = set ("RajKumar")
print(A)
B = set (["RajKumar", "ParthAmradkar", "CoolBoy", "RajKumar"])
print(B)
B.add("Heera")
print(B)
B.remove("RajKumar")
print(B)
a = {"A", "B", "C", "D", "E"}
b = {"B", "E", "F"}
print (a.difference(b))
print(a.intersection(b))
print(a.union(b))
name1 = input("Enter The Name")
marks = input("Enter The Marks")#