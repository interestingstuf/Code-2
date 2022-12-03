def Divisablity_Check(num1):
    answer = num1%2
    answer1 = num1%3
    if answer   == 0 and answer1 == 0:
        print(num1, "Is Divisable By Two And Three")
    else:
        print(num1, "Is Not Divisable By Two And Three")    
Divisablity_Check(8)     
def evenOdd(dig1):
    equation = dig1%2
    if equation == 0:
        print(dig1, "Is Even") 
    else:
        print(dig1, "Is Odd")    
evenOdd(2)        
def primenumber(digit1):

    for i in range(2,digit1 ):
        if digit1%i == 0:
            check = True
            break
        else:
            check = False
    if check == True:
        print("Is not a prime number")
    else:
        print("It Is A Prime Number")    
    
primenumber(30)
            
            



    
    


