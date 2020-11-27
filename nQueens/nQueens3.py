import time, random
from heapq import heappop, heappush, heapify

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    return True

def collisions(board,ind):
    count=board.count(board[ind])-1 # number of column conflicts
    myDiff=ind-board[ind]
    differences=[x-board[x] for x in range(len(board))]
    count += differences.count(myDiff)-1 # number of diag1 coflicts
    mySum=ind+board[ind]
    sums=[x+board[x] for x in range(len(board)) if board[x]!=-1]
    count+=sums.count(mySum)-1
    return count

def print_board(board):
    size=len(board)
    for i in board:
        print("-"*i + "*" + "-"*(size-1-i))
    print()

def makeRandom(size):
    lis=[i for i in range(size)]
    random.shuffle(lis)
    return lis

def get_sorted_values(state,row):
    col=state[row]
    lis=[]
    for num in range(len(state)):
        if num!=col:
            new_state = state[:row] + [num] + state[row + 1:]
            val=collisions(new_state,row)
            lis.append((val,num))
    heapify(lis)
    return lis

def get_next_unassigned_var(state,conflicts):
    maxNum=max(conflicts)
    choices=[row for row in range(len(state)) if conflicts[row]==maxNum]
    return random.choice(choices)

def solve(state,conflicts):
    if sum(conflicts)==0:
        return state
    print("Board: " + str(state))
    print("Conflicts: " + str(sum(conflicts)))
    row=get_next_unassigned_var(state,conflicts)#conflicts.index(max(conflicts)) # gets row w max conflicts
    for new_conflict,col in get_sorted_values(state,row):
        new_state = state[:row] + [col] + state[row + 1:]
        result = solve(new_state,[collisions(new_state,i) for i in range(len(new_state))])
        if result is not None:
            return result
    return None


def solvePuzzle(size):
    board=makeRandom(size)
    conflict=[collisions(board,i) for i in range(len(board))]
    return solve(board,conflict)


def csp_get_sorted_values(state,row,col,d1,d2):
    var = []
    size = len(state)
    for num in range(size // 2, size):
        if col[num] and d1[row + num] and d2[row - num - 1 + size]:
            var.append(num)
        count = 0
    for num in range(size // 2 - 1, -1, -1):
        if col[num] and d1[row + num] and d2[row - num - 1 + size]:
            var.insert(count,num)
            count += 2
    return reversed(var)
    # for num in range(size):
    #     if col[num] and d1[row+num] and d2[row-num-1+size]:
    #         var.append(num)
    # return var

def csp_get_next_unassigned_var(state):
    #sorts row so that middle rows are checked first
    size = len(state)
    fringe=[ (abs(size//2-i),i) for i in range(size) if state[i]==-1]
    heapify(fringe)
    return heappop(fringe)[1]


def csp_backtracking(state,col,d1,d2):
    if -1 not in state:
        return state
    row=csp_get_next_unassigned_var(state)
    for column in csp_get_sorted_values(state,row,col,d1,d2):
        col[column]=False
        d1[row+column]=False
        d2[row-column-1+len(state)]=False
        new_state=state[:row]+[column]+state[row+1:]
        result=csp_backtracking(new_state,col,d1,d2)
        if result is not None:
            return result
        col[column] = True
        d1[row + column] = True
        d2[row - column - 1 + len(state)] = True
    return None

def nQueens(n):
    column=[True]*n
    diag1=[True]*(2*n-1)
    diag2=diag1.copy()
    return csp_backtracking([-1]*n,column,diag1,diag2)

myT=time.perf_counter()
state=nQueens(31) #31 = 2.5seconds 32=1.5s
print("Backtracking: " + str(state))
print("Check  Solution: " + str(test_solution(state)))
print()
state=nQueens(32) #31 = 2.5seconds 32=1.5s
print("Backtracking: " + str(state))
print("Check  Solution: "  + str(test_solution(state)))
print()


flawedBoard=solvePuzzle(35)
print(flawedBoard)
#print_board(nQueens)
print("Conflicts: 0")
print("Check  Solution: " + str(test_solution(flawedBoard)))
print()

flawedBoard=solvePuzzle(37)
print(flawedBoard)
print("Conflicts: 0")
print("Check  Solution: " + str(test_solution(flawedBoard)))
print()
print("Total Time: %ss" %(time.perf_counter()-myT))