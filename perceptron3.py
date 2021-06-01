import sys,ast
def step(num):
    if num>0:
        return 1
    return 0

def perceptron(A,w,b,x): #w*x+b
    num=0
    for i in range(len(w)):
        num+=w[i]*x[i]
    num+=b
    return A(num)


def XOR(ins):
    w3,b3=(1,1),0
    w4,b4=(1, 2),-2
    w5,b5=(1,-1),0
    #XOR HAPPENS HERE
    tup3=perceptron(step,w3,b3,ins)
    tup4=perceptron(step,w4,b4,ins)
    out=perceptron(step,w5,b5,(tup3,tup4))
    return (ins,out)

mytup=ast.literal_eval(sys.argv[1])
print(XOR(mytup))