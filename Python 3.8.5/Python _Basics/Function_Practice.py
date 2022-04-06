


def Add1(a, b):


    c = a+b
    print(c)
#num1 = int(input("Enter First Number"))    
#num2 = int(input("Enter Second Number"))  
#Add1(num1, num2)  
def sub1(a, b):
    c = a-b
    return c
#print(sub1(16, 12))
d = sub1(16,12)
e = d * 10
print(e)    
#lambda functions

square = lambda x: x * x
print(square(4))

Add2 = lambda x, y: x+y
print(Add2(4, 6))
FullName = lambda First, Last:print("The Full Name Is", First,"",Last)
FullName("Raj", "Kumar")