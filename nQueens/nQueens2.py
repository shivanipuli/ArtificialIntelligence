import time
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

# def is_valid(lis):
#     if len(set(lis+[-1]))!=len(lis)-lis.count(-1)+1:
#         return False
#     differences=[x-lis[x] for x in range(len(lis)) if lis[x]!=-1]
#     if len(set(differences))!=len(differences):
#         return False
#     sums=[x+lis[x] for x in range(len(lis)) if lis[x]!=-1]
#     if len(set(sums))!=len(sums):
#         return False
#     return True

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

# myT=time.perf_counter()
# state=nQueens(31) #31 = 2.5seconds 32=1.5s
# print("Backtracking: " + str(state))
# print("Valid: " + str(test_solution(state)))
# print()
# state=nQueens(32) #31 = 2.5seconds 32=1.5s
# print("Backtracking: " + str(state))
# print("Valid: " + str(test_solution(state)))
# print()
# print("Total Time: " + str(time.perf_counter()-myT))

print(nQueens(11))