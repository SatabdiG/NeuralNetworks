from perceptronclasses import *

training=[None]*2000
count=0

def f(x):
    return 2*x+1

#Setup
width=640
height=240


ptron=Perceptron(3)

for i  in range(0, 2000):
    x=random.uniform(-width/2, width/2)
    y=random.uniform(-height/2, height/2)
    answer=1
    if(y<f(x)):
        answer=-1
    training[i]=Trainer(x,y,answer)


#train for trainning values
for i in range(0, len(training)):
    #print training[i].answer
    ptron.train(training[i].input, training[i].answer)

#Evaluate

#testdata
xtets=random.uniform(-width/2, width/2)
yest=random.uniform(-height/2, height/2)
bias=1
inputets=[xtets,yest,bias]
print("Input")
print inputets
guess=ptron.feedforward(inputets)
print("Output")
print(guess)



