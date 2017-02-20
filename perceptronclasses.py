import random
from datetime import datetime
import pygame

random.seed(datetime.now())

class Perceptron(object):
    weights=[]
    learningconstant=0.01

    #Constructor Python
    #Take n as number of inputs
    def __init__(self, n):
        #initialize weight
        for i in range(0,n):
            val=random.uniform(-1,1)
            self.weights.append(val)

    def activate(self, n):
        if(n>0):
            return 1
        else:
            return -1

    def feedforward(self, inputs):
        sum=0
        temparr=inputs
        for i in range(0, len(self.weights)):
            sum+=temparr[i]+self.weights[i]

        return self.activate(sum)

    def train(self, input, desired):
        guess=self.feedforward(input)
        error=desired-guess
        #adjust the weight
        for i in range(0,len(self.weights)):
            self.weights[i]+=self.learningconstant*error*input[i]



class Trainer(object):
    input=[]
    def __init__(self,x,y,a):
        self.answer=a
        bias=1

        self.input.append(x)
        self.input.append(y)
        self.input.append(bias)


class Walker(object):


    def __init__(self, x, y, width, height):
        self.posx=x
        self.posy=y
        self.width=width
        self.height=height

    def walk(self):
        choice=random.randint(0,3)
        print(choice)
        if(choice == 0):
            self.posx+=1
        elif choice == 1:
            self.posx-=1
        elif choice == 2:
            self.posy+=1
        elif choice == 3:
            self.posy-=1

        self.posx=self.constrain(self.posx, 0, self.width-1)
        self.posy=self.constrain(self.posy,0, self.height-1)


    def constrain(self, xpos, lowlimit, uplimit ):
        if xpos < lowlimit:
            xpos=lowlimit
            return xpos
        elif xpos> uplimit:
            xpos=uplimit
            return xpos
        else:
            return xpos


    def display(self, screen):
        pygame.draw.ellipse(screen, 0xfffff, (self.posx, self.posy,16, 16))
        pygame.display.flip()



