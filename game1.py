import pgzrun 

# add bgm music
music.play('bgm')

b = Rect((150,150) , (100,50))
vx ,vy =  3 , 3  #vx= velocity on x axis  #global variable
                 #vy=velocity on y axis

def draw():
    screen.fill('black')
    screen.draw.rect(b ,'green')

def update():
    global vx , vy
    b.x +=vx
    b.y +=vy
    sound
    if b.right > 800 or b.left < 0:
        vx = -vx
    if b.bottom > 600 or b.top < 0:
        vy = -vy
    

#outside of all function

pgzrun.go()