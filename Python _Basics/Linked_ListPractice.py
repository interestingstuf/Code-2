
from collections import deque as de
"""
l_list1 = de(["A", "B", "C"])

print(l_list1)

l_list1.append("D")
print(l_list1)
l_list1.appendleft("E")
print(l_list1)
l_list1.pop()
print(l_list1)
l_list1.popleft()
print(l_list1)
"""
Patients = de()
while True:
    
    Entry1 = input("Enter The Patient")
    if Entry1 == "Delete":
        Patients.popleft()
    else:    
        Patients.append(Entry1)
        

    print(Patients)
    
        



