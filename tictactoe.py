import sys,random
#x=1,o=-1,draw=0
def game_over(board):
    for ind in range(0,9,3):#checks all rows
        temp=board[ind:ind+3]
        if temp=="XXX":
            return 1
        elif temp=="OOO":
            return -1
    for ind in range(0,3):#checks all cols
        temp=board[ind]+board[ind+3]+board[ind+6]
        if temp == "XXX":
            return 1
        elif temp == "OOO":
            return -1
    temps=[board[0]+board[4]+board[8],board[2]+board[4]+board[6]]#diagonals
    if "XXX" in temps:
        return 1
    elif "OOO" in temps:
        return -1
    if "." not in board: #if board is full
        return 0
    return None

def getChildren(state,symbol):
    children=set()
    for i in range(9):
        if state[i]==".":
            children.add(state[:i]+symbol+state[i+1:])
    return children

def print_puzzle(state):
    print("Current Board: ")
    print(state[0:3]+"    012")
    print(state[3:6]+"    345")
    print(state[6:9]+"    678")
    print()

#<------part 2------->
outputs={}

def max_step(state):
    end=game_over(state)
    if end is not None:
        return end
    results=[]
    for child in getChildren(state,"X"):
        results.append(min_step(child))
    return max(results)

def min_step(state):
    end = game_over(state)
    if end is not None:
        return end
    results = []
    for child in getChildren(state, "O"):
        results.append(max_step(child))
    return min(results)

def get_player_input(state):
    options=[i for i in range(9) if state[i]=="."]
    print("Your options are %s" %options)
    #nextmove=int(input("Your choice?"))
    nextmove=options[random.randint(len(options))]
    return nextmove

def max_move(state):
    maxVal=-2
    maxInd=-1
    for child in getChildren(state,"X"):
        ind=[state[i]==child[i] for i in range(9)].index(False)
        outcome=min_step(child)
        print("Moving at %s results in a %s" %(ind,["lose","tie","win"][outcome+1]))
        if outcome>maxVal:
            maxVal=outcome
            maxInd=ind
    print()
    print("I choose space " + str(maxInd))
    print()
    state=state[:maxInd]+"X"+state[maxInd+1:]
    print_puzzle(state)
    return state


def min_move(state):
    minVal=2
    minInd=-1
    for child in getChildren(state,"O"):
        ind = [state[i] == child[i] for i in range(9)].index(False)
        outcome = max_step(child)
        print("Moving at %s results in a %s" % (ind, ["win", "tie", "lose"][outcome + 1]))
        if outcome<minVal:
            minVal=outcome
            minInd=ind
    print()
    print("I choose space " + str(minInd))
    print()
    state=state[:minInd]+"O"+state[minInd+1:]
    print_puzzle(state)
    return state

computer=""
player=""
def compTurn(board):
    end=game_over(board)
    if end is not None:
        return board,end
    newBoard=""
    if computer=="X":
        newBoard=max_move(board)
    else:
        newBoard = min_move(board)
    return playerTurn(newBoard)


def playerTurn(board):
    end = game_over(board)
    if end is not None:
        return board,end
    myList=[ind for ind in range(9) if board[ind]=="."]
    print("You can move to any of these spaces: %s." %myList)
    ind=int(input("Your choice? "))
    board=board[:ind]+player+board[ind+1:]
    print_puzzle(board)
    return compTurn(board)

board=sys.argv[1]
print_puzzle(board)

if board==".........":
    computer=input("Should I be X or O? ")
    player="OX".replace(computer,"")
else:
    computer="OX"[board.count(".")%2]
    player = "OX".replace(computer, "")

winner=""
if board.count(".")%2==1 and computer=="X":
    board,winner=compTurn(board)
elif board.count(".")%2==1 and player=="X":
    board,winner=playerTurn(board)
elif board.count(".")%2==0 and computer=="O":
    board,winner=compTurn(board)
else:
    board,winner=playerTurn(board)


if "O X"[winner+1]==computer:
    print("I win!")
elif "O X"[winner+1]==player:
    print("You win!")
else:
    print("We tied!")

#<-----part 1------->
# finalBoards=set()
# def allPossibles(state,symbol):
#     if game_over(state) is not None:
#         finalBoards.add(state)
#         return 1
#     symbol="xo".replace(symbol,"")
#     sum=0
#     for child in getChildren(state,symbol):
#         sum+=allPossibles(child,symbol)
#     return sum
#
# totalGames=allPossibles("."*9,"x")
# print("Total final boards: " + str(len(finalBoards)))
# print("Total games: " + str(totalGames))
#
# endResults={5:0,6:0,7:0,8:0,9:0,10:0}
# for board in finalBoards:
#     if game_over(board)==0:
#         endResults[10]+=1
#     elif "." not in board:
#         endResults[9]+=1
#     else:
#         moves=9-board.count(".")
#         endResults[moves]+=1
# print("Winner: "+ str(endResults))