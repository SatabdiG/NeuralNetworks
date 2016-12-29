#Toy Neural network for experimentation

import numpy as np
import  matplotlib.pyplot as plt

x= np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])

y=np.array([[0,1,1,0]]).T

#sigmoid
def nonlin(x, deriv=False):
    if(deriv == True):
        return x*(1-x)
    else:
        return 1/(1+np.exp(-x))


Xacis=np.arange(-5,5,0.2)
#plt.plot(Xacis, nonlin(Xacis))
#plt.show()

np.random.seed(1)

#install the weights
sym0=2*np.random.random((3,1))-1
print(sym0)

for iter in range(15000 ):
    #forward propogation
    l0=x
    l1=nonlin(np.dot(l0, sym0))

    #Errow
    l1_error=y-l1

    #multiply how much we missed by slope of the sigmoid
    l1_delta= l1_error*nonlin(l1, True)

    #update the weights
    sym0+=np.dot(l0.T,l1_delta)



x1= np.array([[1,0,1],[1,1,1],[0,0,1],[0,1,1]])
l1=nonlin(np.dot(x1,sym0))
print("Output")
print(l1)