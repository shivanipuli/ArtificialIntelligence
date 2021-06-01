import numpy as np
import sys,ast
import math, random

def step(num):
    if num>0:
        return 1
    return 0

def sigmoid(num):
    num*=-1
    return 1/(1+math.exp(num))

def p_net(A,x,w,b):
    new_A=np.vectorize(A)
    a=np.array(x)
    for i in range(len(w)):
        l=a@w[i]+b[i]
        a=new_A(l)
    if a<.49:
        return 0
    return 1




#XOR HAPPENS HERE
w=[np.array([[-1,1],[-1,1]]),np.array([1,1])]
b=[np.array([[1.5,-.5]]),np.array([-1])]
x=np.array([0,1])
#print(p_net(step,x,w,b))

# #DIAMOND
# n7=math.sqrt(2)/2
# w=[np.array([[1,-1,-1,1],[-1,-1,1,1]]),np.array([1,1,1,1])]
# b=[np.array([n7,3*n7,n7,-1*n7]),np.array([-3])]
#
# n7=math.sqrt(2)/2
# w=[np.array([[1,-1,-1,1],[-1,-1,1,1]]),np.array([1,1,1,1])]
# b=[np.array([n7,n7,n7,n7]),np.array([-2.6])]
#
# for i in range(500):
#     in1, in2 = random.randint(-1, 1), random.randint(-1, 1)
#     x = np.array([in1, in2])
#     t=math.sqrt(in1**2+in2**2)<1
#     p=p_net(sigmoid,x,w,b)
#     #print(math.sqrt(in1**2+in2**2)<1)
#     #print(p_net(sigmoid,x,w,b))
#     print(t==p)

if len(sys.argv)==1:
    count = 0
    for i in range(500):
        in1, in2 = random.uniform(-1, 1), random.uniform(-1, 1)
        x = np.array([in1, in2])
        n7 = math.sqrt(2) / 2
        w = [np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([1, 1, 1, 1])]
        b=[np.array([1,1,1,1]),np.array([-2.8])]
        t = math.sqrt(in1 ** 2 + in2 ** 2) < 1
        p = p_net(sigmoid, x, w, b)
        if t == p:
            count+=1
        else:
            p = p_net(sigmoid, x, w, b)
            if p==1:
                print(str(x) +" was classified as inside the circle when it's actually outside")
            else:
                print(str(x) + " was classified as outside the circle when it's actually inside")
    print("%s percent were classified correctly" %(count/5))
elif len(sys.argv)==2:
    x=ast.literal_eval(sys.argv[1])
    x=np.array(x)
    # XOR HAPPENS HERE
    w = [np.array([[-1, 1], [-1, 1]]), np.array([1, 1])]
    b = [np.array([[1.5, -.5]]), np.array([-1])]
    print(p_net(step,x,w,b))
elif len(sys.argv)==3:
    in1,in2=ast.literal_eval(sys.argv[1]),ast.literal_eval(sys.argv[2])
    x=np.array([in1,in2])
    n7 = math.sqrt(2) / 2
    w = [np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([1, 1, 1, 1])]
    b = [np.array([n7, 3 * n7, n7, -1 * n7]), np.array([-3])]
    if p_net(step,x,w,b)==0:
        print("outside")
    else:
        print("inside")
