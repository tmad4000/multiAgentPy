# https://pythonprogramming.net/drawing-objects-pygame-tutorial/

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('MultiAgent Sim')
clock = pygame.time.Clock()

# carImg = pygame.image.load('racecar.gif')



class Car:
    def __init__(self,x=display_width * 0.45, y=display_height * 0.8):
        self.x = x
        self.y = y

        self.x_changeLeft = -5
        self.x_changeRight = 5
        self.car_width = 73
        self.speed=5
    
    def nudgeLeft(self):
        self.x += self.x_changeLeft
    
    def nudgeRight(self):
        self.x += self.x_changeRight

    def nudgeUp(self):
        self.y -= self.speed
    
    def nudgeDown(self):
        self.y += self.speed


    def draw(self):
        circle = pygame.draw.circle(gameDisplay, (0, 0, 0), (int(self.x), int(self.y)), int(self.car_width/2), 1)
        


class Obstacle:
    def __init__(self,x=display_width * 0.45, y=display_height * 0.8):
        thing_startx = random.randrange(0, display_width)
        thing_starty = -600
        
        self.x = thing_startx
        self.y = thing_starty
        self.color=black
       
        self.vx = 0
        self.vy = 7

        self.w = 100
        self.h = 100


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
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
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
    theCar=Car()
    obstacle=Obstacle()
    # x = (display_width * 0.45)
    # y = (display_height * 0.8)

    # x_change = 0
######
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
######
    gameExit = False

    while not gameExit:


        #left and right motion
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
        # if event.key == pygame.K_LEFT:
            # x_change = -5
            theCar.nudgeLeft()
        if pressed[pygame.K_RIGHT]:                    
        # if event.key == pygame.K_RIGHT:
            # x_change = 5
            theCar.nudgeRight()     
            
        if pressed[pygame.K_UP]:                    
            theCar.nudgeUp()     
        if pressed[pygame.K_DOWN]:                    
            theCar.nudgeDown()     
            

        for event in pygame.event.get():

            #wuitting
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                # CMD=310
                Q=113 
                
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
        obstacle.tick()
        # thing_starty += thing_speed
        # car(x,y)
        obstacle.draw()
        theCar.draw()
     ##########
        if theCar.x > display_width - theCar.car_width or theCar.x < 0:
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

