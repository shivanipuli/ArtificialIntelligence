# Need to download mnist_test.csv from web for fully functioning code
# Then test using mnist_testing.py

import numpy as np
import random,sys,math
import csv

def help_s(num):
    num =2.7182818284590452353602874713527**(-num)
    return 1 / (1 + num)

def sigmoid(num):
    A=np.vectorize(help_s)
    return A(num)

def deriv_sigmoid_help(num):
    n=sigmoid(num)
    return n*(1-n)

def deriv_sigmoid(num):
    A=np.vectorize(deriv_sigmoid_help)
    return A(num)

def err(y, a):
    return 0.5 *np.linalg.norm(y - a)**2

def error(y, a):
    A=np.vectorize(err)
    return A(y,a)


def make_network(my_list):
    w=[None]
    b=[None]
    for i in range(1,len(my_list)):
        w.append(2 * np.random.rand(my_list[i-1], my_list[i])-1)
        b.append(2 * np.random.rand(1, my_list[i]) - 1)
    return w,b

w,b=make_network([784,300,100,10])
learn_rate=0.05
file = open("mnist_train.csv")
file = csv.reader(file)
outfile = open("save.txt", 'w')

count=0
for line in file:
            x = []
            for r in line:
                x.append(int(r))
            num = x.pop(0)
            y=[0]*10
            y[num]=1

            dots = [np.array([[0]])]*len(w)
            deltas = [np.array([[0]])]*len(w)
            a=[np.array([[0]])]*len(w)
            learn_rate = 0.4

            a[0]=np.array([x])/255
            for i in range(1, len(w)):
                dots[i] = (a[i - 1] @ w[i]) + b[i]
                a[i] = sigmoid(dots[i])
            # print(str(x)+str(a[-1]))
            deltas[-1] = deriv_sigmoid(dots[-1]) * (y - a[-1])
            for i in range(len(w)-2, -1, -1):
                deltas[i] = deriv_sigmoid(dots[i]) * (deltas[i + 1] @ w[i + 1].T)
            for i in range(len(deltas) - 1, 0, -1):
                b[i] = b[i] + learn_rate * deltas[i]
                w[i] = w[i] + learn_rate * (a[i - 1].T @ deltas[i])
            #print(y)
            #temp=list(a[-1][0])
            #answer=temp.index(max(temp))
            #print(answer)
            count+=1
            print(count)
            if count%30000==0:
                outfile.write(str(w))
                outfile.write(str(b))
                break


num_right=0
tot_num=0
file = open("mnist_train.csv")
file = csv.reader(file)
for line in file:
    x = []
    for r in line:
        x.append(int(r))
    num = x.pop(0)
    y = [0] * 10
    y[num] = 1

    a=[np.array([[0]])]*len(w)
    a[0] = np.array([x]) / 255
    for i in range(1, len(w)):
        dot = (a[i - 1] @ w[i]) + b[i]
        a[i] = sigmoid(dot)
    temp = list(a[-1][0])
    answer = temp.index(max(temp))
    if answer==num:
        num_right+=1
    tot_num+=1
    print("Training Accuracy: %s" %(100*num_right/tot_num))
outfile.write(str(100*num_right/tot_num))


num_right=0
tot_num=0
file = open("mnist_test.csv")
file = csv.reader(file)
for line in file:
    x = []
    for r in line:
        x.append(int(r))
    num = x.pop(0)
    y = [0] * 10
    y[num] = 1

    a=[np.array([[0]])]*len(w)
    a[0] = np.array([x]) / 255
    for i in range(1, len(w)):
        dot = (a[i - 1] @ w[i]) + b[i]
        a[i] = sigmoid(dot)
    temp = list(a[-1][0])
    answer = temp.index(max(temp))
    if answer==num:
        num_right+=1
    tot_num+=1
    print("Testing Accuracy: %s" %(100*num_right/tot_num))
outfile.write(str(100*num_right/tot_num))
