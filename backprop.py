import numpy as np
import sys,random,math

learn_rate=0.1
w=[None,np.array([[-1,1],[-.5,.5]]),np.array([[1,-1],[2,-2]])]
b=[None, np.array([[1,-1]]),np.array([[-.5,.5]])]

def sigmoid(num):
    num*=-1
    return 1/(1+math.exp(num))

def deriv_sigmoid(num):
    n=sigmoid(num)
    return n*(1-n)

def s_error(y, a):
    return 0.5 *np.linalg.norm(y - a)**2

epoch=1
x=np.array([[2,3]])
y=np.array([[0.8,1]])
for i in range(epoch):
    for