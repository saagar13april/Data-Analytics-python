from turtle import *

speed('fastest')
pencolor('black')
fillcolor('yellow')

for i in range (6):
    fd(100)
    for i in range (6):
        fd(50)
        begin_fill()
        for i in range (6):
            fd(25)
            rt(60)
        for i in range (6):
                fd(10)
                rt(60)
        for i in range (6):
                fd(5)
                rt(60)
        end_fill()
        rt(60)
    rt(60)
hideturtle()
mainloop()




