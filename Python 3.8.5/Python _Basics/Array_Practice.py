import array as ar

array1 = ar.array("i", [10, 20, 30, 44])

print(array1)
print(array1[0])
print("BREAK POINT")
array1.insert(2, 345)
array1[0]=100
array1.remove(20)
for i in array1:
    print(i)
print(array1.index(30))    
array2 = ar.array("i", [123,12344,46767,6867])
#Combines array 1 and array 2
array1.extend(array2)

print(array1)
array1.pop(2)
print(array1)
array1.reverse()
print(array1) 
array3 = ar.array("d", [123.5,12344.7,46767.3,6867.9])
for i in array3:
    print(i)
array4 = ar.array("u", "Hello")
for i in array4:
    print(i)