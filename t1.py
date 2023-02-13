from turtle import * # import turtle module

speed ('fastest')
side = 10
size = 40

#Creat a hexagon
for i in range (side):
    fd(size)
    lt(360/side)
    write(i)


hideturtle()
mainloop()



