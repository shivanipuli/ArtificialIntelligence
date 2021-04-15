import ast,sys

def pretty_print_tt(table):
    for tuple1 in table:
        ins,out=tuple1
        print_this=""
        for item in ins:
            print_this+=str(item)+" "
        print_this+="| "+str(out)
        print(print_this)
    print()

def truth_table(bits,n):
    outs=bin(n)
    outs=outs[2:]
    if len(outs)<2**bits:
        outs="0"*(2**bits-len(outs))+outs
    ins=[(1,),(0,)]
    #if bits==1:
    #    return [((1),int(outs[0])),((0),int(outs[1]))]
    for i in range(bits-1):
        new_ins=[]
        for tup in ins:
            new_ins.append(tup+(1,))
            new_ins.append(tup+(0,))
        ins=new_ins
    toreturn=[]
    for tup in ins:
        toreturn.append((tup,int(outs[0])))
        outs=outs[1:]
    return toreturn

def step(num):
    if num>0:
        return 1
    return 0

def perceptron(A,w,b,x):
    num=0
    for i in range(len(w)):
        num+=w[i]*x[i]
    num+=b
    return A(num)

def check(n,w,b):
    mytable=truth_table(len(w),n)
    #pretty_print_tt(mytable)
    accuracy=0
    for row in mytable:
        ins,out=row[0],row[1]
        if perceptron(step,w,b,ins)==out:
            accuracy+=1
    accuracy/=2**len(w)
    return accuracy

# #print(bin(100))
# myt=truth_table(5,70)
# print(myt)
# pretty_print_tt(myt)

#print(perceptron(step, (1,1), -1.5, (1,0)))

n=ast.literal_eval(sys.argv[1])
w=ast.literal_eval(sys.argv[2])
b=ast.literal_eval(sys.argv[3])
print(check(n,w,b))