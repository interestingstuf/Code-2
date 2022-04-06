
list1 = [10, 20, "Banana", 10.5]
list2 = ["Mango","Apple", 10.8 ]
#print(list1)
#print(list1[2])
#new = input("enter the item")
#list1.append(new)
print(list1)
p = list1 + list2
print(p)
s = list1*3
print(s)
f = p*4
print(f)
print("Banana" in list1 )

list1 = [10, 20, "Banana", 10.5]
print (list1[0:3])
list1.insert(2, "Carrot")
print(list1)
list1.remove(20)
print(list1)
list1.pop(2)
print(list1)
list3 = [10, 20, 44, 33 , 22, 11]
list3.sort(reverse=True)
print(list3)

fruit = list1[2]
print("The fruit in the list is the", fruit)
list1.append("Apple")
list1.pop()
print(list1)
print(len(list1))
list1[0] = "More Mangos"
print (list1)




