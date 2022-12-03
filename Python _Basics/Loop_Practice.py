"""
for i in range (5):
    print(i)
print("Hi")   
"""
"""
i = 0
while i < 5:
    print("This Works")
    print(i)
    i = i + 1

"""
"""
bag = ["Science Book", "Math Book", "English Book"]
for i in bag:
    print(i)
"""
"""
bag = ["Science Book", "Math Book", "English Book", "Music Book"]
length = len(bag)
i = 0
while i < length:
    print(bag[i])
    i = i+1
"""
num = int (input("Enter a Number To Generate Its Pattern"))
for i in range (1,num +1):
    for j in range (1, i+1):
        print(j, end = ",")
    print()    
