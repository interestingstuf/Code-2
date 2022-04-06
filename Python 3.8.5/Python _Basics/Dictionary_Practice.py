from os import name


d1 = {"Mohan": 94, "Parth": 100, "Raj": 12}
#input1 = input("")
print(d1)
print(d1.items())
print(d1.values())
print(d1.keys())
print(d1["Parth"])
d1["Mohan"] = 76
print(d1)
del d1 ["Mohan"]
print(d1)
name1 = input("Enter The Name")
marks = input("Enter The Marks")
d3 = dict()
d3 [name1] = marks
print(d3)
d4 = d3
d4 [name1] = marks
print(d4)