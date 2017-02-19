import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

#Set height width
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

x1=10
y1=10

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y1-=1
        if keys[pygame.K_DOWN]:
            y1+=1
    #
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]
    #Load screen with black
    screen.fill(black)
    font=pygame.font.Font(None,60)
    ren=font.render("Hello world", 0,(245,244,244))
    pygame.draw.line(screen, 0xfff00, (10,10), (20,20))
    screen.blit(ren, (10,10))
    #pygame.draw.ellipse(screen, 0xfff00,(200,150,100,50))
    screen.blit(ball, (x1, y1))


    pygame.display.flip()