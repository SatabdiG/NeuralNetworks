import pygame, sys
from TestCaseClass import Neuron, Network, Connection

#Setup
width=640
height=640


black=0,0,0

screen=pygame.display.set_mode((height,width))

network=Network(width/2, height/2)

neu= Neuron(-200,0)
neu2=Neuron(0, 100)
neu3=Neuron(0, -100)
neu4=Neuron(200,0)



network.connect(neu, neu2)
network.connect(neu, neu3)
network.connect(neu3, neu4)
network.connect(neu2, neu4)

network.addNeuron(neu)
network.addNeuron(neu2)
network.addNeuron(neu3)
network.addNeuron(neu4)



#Main Loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        network.display(screen)

    screen.fill(black)

