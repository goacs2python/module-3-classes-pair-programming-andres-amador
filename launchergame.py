import pgzrun
import math
import random

WIDTH = 1000
HEIGHT = 800

bulletRadius =10
mousePos = (0,0)
firing = 0
yacc = 5
bullets = []
targets = []
score = 0
timer = 30

class Bullets():
    
    def __init__(self, pos, xvel):
        self.pos = pos
        self.xvel = xvel
        self.yvel = 0

class Targets():
    
    def __init__(self, pos):
        self.pos = pos


def draw():
    screen.clear()
    screen.draw.filled_circle(mousePos,10,"green")
    if timer > 0:
        for bullet in bullets:
            screen.draw.filled_circle(bullet.pos,bulletRadius,"white")
        for target in targets:
            screen.draw.filled_circle(target.pos, 40, "yellow")
        screen.draw.text(str(timer), (0,0))
        screen.draw.text(str(score), (100,0))
    else:
        f = open("highscores.txt", "a")
        f.write(str(score)+"\n")
        f.close()
        exit()
    
  
def createTarget():
    global targets
    targets.append(Targets((random.randint(0,1000),random.randint(100,800))))

def myCountdown():
    global timer
    timer -=1

def update():
    global bullets, targets, firing, yacc, score, timer
    firing += 1
    for bullet in bullets:
        bullet.yvel += yacc
        bullet.pos = (bullet.pos[0]+bullet.xvel, bullet.pos[1]+bullet.yvel)
        if bullet.pos[0] >1020 or bullet.pos[1] > 820:
            del bullets[bullets.index(bullet)]
        for target in targets:
            if (target.pos[0]-bullet.pos[0])**2+(target.pos[1]-bullet.pos[1])**2 <= (10+40)**2:
                del bullets[bullets.index(bullet)]
                del targets[targets.index(target)]
                score +=1
    
    if firing >= 100:
        firing = 0
    
clock.schedule_interval(createTarget, 1)
clock.schedule_interval(myCountdown, 1)

def on_mouse_down(button):
    global firing
    if button == mouse.LEFT:
        if firing > 10:
            bullets.append(Bullets((500,0),(1/5)*(mousePos[0]-500)))
            firing = 0

def on_mouse_move(pos):
  global mousePos
  mousePos = pos
  
pgzrun.go()