def setup():
    fullScreen()
    
cpu_y = 0
dir = 5
bola_x = 100
dir_x = 5
perdeu = False


def mouseClicked():
    global perdeu
    global cpu_y
    global dir
    global dir_x
    global bola_x

    if perdeu == True:
        
        perdeu = False
        cpu_y = 0
        dir = 5
        bola_x = 100
        dir_x = 5
        
    
def draw():

    global perdeu
    global cpu_y
    global dir
    global dir_x
    global bola_x
    background(0)
    
    if perdeu == True :
        textAlign(CENTER)
        textSize(65)
        text('game over!', width/2, height/2)
        return 
    
    fill(25,25,255)
    rectMode(CENTER)
    rect(15,cpu_y,30,150)
    
    cpu_y += dir 
    
    if cpu_y + 10 >= height:
        dir =-5
    elif cpu_y <=0:
        dir = 5
    
    rectMode(CENTER)
    fill(255,0,0)
    rect(width - 15, mouseY, 30, 150)
    
    rectMode(CORNER)
    fill(255,255,0)
    rect(bola_x, cpu_y, 10,10)
    bola_x += dir_x
    
    if bola_x + 10 >= width:
         perdeu = True
    elif bola_x <= 30:
        dir_x = 5
        
    #jogable
    
    if bola_x >= width - 40 and cpu_y - 9 >= mouseY - 75 and cpu_y + 9 <= mouseY + 75 :
        dir_x = -5
        
        
