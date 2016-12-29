import numpy as np

#Trainning sample
#Input
x=np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
#output
y=np.array([[0],[1],[1],[0]])


#sigmoig function
def nonlin(x, deriv=False):
    if(deriv==True):
        return x*(1-x)
    else:
        return 1/(1+np.exp(-x))


np.random.seed(1)
#Two sets of weights
sym0=2*np.random.random((3,4))-1
sym1=2*np.random.random((4,1))-1

for iter in range(6000):
    l0=x
    l1=nonlin(np.dot(l0,sym0))
    l2=nonlin(np.dot(l1,sym1))

    ##backpropgation
    #error of l2
    l2_error=y-l2
    l2_delta=l2_error*(nonlin(l2,True))
    sym1+=np.dot(l1.T,l2_delta)

    #error of l1
    l1_error=l2_delta.dot(sym1.T)
    l1_delta=l1_error*(nonlin(l1, True))

    sym0+=np.dot(l0.T,l1_delta)



l1=nonlin(np.dot(x.T,sym1))
print(l1)
