from turtle import *

speed ('fast')
pencolor('blue')

gap = 5
angle = 60

for i in range (50):
    fd(i*3+5)
    print (i*gap)
    lt(angle)

mainloop()