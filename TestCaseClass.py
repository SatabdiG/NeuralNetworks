import pygame
import random

class Neuron(object):
    connections=[]
    network=None

    #where x and y are initial position

    def __init__(self, x, y):
        self.x=x
        self.y=y


    def display(self, screen):
        # draw a circle at position
        for conn in self.connections:
            conn.display(screen)
        pygame.draw.ellipse(screen, 0xfffff, (self.x, self.y, 16, 16))
        pygame.display.flip()

    def addConection(self, b):
        self.connections.append(b)






class Network(object):

    neuronlist=[]

    def __init__(self, x,y):
        self.locationx=x
        self.locationy=y


    def addNeuron(self, neuron):
        xpos=neuron.x+self.locationx
        ypos=neuron.y+self.locationy
        obj=Neuron(xpos, ypos)
        self.neuronlist.append(obj)


    def display(self, screen):
        for neu in self.neuronlist:
            neu.display(screen)

    def connect(self,a,b):
        xpos = a.x + self.locationx
        ypos = a.y + self.locationy
        obj = Neuron(xpos, ypos)
        xpos2 = b.x + self.locationx
        ypos2 = b.y + self.locationy
        obj2 = Neuron(xpos2, ypos2)
        c=Connection(obj,obj2,random.random())
        a.addConection(c)


class Connection(object):
        neurona=None
        neuronb=None
        weight=None

        def __init__(self, neuronfrom, neuronto, weight):
            self.weight=weight
            self.neurona=neuronfrom
            self.neuronb=neuronto


        def display(self, screen):
            color=0xfff00
            #draw the line
            pygame.draw.line(screen, color,(self.neurona.x, self.neurona.y),(self.neuronb.x, self.neuronb.y))
