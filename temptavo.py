import numpy as np

import pickle
import csv
EPOCHS = 10000 #?
lr = 0.05
def step(x):
    if x > 0:
        return 1
    else:
        return 0


def sigstep(x):
    if x >= 0.5:
        return 1
    else:
        return 0

def sigmoid(x):
    return 1 / (1 + (2.7182818284590452353602874713527 ** -x))


a1 = 1.0000000000001


def p_net(x, input, w_list, b_list):
    start = np.array(input)
    x = np.vectorize(x)
    for a in range(len(w_list)):
        start = x((start @ w_list[a]) + b_list[a])
    return start


def sigmoidd(x):
    return sigmoid(x)*(1-sigmoid(x))
def error(exepected,obtained):
    sum = 0
    for a in range(len(exepected)):
        sum += (exepected[a]-obtained[a])**2
    return sum*0.5

def create_random(size):
    weights = []
    biases = []
    for a in range(len(size)-1):
        weights.append(2 * np.random.rand(size[a], size[a+1]) - 1)
        biases.append(2 * np.random.rand(1, size[a+1]) - 1)
    return weights,biases
def bp(x,weights,biases):
    x = np.vectorize(x)
    for abc in range(EPOCHS):
        for pp in range(len(weights)):
            np.savetxt("weights%s%s.csv"%(abc,pp),weights[pp],delimiter=',')
        for pp in range(len(biases)):
            np.savetxt("biases%s%s.csv" % (abc, pp), biases[pp], delimiter=',')
        savefile = open("saved.txt", 'w')
        print(abc)
        savefile.write(str(weights))
        savefile.write(str(biases))
        savefile.close()
        # pickle.dump((weights,biases),savefile)
        training = open("mnist_train.csv")
        training = csv.reader(training)
        for line in training:
            cur = []
            for b in line:
                cur.append(int(b))
            target = cur[0]
            if target==0:
                y = np.array([1,0,0,0,0,0,0,0,0,0])
            elif target==1:
                y = np.array([0,1,0,0,0,0,0,0,0,0])
            elif target==2:
                y = np.array([0,0,1,0,0,0,0,0,0,0])
            elif target==3:
                y = np.array([0,0,0,1,0,0,0,0,0,0])
            elif target==4:
                y = np.array([0,0,0,0,1,0,0,0,0,0])
            elif target==5:
                y = np.array([0,0,0,0,0,1,0,0,0,0])
            elif target==6:
                y = np.array([0,0,0,0,0,0,1,0,0,0])
            elif target==7:
                y = np.array([0,0,0,0,0,0,0,1,0,0])
            elif target==8:
                y = np.array([0,0,0,0,0,0,0,0,1,0])
            else:
                y = np.array([0,0,0,0,0,0,0,0,0,1])
            cur = cur[1:]
            cur = np.array(cur)/255
            dot_list = []
            output_list = []
            output_list.append(cur)
            for a in range(len(weights)):
                ad = cur @ weights[a]
                ac = ad + biases[a]
                # dot = (cur @ weights[a]) + biases[a]
                dot = ac
                dot_list.append(dot)
                cur = np.squeeze(x(dot))
                output_list.append(cur)
            delta = sigmoidd(dot_list[-1]) * (y-output_list[-1])
            delta_list = dict()
            delta_list[len(weights)-1] = delta
            for i in range(len(weights)-2,-1,-1):
                delta_list[i]= sigmoidd(dot_list[i]) * (delta_list[i+1] @ np.transpose(weights[i+1]))
            for a in range(len(weights)):
                biases[a] = biases[a] + (lr*delta_list[a])
                d = output_list[a][np.newaxis].transpose()
                c = delta_list[a][np.newaxis]
                e = d @ c
                weights[a] = weights[a] + lr*(e)
                weights[a] = np.reshape(weights[a],weights[a].shape[1:])
    return weights, biases

weight, bias = create_random([784,300,100,10])
a = bp(sigmoid,weight,bias)