
import turtle as t
t.speed(10)
t.shape("turtle")
t.shapesize(5)
t.pencolor("green")
t.pensize(0)
t.fillcolor("red")
"""
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
"""

count = 0 
length = 200
color = ["red", "green", "blue", "yellow"]
while count < 50:
    t.pencolor(color [count%4])
    t.forward(length)
    t.left(90)
    count = count+1
    length = length-5
    
    






















t.mainloop()


