#set variable
i = 1
#sets how many times it will repeat the pattern
while i <= 10:
    print("Outer Loop Is Executed Only Once")
    #sets how much it will increment every time i increases
    j = 1
    #makes a loop for the incremental digits 
    while j <= i:
        #makes the digits increase
        j = j+1
        #prints results
        print("*", end = "")
        print("Inner Loop Is Executed Until The Completion")
    #makes i higher by one at the end of the cycle    
    i = i+1
    print()

import turtle as t
i =0
while i <= 2:
    t.circle(100)
    i = i+1

    j = 0
    t.goto(0,20)
    while j < 4:
       
        t.forward(100)
        t.left(90)
        j = j+1
t.mainloop()