import pgzrun 

# add bgm music
music.play('man')

b = Rect ((150,150) , (100,50))
b=   Actor('ss', (300,300))

vx , vy =  3 , 3  #vx= velocity on x axis           #global variable
                 #vy=velocity on y axis

def draw():
    screen.fill('white')
    b.draw()
    
def update():
    global vx , vy
    b.x +=vx
    b.y +=vy                   
    
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()
    

#outside of all function

pgzrun.go()