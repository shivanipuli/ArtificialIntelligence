import time, sys
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


def is_valid(lis):
    if len(set(lis + [-1])) != len(lis) - lis.count(-1) + 1:
        return False
    differences = [x - lis[x] for x in range(len(lis)) if lis[x] != -1]
    if len(set(differences)) != len(differences):
        return False
    sums = [x + lis[x] for x in range(len(lis)) if lis[x] != -1]
    if len(set(sums)) != len(sums):
        return False
    return True


def get_sorted_values(state, row):
    # sorts values so that edges are checked first
    size = len(state)
    var=[num for num in range(size//2) if is_valid(state[:row] + [num] + state[row + 1:])]
    count=0
    for num in range(size-1,size//2-1,-1):
        if is_valid(state[:row] + [num] + state[row + 1:]):
            var.insert(count, num)
            count += 2
    return var
    # var = []
    # size = len(state)
    # for num in range(size // 2, size):
    #     temp = state[:row] + [num] + state[row + 1:]
    #     if is_valid(temp):
    #         var.append(num)
    # if row!=len(state)//2:
    #     count = 0
    #     for num in range(size // 2 - 1, -1, -1):
    #         temp = state[:row] + [num] + state[row + 1:]
    #         if is_valid(temp):
    #             var.insert(count, num)
    #             count += 2
    # return reversed(var)


def get_next_unassigned_var(state):
    # sorts row so that middle rows are checked first
    size = len(state)
    fringe = [(abs(size // 2 - i), i) for i in range(size) if state[i] == -1]
    heapify(fringe)
    return heappop(fringe)[1]


def csp_backtracking(state):
    if -1 not in state:
        return state
    var = get_next_unassigned_var(state)
    for variable in get_sorted_values(state, var):
        new_state = state[:var] + [variable] + state[var + 1:]
        result = csp_backtracking(new_state)
        if result is not None:
            return result
    return None


def nQueens(n):
    return csp_backtracking([-1] * n)


myT = time.perf_counter()
state = nQueens(28)  # 33 = 7seconds
# state=nQueens(int(sys.argv[1]))
print(state)
print(test_solution(state))
print(time.perf_counter() - myT)
