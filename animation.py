import sys, pygame, glob
import pygame.time as tmt

#Height
#width
height=300
width=400

#Screen color
black=0,0,0

screen=pygame.display.set_mode((width, height))
clocl=tmt.Clock()

#Player funtion
class Player(object):
    def __init__(self):
        #Original Position
        self.x=10
        self.y=10
        self.speedinit=10
        self.animationspeed=self.speedinit
        self.anipos=0
        self.animax=3
        self.img=pygame.image.load("ball.bmp")


    def update(self, keypress):
        if keypress[pygame.K_UP]:
            self.y-=2
        if keypress[pygame.K_DOWN]:
            self.y+=2
        if keypress[pygame.K_RIGHT]:
            self.x+=2
        if keypress[pygame.K_LEFT]:
            self.x -=2

        screen.blit(self.img, (self.x, self.y))
        pygame.display.flip()






player1=Player()

#Main Game Loop
while 1:
    screen.fill(black)
    #clocl.tick(60)

    #check events:

    for event in pygame.event.get():
        #if Window is closed. Shut down
        if event.type == pygame.QUIT:
            sys.exit()
        keys=pygame.key.get_pressed()
        player1.update(keys)

