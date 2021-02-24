import sys,random
#x=1,o=-1,draw=0
def game_over(board,token):
    opponent="XO".replace(token,"")
    for ind in range(0,9,3):#checks all rows
        temp=board[ind:ind+3]
        if temp==token*3:
            return 1
        elif temp==opponent*3:
            return -1
    for ind in range(0,3):#checks all cols
        temp=board[ind]+board[ind+3]+board[ind+6]
        if temp == token*3:
            return 1
        elif temp == opponent*3:
            return -1
    temps=[board[0]+board[4]+board[8],board[2]+board[4]+board[6]]#diagonals
    if token*3 in temps:
        return 1
    elif opponent*3 in temps:
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

def max_step(state,token):
    end=game_over(state,token)
    if end is not None:
        return end
    results=[]
    for child in getChildren(state,token):
        results.append(-1*max_step(child,"XO".replace(token,"")))
    return max(results)

def get_player_input(state):
    options=[i for i in range(9) if state[i]=="."]
    print("Your options are %s" %options)
    #nextmove=int(input("Your choice?"))
    nextmove=options[random.randint(len(options))]
    return nextmove

def max_move(state,token):
    maxVal=-2
    maxInd=-1
    for child in getChildren(state,token):
        ind=[state[i]==child[i] for i in range(9)].index(False)
        outcome=-1*max_step(child,"XO".replace(token,""))
        print("Moving at %s results in a %s" %(ind,["lose","tie","win"][outcome+1]))
        if outcome>maxVal:
            maxVal=outcome
            maxInd=ind
    print()
    print("I choose space " + str(maxInd))
    print()
    state=state[:maxInd]+token+state[maxInd+1:]
    print_puzzle(state)
    return state

computer=""
player=""
def compTurn(board):
    end=game_over(board,computer)
    if end is not None:
        return board
    newBoard=max_move(board,computer)
    return playerTurn(newBoard)


def playerTurn(board):
    end = game_over(board,player)
    if end is not None:
        return board
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


if board.count(".")%2==1 and computer=="X":
    board=compTurn(board)
elif board.count(".")%2==1 and player=="X":
    board=playerTurn(board)
elif board.count(".")%2==0 and computer=="O":
    board=compTurn(board)
else:
    board=playerTurn(board)

winner=game_over(board,computer)
if winner==1:
    print("I win!")
elif winner==-1:
    print("You win!")
else:
    print("We tied!")
