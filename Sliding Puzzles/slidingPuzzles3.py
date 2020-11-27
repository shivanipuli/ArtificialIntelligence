import queue, time, sys
from collections import deque
from heapq import heappop, heappush, heapify

# <------Optimize Level 1-------->
rights=[[],[],[1,3],[2,5,8],[3,7,11,15],[4,9,14,19,24]]

goalCoord={}
goal_state="ABCDEFGHIJKLMNO"
for num in goal_state:
    xDist = goal_state.find(num) // 4
    yDist = goal_state.find(num) % 4
    goalCoord[num]=(xDist,yDist)


def print_puzzle(size,board):
    for x in range(size):
        print((" ").join(board[:size]))
        board=board[size:]
    print()

def get_children(board):
    size=int(len(board)**.5)
    index=board.index(".")
    children=set()
    if index not in rights[size]: #it can swap right #12.3
        goalX, goalY = goalCoord[board[index + 1]]
        newY=index%size
        if abs(newY+1-goalY)>abs(newY-goalY):
            children.add((-1,board[:index]+board[index+1]+"."+board[index+2:]))
        else:
            children.add((1, board[:index] + board[index + 1] + "." + board[index + 2:]))
    if index%size !=0: #it can swap left
        goalX, goalY = goalCoord[board[index - 1]]
        newY = index% size
        if abs(newY-1-goalY)>abs(newY-goalY):
            children.add((-1,board[:index-1] + "." + board[index-1] + board[index + 1:]))
        else:
            children.add((1,board[:index-1] + "." + board[index-1] + board[index + 1:]))
    if index>=size: #it can swap up
        goalX, goalY = goalCoord[board[index - size]]
        newX=index//size
        if abs(newX-1-goalX)>abs(newX-goalX):
            children.add((-1,board[:index-size]+"."+board[index-size+1:index]+board[index-size]+board[index+1:]))
        else:
            children.add((1, board[:index - size] + "." + board[index - size + 1:index] + board[index - size] + board[index + 1:]))
    if index<size*(size-1):#it can swap down
        goalX, goalY = goalCoord[board[index + size]]
        newX=index//size
        if abs(newX+1 - goalX) > abs(newX- goalX):
            children.add((-1,board[:index]+board[index+size]+board[index+1:index+size]+"."+board[index+size+1:]))
        else:
            children.add((1, board[:index] + board[index + size] + board[index + 1:index + size] + "." + board[                                                                                                    index + size + 1:]))
    return children

def find_goal(board):
    return "".join(sorted(board.replace(".","")))+"."

def goal_test(board):
    return board==find_goal(board)


def taxiCab(board):
    goal_state=find_goal(board)
    size=int(len(board)**.5)
    count=0
    for i in range(len(board)):
        num=board[i]
        if not board[i] == ".":
            x,y=goalCoord[num]
            xDist = abs(x - i // size)
            yDist = abs(y-i % size)
            count += xDist+yDist
    return count

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
        for tup in get_children(state):
            heuristic,child=tup
            if child not in checked:
                heappush(fringe,(dist+heuristic+1,child,moves+1))
                checked.add(child)
    return None

# totTime=time.perf_counter()
# with open(sys.argv[1]) as f:
#     count=0
#     for line in f:
#         if "\n" in line:
#             line=line[:-1]
#         print("Line %s: %s" %( str(count),ASearch(line)))
#         count+=1
#
# totTime=time.perf_counter()-totTime
# print("Total Time: "+ str(totTime) + " seconds")

# <------Extend Level 1-------->
moves = {0: [3, 5], 1: [6, 8], 2: [7, 9], 3: [0, 10, 5, 12], 4: [11, 13], 5: [0, 3, 12, 14], 6: [1, 8], 7: [9, 2],
         8: [1, 6], 9: [7, 2], 10: [3, 12], 11: [4, 13], 12: [3, 5, 10, 14], 13: [11, 4], 14: [12, 5]}


def print_triangle(board):
    index = 0
    for i in range(5, 0, -1):
        string = " " * i
        string += " ".join(board[index:index + 6 - i])
        index = index + 6 - i
        print(string)
    print()


def goalStateTriangle(board):
    return board.count("*") == 1


def get_children_triangle(board):
    children = []
    for i in range(len(board)):
        if board[i] == "*":
            for endInd in moves[i]:
                hopInd = (i + endInd) // 2
                if board[endInd] == "o" and board[hopInd] == "*":
                    newChild = board[:i] + "o" + board[i + 1:]
                    newChild = newChild[:endInd] + "*" + newChild[endInd + 1:]
                    newChild = newChild[:hopInd] + "o" + newChild[hopInd + 1:]
                    children.append(newChild)
    return children


def findPath(board):
    visited = set()
    visited.add(board)
    fringe = [(0, board, [board])]
    heapify(fringe)
    while len(fringe) > 0:
        moves, state, path = heappop(fringe)
        if goalStateTriangle(state):
            return path
        for item in get_children_triangle(state):
            if item not in visited:
                visited.add(item)
                heappush(fringe, (moves + 1, item, path + [item]))
    return None


# path = findPath("o**************")
# for item in path:
#     print_triangle(item)

# <-------Extend Level 2--------->
def print_flood(board):
    size = int(len(board) ** .5)
    for i in range(0, len(board), size):
        print(board[i:i + size])
    print()


def flood(state, color):
    return floodRec(state, state[0], color, 0, 0)


def floodRec(state, initColor, newColor, xPos, yPos):
    size = int(len(state) ** .5)
    index = xPos * size + yPos
    if state[xPos * size + yPos] == initColor:
        state = state[:xPos * size + yPos] + newColor + state[xPos * size + yPos + 1:]
        if xPos < size - 1 and state[(xPos + 1) * size + yPos] == initColor:  # has down neighbor
            state = floodRec(state, initColor, newColor, xPos + 1, yPos)
        if yPos < size - 1 and state[xPos * size + yPos + 1] == initColor:  # has right neighbor
            state = floodRec(state, initColor, newColor, xPos, yPos + 1)
        # if xPos>0 and state[(xPos-1)*size+yPos]==initColor: #has top neighbor
        #    state = floodRec(state, initColor, newColor, xPos - 1, yPos)
        # if yPos>0 and state[xPos*size+yPos-1]==initColor: #has left neighbor
        #    state = floodRec(state, initColor, newColor, xPos, yPos - 1)
    return state


def findSolutionB(board):
    fringe = queue.Queue()
    fringe.put((0, board, [board]))
    while not fringe.empty():
        moves, state, path = fringe.get()
        if len(set(list(state))) == 1:
            return path
        for char in "1234":
            child = flood(state, char)
            fringe.put((moves + 1, child, path + [child]))
    return None


board=sys.argv[1]
board="1324221431243122414123211"
print(len(board))
count = 0
myTime = time.perf_counter()
path=findSolutionB(board)
for item in path:
    print_flood(item)
    count += 1

print("Total Time: " + str(time.perf_counter()-myTime))
print("Total # of Moves: " + str(count))
