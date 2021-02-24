import queue, time, sys

def print_puzzle(board):
    board=board.replace(" ","-")
    for i in range(6):
        print(" ".join(board[i*6:(i+1)*6]))
    print()

def goal_state(board):
    if "*" not in board:
        print_puzzle(board)
    return board.rindex("*")==17

def getChildren(board):
    #print_puzzle(board)
    cars=set(list(board))
    cars.remove(" ") #empty spaces in cars
    children=set()
    for car in cars:
        horizontal=True
        length=board.count(car)
        ind=board.index(car)
        rInd=board.rindex(car)
        if ind+length-1 != rInd: #checks if car is horizontal or vertical
            horizontal=False
        if horizontal:
            moveLeft= ind%6!=0 and board[ind-1]==" " #can move left
            count=1
            while moveLeft and count<=6:
                tempboard=board[:ind-count]+(car*length)+(" "*count)+board[rInd+1:]
                children.add(tempboard)
                count+=1
                moveLeft=(ind-count+1)%6!=0 and (ind-count+1)>=0 and board[ind-count]==" "
            moveRight=rInd%6!=5 and board[rInd+1]==" "
            count=1
            while moveRight and count<=6:
                tempboard=board[:ind]+(" "*count)+(car*length)+board[rInd+1+count:]
                children.add(tempboard)
                count+=1
                moveRight=(rInd+count)%6!=0 and rInd+count<36 and board[rInd+count]==" "
        else: #if car is vertical
            moveUp=ind//6>0 and board[ind-6]==" "
            count=1
            tempList = list(board)
            while moveUp and count<=6:
                tempList[ind-6*count]=car
                tempList[rInd-6*(count-1)]=" "
                children.add("".join(tempList))
                count += 1
                moveUp = (ind - 6*count) >= 0 and board[ind - 6*count] == " "
            tempList = list(board)
            moveDown = rInd // 6 < 5 and board[rInd + 6] == " "
            count=1
            while moveDown and count <= 6:
                tempList[ind + 6 * (count-1)] = " "
                tempList[rInd + 6 * count] = car
                children.add("".join(tempList))
                count += 1
                moveDown =  (rInd + 6 * count) < 36 and board[rInd + 6 * count] == " "
    return children


def kDFSMoves(board,k):
    temp_set = set()
    temp_set.add(board)
    fringe=[(board,[board],temp_set)]
    while len(fringe)>0:
        state,path,ancestors=fringe.pop()
        if goal_state(state):
            return path
        if len(path)<k:
            for child in getChildren(state):
                if child not in ancestors:
                    newSet=ancestors.copy()
                    newSet.add(child)
                    fringe.append((child,path+[child],newSet))
    return None

def DFSsearch(board):
    max_depth=0
    result=None
    while result is None:
        print(max_depth)
        result=kDFSMoves(board,max_depth)
        max_depth+=1
    return result

def get_children(board):
    cars = set(list(board))
    grid=[]
    for i in range(6):
        grid.append(board[i*6:i*6+6])
    cars.remove(" ")  # empty spaces in cars
    children = set()
    for car in cars:
        horizontal = True
        length = board.count(car)
        xPos=board//6
        yPos=board%6
        ind=board.index(car)
        rInd=board.rindex(car)
        if ind + length - 1 != rInd:  # checks if car is horizontal or vertical
            horizontal = False
        if horizontal:
            print()
            #move left
            #move right
        else:
            print()
            #move up
            #move down
    return children

def BFSsearch(board):
    visited=set()
    visited.add(board)
    fringe = queue.Queue()
    fringe.put((0, board, [board]))
    while not fringe.empty():
        moves, state, path = fringe.get()
        if goal_state(state):
            return path
        for child in getChildren(state):
            if child not in visited:
                visited.add(child)
                fringe.put((moves + 1, child, path + [child]))
    return None


myBoard="AA  BCDDD BCE** FGE H FG IHJJ  IKKK "
myBoard="        ABCD**ABCDEFFBC EGH   EGHIII"

#print_puzzle(myBoard)
myTime=time.perf_counter()
count=0 #to exclude initial state
for item in BFSsearch(myBoard):
    print_puzzle(item)
    count+=1
print("Number of Moves: " + str(count))
print("Total Time: %ss" %(time.perf_counter()-myTime))

#Input: ** is used for target car
#Input: any capital alphabet are used for other cars
#Input: space= empty space
#Input: send in 36 character string
