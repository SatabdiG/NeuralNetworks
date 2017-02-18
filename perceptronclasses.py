import random
from datetime import datetime

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


