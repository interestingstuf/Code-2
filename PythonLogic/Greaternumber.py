

def Greater(num1, num2, num3):
    if num1 >=num2>=num3 or num1 >= num3 >=num2:
        print(num1, "Is Bigger")
        
    elif num2 >= num3 >=num1 or num2 >= num1 >= num3:

        print(num2, "Is Bigger")
    elif num3 >=num1 >=num2 or num3 >= num2 <= num1:
        print(num3, "Is Bigger")

  

Greater(2,5,1)     

Greater(2,7,2)
Greater(8,2,6)
Greater(4,2,8)
Greater(8,4,6)
def Greater1(num1, num2, num3):
    list1 = [num1, num2, num3]
    print("The Greatest Number Is: ",max(list1))

Greater1(34262834682657634866327141274761868746186487,1234687126387983479187391749168476184761284582685, 2345674237864862384628364823646238462734682634823648263864872638462836482736482364723684268374628376)    