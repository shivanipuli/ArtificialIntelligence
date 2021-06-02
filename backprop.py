import numpy as np
import sys,random,math
from random import uniform

def help_s(num):
    num *= -1
    return 1 / (1 + math.exp(num))
def sigmoid(num):
    A=np.vectorize(help_s)
    return A(num)

def deriv_sigmoid_help(num):
    n=sigmoid(num)
    return n*(1-n)

def deriv_sigmoid(num):
    A=np.vectorize(deriv_sigmoid_help)
    return A(num)

def in_circle(x,y):
    if math.sqrt(x ** 2 + y ** 2) < 1:
        return 1
    return 0

def error(y, a):
    return 0.5 *np.linalg.norm(y - a)**2

def step_helper(num):
    if num>.5:
        return 1
    return 0

def step(num):
    A=np.vectorize(step_helper)
    return A(num)

#CHALLENGE 1
# learn_rate=0.1
# w=[None,np.array([[1,-.5],[1,.5]]),np.array([[1,2],[-1,-2]])]
# b=[None,np.array([[1,-1]]),np.array([[-.5,.5]])]
# epoch=2
# x=np.array([[2,3]])
# y=np.array([[0.8,1]])
# dots=[0]*3
# deltas=[0,0,0]
# a=[0,0,0]
# for epo in range(epoch):
#     a[0]=x
#     for i in range(1,3):
#         dots[i]=(a[i-1]@w[i])+b[i]
#         a[i]=sigmoid(dots[i])
#     print(error(y,a[-1]))
#     deltas[-1]=deriv_sigmoid(dots[-1])*(y-a[-1])
#     for i in range(1,-1,-1):
#         deltas[i]=deriv_sigmoid(dots[i])*(deltas[i+1]@w[i+1].T)
#     for i in range(1,len(deltas)):
#         b[i]=b[i]+learn_rate*deltas[i]
#         w[i]=w[i]+learn_rate*(a[i-1].T@deltas[i])

#<-------CHALLENGE 2----------->
if sys.argv[1]=="S":
    learn_rate=.05
    training=[(np.array([0,0]),np.array([0,0])),
              (np.array([0,1]),np.array([0,1])),
              (np.array([1,0]),np.array([0,1])),
              (np.array([1,1]),np.array([1,0]))]
    w=[None, np.array([[random.uniform(-1,1),random.uniform(-1,1)],[random.uniform(-1,1),random.uniform(-1,1)]]),np.array([[random.uniform(-1,1),random.uniform(-1,1)],[random.uniform(-1,1),random.uniform(-1,1)]])]
    b=[None,np.array([random.uniform(-1,1),random.uniform(-1,1)]),np.array([random.uniform(-1,1),random.uniform(-1,1)])]
    a=[0,0,0]
    dots=[0,0,0]
    deltas=[np.array([0,0])]*3
    new_vals=[0,0,0,0]
    y_vals=[i[1] for i in training]

    for t in range(1):
        learn_rate = random.uniform(2,5)
        for epo in range(2000):
            new_vals=[]
            for x,y in training:
                a[0]=x
                for i in range(1,len(w)):
                    dots[i] = (a[i - 1] @ w[i]) + b[i]
                    a[i]=sigmoid(dots[i])
                #print(str(x)+str(a[-1]))
                deltas[-1]=deriv_sigmoid(dots[-1])*(y-a[-1])
                for i in range(1,-1,-1):
                    deltas[i]=deriv_sigmoid(dots[i])*(deltas[i+1]@w[i+1].T)
                for i in range(len(deltas)-1,0,-1):
                    b[i]=b[i]+learn_rate*deltas[i]
                    w[i]=w[i]+learn_rate*(a[i-1].T@deltas[i])
                print(a[-1])
                new_vals.append(a[-1])


    print("Final Test:")
    for input,output in training:
        print("Input: " + str(input))
        for i in range(1, 3):
            input = sigmoid((input @ w[i]) + b[i])
        input=step(input)
        print("Output: " + str(output))

#<--------CHALLENGE 3-------->
else:
    training=[]
    with open("10000_pairs.txt") as f:
        for line in f:
            line=line.strip()
            x=line.split()
            x=[float(x[0]),float(x[1])]
            y=in_circle(x[0],x[1])
            training.append((np.array([[float(x[0]),float(x[1])]]),[in_circle(x[0],x[1])]))

    n7 = math.sqrt(2) / 2
    w = [None,np.array([[1, -1, -1, 1], [-1, -1, 1, 1]]), np.array([[1, 1, 1, 1]]).T]
    b = [None,np.array([[n7, 3 * n7, n7, -1 * n7]]), np.array([[-3]])]
    a=[0,0,0]
    dots=[0,0,0]
    deltas=[np.array([0,0])]*3

    for t in range(1):
        learn_rate = 0.4
        for epo in range(100):
            for x,y in training:
                a[0]=np.array(x)
                for i in range(1,3):
                    dots[i] = (a[i - 1] @ w[i]) + b[i]
                    a[i]=sigmoid(dots[i])
                #print(str(x)+str(a[-1]))
                deltas[2]=deriv_sigmoid(dots[2])*(y-a[2])
                for i in range(1, -1, -1):
                    deltas[i]=deriv_sigmoid(dots[i])*(deltas[i+1]@w[i+1].T)
                for i in range(len(deltas)-1,0,-1):
                    b[i]=b[i]+learn_rate*deltas[i]
                    w[i]=w[i]+learn_rate*(a[i-1].T@deltas[i])
            #post training
            num_wrong=0
            for x,y in training:
                a[0] = np.array(x)
                for i in range(1, 3):
                    dots[i] = (a[i - 1] @ w[i]) + b[i]
                    a[i] = sigmoid(dots[i])
                a[-1]=step(a[-1])
                if int(a[-1])!=int(y[0]):
                    num_wrong+=1
            print("Epoch %s misclassified points: %s" %(epo,num_wrong))



# for input,output in training:
#     print("Input: " + str(input))
#     for i in range(1, 3):
#         input = sigmoid((input @ w[i]) + b[i])
#     input=step(input)
#     print("Output: " + str(input))