# https://pythonprogramming.net/drawing-objects-pygame-tutorial/

import pygame
import time
import random
import math

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MultiAgent Sim')
clock = pygame.time.Clock()

# carImg = pygame.image.load('racecar.gif')

class Obj:
    def __init__(self,x, y, w=50,h=50, color=black,  speed=20, acc=20, heading=0, vx=0,vy=0):
        self.x = x
        self.y = y

        self.vx = vx
        self.vy = vy

        self.w = w
        self.h = h
        self.color=color

        self.speed=speed
        self.acc=acc

        self.heading=heading
        self.headCos=math.cos(self.heading)
        self.headSin=math.sin(self.heading)

    def tick(self):
        self.x += self.vx
        self.y += self.vy

        #friction
        self.vx*=.9
        self.vy*=.9

        self.vx*=0
        self.vy*=0


    def drawRect(self):
        pygame.draw.rect(gameDisplay, self.color, [int(self.x), int(self.y), int(self.w), int(self.h)])
    
    def draw(self):
        pass
      
    

class Car(Obj):
    def __init__(self,x=display_width * 0.45, y=display_height * 0.8):
        super().__init__(x,y,w=73,h=73, color=black, speed=20, acc=20, heading=0, vx=0,vy=0)
    
    def nudgeLeft(self):


        self.vy+= -self.acc*self.headCos
        self.vx+= self.acc*self.headSin

        # self.x -= self.speed
    
    def nudgeRight(self):

        self.vy-= -self.acc*self.headCos
        self.vx-= self.acc*self.headSin

#        self.x += self.speed

    def nudgeUp(self):
        self.vx+= self.acc*self.headCos
        self.vy+= self.acc*self.headSin

        # self.y -= self.speed
        # self.y -= self.speed
    
    def nudgeDown(self):

        self.vx-= self.acc*self.headCos
        self.vy-= self.acc*self.headSin

        # self.y += self.speed


    def tick(self):
        super().tick()
        # self.x += self.vx
        # self.y += self.vy

        # #friction
        # self.vx*=.9
        # self.vy*=.9

        # self.vx*=0
        # self.vy*=0


        (mx,my)=pygame.mouse.get_pos()
        self.mx=mx
        self.my=my
        circle = pygame.draw.circle(gameDisplay, red, (int(mx), int(my)), int(20/2), 1)

    def draw(self):
        circle = pygame.draw.circle(gameDisplay, (0, 0, 0), (int(self.x), int(self.y)), int(self.w/2), 1)
        circle = pygame.draw.circle(gameDisplay, (0, 0, 0), (int(self.x), int(self.y)), int(10/2), 1)
        
        dx=self.mx-self.x
        dy=self.my-self.y
        dist=math.sqrt((dx)**2+(dy)**2)
        
        self.headCos=dx/(dist)
        self.headSin=dy/(dist)
        self.heading=math.atan2(dy,dx)
        
        circle = pygame.draw.circle(gameDisplay, red, (int(self.x+self.headCos*self.w/2), int(self.y+self.headSin*self.w/2)), int(10/2), 1)
        


class Obstacle(Obj):
    def __init__(self,x=display_width * 0.45, y=display_height * 0.8):
        thing_startx = random.randrange(0, display_width)
        thing_starty = -100

        super().__init__(thing_startx,thing_starty,w=100,h=100, color=black, speed=20, acc=20, heading=0, vx=0,vy=14)
        

    def tick(self): 
        self.x += self.vx
        self.y += self.vy

        if self.y > display_height:
            self.y = 0 - self.h
            self.x = random.randrange(0,display_width)

    def draw(self):        
        # circle = pygame.draw.circle(gameDisplay, (0, 0, 0), (int(self.x), int(self.y)), int(self.car_width/2), 1)
        # things(thingx, thingy, thingw, thingh, color):
        pygame.draw.rect(gameDisplay, self.color, [int(self.x), int(self.y), int(self.w), int(self.h)])


        
#######
# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#######
    


# def car(x,y):
#     circle = pygame.draw.circle(gameDisplay, (0, 0, 0), (int(x), int(y)), int(car_width/2), 1)

    # gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop():
    objects=[]

    def registerObject(o):
        objects.append(o)

    def tick():
        for o in objects:
            o.tick()
            o.draw()
            
    theCar=Car()
    obstacle=Obstacle()
    registerObject(theCar)
    registerObject(obstacle)

    # x = (display_width * 0.45)
    # y = (display_height * 0.8)

    # x_change = 0
######
    # thing_startx = random.randrange(0, display_width)
    # thing_starty = -600
    # thing_speed = 7
    # thing_width = 100
    # thing_height = 100
######
    gameExit = False

    while not gameExit:


        #left and right motion
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
        # if event.key == pygame.K_LEFT:
            # x_change = -5
            theCar.nudgeLeft()
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:                    
        # if event.key == pygame.K_RIGHT:
            # x_change = 5
            theCar.nudgeRight()     
            
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:                    
            theCar.nudgeUp()     
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:                    
            theCar.nudgeDown()     
            
        if pygame.mouse.get_pressed()[0]:  
            pass


        for event in pygame.event.get():

            #wuitting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                # CMD=310
                Q=113 
                
                #cmd q
                if (pygame.key.get_mods() & pygame.KMOD_META) and event.key == 113:
                    exit()
                
                # event.key == CMD:

                
                # print(event.key)
               

            # if event.type == pygame.KEYUP:
            #     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #         x_change = 0

        # x += x_change
        
        gameDisplay.fill(white)

     ##########
        # things(thingx, thingy, thingw, thingh, color)
        # things(thing_startx, thing_starty, thing_width, thing_height, black)
        # obstacle.tick()
        # theCar.tick()
        # thing_starty += thing_speed
        # car(x,y)
        # obstacle.draw()
        
     ##########

        tick()

        if theCar.x > display_width - theCar.w or theCar.x < 0:            
            crash()

        # if thing_starty > display_height:
        #     thing_starty = 0 - thing_height
        #     thing_startx = random.randrange(0,display_width)
            
        
        pygame.display.update()
        clock.tick(60)

def exit():
    pygame.quit()
    quit()

game_loop()
exit()

