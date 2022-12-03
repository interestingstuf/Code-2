import random
"""
#Creates A List For The Module To Choose From
list1 =[1,2,3,4,5,6]
#Prints The Value Randomly
print(random.choice(list1))
"""
"""
digit1=[1,2,3,4,5,6,7,8,9]
digit2=["@", "#", "$", "%", "&", "*"]
digit3=["A","B", "C", "D", "E", "F", "G"]
digit4=[1,2,3,4,5,6,7,8,9]
digit5=[":",";"]
Result1=random.choice(digit1)
Result2=random.choice(digit2)
Result3=random.choice(digit3)
Result4=random.choice(digit4)
Result5=random.choice(digit5)
List1 = [Result1, Result2, Result3,Result4,Result5]
for i in List1:


    print(i, end = "")
print()
"""
"""
Digt1 = "ABCDEFGHIJKLMNOP1234abcdefghigklmnop!$%@#"
password = "mt"
for i in range(9):
    password = random.choice(Digt1)
    print(password, end="")
print()
"""
#print(random.randrange(10, 45, 5))
"""
list1 = ["Rock", "Paper", "Cutter"]
while True:
    Ask = input("Choose Among Rock Paper Or Cutter")
    RobotAnswer=random.choice(list1)
    print(RobotAnswer)
    if Ask == "Rock" and RobotAnswer == "Paper":
        print("You Win")
    elif Ask == "Rock" and RobotAnswer == "Cutter":
        print("You Win")
    elif Ask == "Cutter" and RobotAnswer == "Paper":
        print("You Win")      
    elif Ask == "Cutter" and RobotAnswer == "Rock":
        print("You Lose")
    elif Ask == "Paper" and RobotAnswer == "Cutter":
        print("You Lost") 
        
    elif Ask == "Paper" and RobotAnswer == "Rock":
        print("You Lost")
        
    else: 
        print("ReMatch")       
"""


random.seed(0)

print(random.random())
list3 = [1, 2, 3]
random.shuffle(list3)
print(list3)
print(random.uniform(4,8))



