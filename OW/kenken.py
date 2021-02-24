import sys

template=""
boxConstraints={}
with open(sys.argv[1]) as f:
    for line in f:
        if template=="":
            template=line.strip()
        else:
            letter, num, operation = line.strip().split(" ")
            boxConstraints[letter] = [num, operation]
N=int(len(template)**.5)
boxToInd={}
for ind in range(N**2):
    tempBox=boxToInd.get(template[ind],[])
    boxToInd.update({template[ind]: tempBox+[ind]})

def print_puzzle(board):
    for x in range(N):
        print((" ").join(board[:N]))
        board=board[N:]
    print()

def is_valid(state,index,num):
    row=index//N
    if str(num) in state[row*N:(row+1)*N]:
        return False
    col=index%N
    if str(num) in [state[ind] for ind in range(col,N**2,N)]:
        return False
    box=template[index]
    state = state[:index] + str(num) + state[index + 1:]
    if "." in [state[ind] for ind in boxToInd[box]]:
        return True
    vals = [int(state[ind]) for ind in boxToInd[box]]
    operation=boxConstraints[box][1]
    result=int(boxConstraints[box][0])
    if operation=="+":
        total=sum(vals)
        if total!=result:
            return False
    elif operation=="-":
        total=max(vals)*2-sum(vals)
        if total!=result:
            return False
    elif operation == "x":
        total = result
        for num in vals:
            total /= num
        if total != 1:
            return False
    else: #boxConstraints[box][1] == "/":
        total = max(vals)**2
        for num in vals:
            total /= num
        if total != result:
            return False
    return True


def get_sorted_values(state,index):
    possible=set()
    for num in range(1,N+1):
        if is_valid(state,index,num):
            possible.add(num)
    return possible

def csp_backtracking(state):
    if "." not in state:
        return state
    ind=state.index(".")
    for variable in get_sorted_values(state, ind):
        new_state = state[:ind] + str(variable) + state[ind + 1:]
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None


new_board="."*(N**2)
print(csp_backtracking(new_board))
