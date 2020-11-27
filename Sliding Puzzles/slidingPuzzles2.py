import queue, time, sys
from collections import deque
from heapq import heappop,heappush,heapify

totTime=time.perf_counter()
#goalStates=["ABC.", "123.", "12345678.", ]
rights=[[],[],[1,3],[2,5,8],[3,7,11,15],[4,9,14,19,24]]
def print_puzzle(size,board):
    for x in range(size):
        print((" ").join(board[:size]))
        board=board[size:]
    print()

def find_goal(board):
    return "".join(sorted(board.replace(".","")))+"."

def get_children(board):
    size=int(len(board)**.5)
    index=board.index(".")
    children=[]
    if index not in rights[size]: #it can swap right #12.3
        children.append(board[:index]+board[index+1]+"."+board[index+2:])
    if index%size !=0: #it can swap left
        children.append(board[:index-1] + "." + board[index-1] + board[index + 1:])
    if index>=size: #it can swap up
        children.append(board[:index-size]+"."+board[index-size+1:index]+board[index-size]+board[index+1:])
    if index<size*(size-1):#it can swap down
        children.append(board[:index]+board[index+size]+board[index+1:index+size]+"."+board[index+size+1:])
    return children

def goal_test(board):
    return board=="".join(sorted(board.replace(".","")))+"."


#<------Finding Path---------->
def findPath(board):
    visited= set()
    fringe=queue.Queue()
    fringe.put(board)
    previous={board:None}
    while not fringe.empty():
        state=fringe.get()
        if state==find_goal(board):
            path=[state]
            while board not in path:
                path+=[previous[path[-1]]]
            path.reverse()
            return path
        if state not in visited:
            visited.add(state)
            for item in get_children(state):
                if item not in previous.keys():
                    previous[item]=state
                fringe.put(item)
    return None

def isSolvable(board):
    even = False
    size=len(board)**.5
    if (board.find(".") // size) % 2 == 0:
        even = True
    board=board.replace(".", "")
    outOrder = 0
    for i in range(len(board)-1):
        for y in range(i + 1, len(board)):
            if board[i] > board[y]:
                outOrder += 1
    #print((even,inOrder))
    if size%2 ==1: #if 3x3 grid or 5x5 grid
        return outOrder % 2 ==0
    return (even and outOrder % 2 == 1) or (not even and outOrder % 2 == 0)

#<------BFS Searching--------->
def BFSMoves(board):
    visited= set()
    fringe=deque()#queue.Queue()
    fringe.append(board)
    #fringe.put(board)
    moves=0
    moves1=1
    moves2=0
    while len(fringe)!=0: #not fringe.empty():
        state=fringe.popleft()#get()
        moves1-=1
        if goal_test(state):
            return moves
        if state not in visited:
            visited.add(state)
            for item in get_children(state):
                fringe.append(item)#put(item)
                moves2+=1
        if moves1 == 0:
            moves,moves1,moves2=moves+1,moves2,0
    return None

def kDFSMoves(board,k):
    temp_set = set()
    temp_set.add(board)
    fringe=[(board,0,temp_set)]
    while len(fringe)>0:
        state,depth,ancestors=fringe.pop()
        if goal_test(state):
            return depth
        if depth<k:
            for child in get_children(state):
                if child not in ancestors:
                    newSet=ancestors.copy()
                    newSet.add(child)
                    fringe.append((child,depth+1,newSet))
    return None

def DFSMoves(board):
    max_depth=0
    result=None
    while result is None:
        result=kDFSMoves(board,max_depth)
        max_depth+=1
    return result

#<-------DFS vs BFS-------->
# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         if not isSolvable(line):
#             print("Line %s: %s, No moves found" % (str(count), line))
#         else:
#             myTime = time.perf_counter()
#             moves = str(BFSMoves(line))
#             myTime = str(time.perf_counter()-myTime)
#             print("Line %s: %s, BFS - %s moves found in % seconds" %( str(count),line,moves, myTime ))
#             myTime = time.perf_counter()
#             moves = str(DFSMoves(line))
#             myTime = str(time.perf_counter() - myTime)
#             print("Line %s: %s, ID-DFS - %s moves found in % seconds" %( str(count),line,moves, myTime))
#             print()
#         count+=1

def taxiCab(board):
    goal_state=find_goal(board)
    size=int(len(board)**.5)
    count=0
    for i in range(len(board)):
        num=board[i]
        if not board[i] == ".":
            xDist = abs(goal_state.find(num) // size - i // size)
            yDist = abs(goal_state.find(num) % size-i % size)
            count += xDist+yDist
    return count



# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         print("Line %s: %s" %( str(count),taxiCab(line)))
#         count+=1

def ASearch(board):
    checked=set()
    checked.add(board)
    totDist=taxiCab(board)
    fringe=[(totDist,board,0)]
    heapify(fringe)
    while len(fringe)>0:
        dist,state,moves=heappop(fringe)
        if goal_test(state):
            return moves
        for child in get_children(state):
            if child not in checked:
                heappush(fringe,(moves+1+taxiCab(child),child,moves+1))
                checked.add(child)
    return None

with open(sys.argv[1]) as f:
    count=0
    for line in f:
        if "\n" in line:
            line=line[:-1]
        vars=line.split(" ")
        myTime = time.perf_counter()
        if not isSolvable(vars[1]):
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, No solution found in %s seconds" % (str(count), vars[1], myTime))
        elif vars[2]=="B":
            myTime=time.perf_counter()
            moves = str(BFSMoves(vars[1]))
            myTime = str(time.perf_counter()-myTime)
            print("Line %s: %s, BFS - %s moves found in % seconds" %( str(count),vars[1],moves, myTime))
        elif vars[2]=="I":
            myTime = time.perf_counter()
            moves = str(DFSMoves(vars[1]))
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, DFS - %s moves found in % seconds" % (str(count), vars[1], moves, myTime))
        elif vars[2]=="A":
            myTime = time.perf_counter()
            moves = str(ASearch(vars[1]))
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, A* - %s moves found in % seconds" % (str(count), vars[1], moves, myTime))
        else:
            myTime = time.perf_counter()
            moves = str(BFSMoves(vars[1]))
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, BFS - %s moves found in % seconds" % (str(count), vars[1], moves, myTime))
            myTime = time.perf_counter()
            moves = str(DFSMoves(vars[1]))
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, DFS - %s moves found in % seconds" % (str(count), vars[1], moves, myTime))
            myTime = time.perf_counter()
            moves = str(ASearch(vars[1]))
            myTime = str(time.perf_counter() - myTime)
            print("Line %s: %s, A* - %s moves found in % seconds" % (str(count), vars[1], moves, myTime))
        print()
        count+=1
totTime=time.perf_counter()-totTime
print("Total Time: "+ str(totTime) + " seconds")