import queue, time, sys
from collections import deque

totTime=time.perf_counter()
goalStates=["ABC.", "123.", "12345678.", ]
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
    return board==find_goal(board)

# <--------Modeling Tasks------------->
# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         print("Line %s start state:" %str(count))
#         print_puzzle(int(line[0]),line[2:])
#         print("Line %s goal state:" % str(count))
#         print_puzzle(int(line[0]),find_goal(line[2:]))
#         print("Line %s children:" %str(count))
#         for item in get_children(line[2:]):
#             print_puzzle(int(line[0]),item)
#         count+=1


def getStates(board):
    visited= set()
    #fringe= [board]
    fringe=queue.Queue()
    fringe.put(board)
    #while len(fringe)!=0:
    while not fringe.empty():
        #state=fringe.pop()
        state=fringe.get()
        if state not in visited:
            visited.add(state)
            for item in get_children(state):
                #fringe.append(item)
                fringe.put(item)
    return len(visited)
#print("2x2: " + str(getStates("ABC.")))
#print("3x3: " + str(getStates("12345678.")))

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

# #path=findPath("13.425786")
# path=findPath("8672543.1")
# print("Longest state took 31 moves: ")
# for item in path:
#     print_puzzle(3,item)


with open(sys.argv[1]) as f:
    count=0
    for line in f:
        if "\n" in line:
            line=line[:-1]
        path = findPath(line[2:])
        print("Line %s: %s" %(str(count),line[2:]))
        for item in path:
            print_puzzle(int(line[0]), item)
        count+=1
#<------BFS Searching--------->
def findMoves(board):
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

# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         myTime=time.perf_counter()
#         moves = str(findMoves(line[2:]))
#         myTime = str(time.perf_counter()-myTime)
#         print("Line %s: %s, %s moves found in % seconds" %( str(count),line[2:],moves, myTime ))
#         count+=1

#<----------Longest moves path------------->
def largestPath(board):
    visited = set()
    fringe = queue.Queue()
    fringe.put(board)
    moves={board:0}
    movesRev={0:[board]}
    while not fringe.empty():
        state = fringe.get()
        if state not in visited:
            visited.add(state)
            for item in get_children(state):
                fringe.put(item)
                if item not in moves.keys():
                    moveNum=moves[state]+1
                    moves[item]=moveNum
                    movesRev[moveNum]=list(movesRev.get(moveNum,[]))+[item]
    maxNum=max(movesRev.keys())
    return [maxNum,movesRev[maxNum]]


# print("Starting state: ")
# print_puzzle(3,"12345678.")
# lPath=largestPath("12345678.")
# print("%s Moves Found to Ending State: " %str(lPath[0]))
# for item in lPath[1]:
#     print_puzzle(3,item)

# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         myTime=time.perf_counter()
#         moves = str(findMoves(line[2:]))
#         myTime = str(time.perf_counter()-myTime)
#         print("Line %s: %s, %s moves found in % seconds" %( str(count),line[2:],moves, myTime ))
#         count+=1
print(time.perf_counter()-totTime)