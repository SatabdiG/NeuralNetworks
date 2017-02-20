import pygame, sys
from perceptronclasses import Walker

width=600
height=600
screen=pygame.display.set_mode((width, height))
black=0,0,0

#set screen

pygame.display.set_caption("Random Walker", "Random walker")

walker=Walker(width/2, height/2, width, height)
screen.fill(black)
#main loop
while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    walker.walk()
    walker.display(screen)


