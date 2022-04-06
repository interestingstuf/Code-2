

name_length = map(len, ["Raj", "Parth", "Little"])
print(list(name_length))
list1 = ["raj", "parth", "little"]
map1 = map(max, list1)
print(list(map1))
s1 = map(lambda a: a * a, [1, 2, 3])
print(list(s1))

from functools import reduce

def Add1(x, y):
    return x + y    
list2 = [1, 2, 3, 4]
print(reduce(Add1, list2))


list3 = ["A", "B", "C", "D", "E", "F"]

def filter_vls(a):
    vls = ["A", "I", "O", "U", "E"]
    if (a in vls):
        return True
    else:
        return False    
vowels = filter(filter_vls, list3)
print(list(vowels))
    