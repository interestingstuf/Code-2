"""

def hi(name="Raj"):
    return "Hi" + "" + name
print(hi())
"""


"""
def hi():

    print("Hi Raj")
#hi()    
Greet = hi

Greet()
"""
#^^^^We Can Assign Function to Variable^^^^
"""
def hi(name):
    print("Youe are inside hi function")
    
    def Greet():
        return "Youe are in greet function"
        
    def Welcome():
        return"Youe Are in Welcome Function"
    #print(Greet())
    #print(Welcome())
    if name == "Raj":
        return Greet()
    else:
        return Welcome()    
    print("Youe Are Back in Hi Function")   
#hi()             
print(hi("Raj"))
"""
#^^^We Can Run A Function Inside a another function from outside in a indirect way^^^
"""
def hi():
    return "Hi Raj"
def before_hi(f1): 
    print("I am doing berfore hi")
    print(f1())  
before_hi(hi)  
#^^^ Call a function from a function^^^  
"""
def First_Decorator(f1):
    def Wrapping_Function():
        print("I Am Doing This Berfore Executing f1")
        f1()
        print("I am Doing This After f1")
    return Wrapping_Function
@First_Decorator     
     
def Function_Require_Decoration():
    print("I Am The Function Which Needs Decoration")
#Function_Require_Decoration = First_Decorator(Function_Require_Decoration)
Function_Require_Decoration()
   