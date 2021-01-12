import sys

def print_puzzle(board):
    for i in range(8):
        print(" ".join(list(board[i*8:(i+1)*8])))
    print()

def is_valid(board,token,ind):
    opp="xo".replace(token,"")
    #jump from right
    if ind%8<6 and board[ind+1]==opp:
        for i in range(ind+1,(ind//8+1)*8):
            if board[i]==token:
                return True
            elif board[i]==".":
                break

    #jump from left
    if ind%8>1 and board[ind-1]==opp:
        for i in range(ind-1,ind-ind%8-1,-1):
            if token==board[i]:
                return True
            elif board[i]==".":
                break
    #jump down
    if ind // 8 < 6 and board[ind + 8] == opp:
        for i in range(ind + 8, 64, 8):
            if board[i] == token:
                return True
            elif board[i] == ".":
                break
    #jump up
    if ind//8>1 and board[ind-8]==opp:
        for i in range(ind-8, -1, -8):
            if board[i]==token:
                return True
            elif board[i]==".":
                break
    #from diagtopleft
    if ind//8>1 and ind%8>1 and board[ind-9]==opp:
        for i in range(ind-9,-1,-9):
            if board[i]==token:
                return True
            if i%8==0 or i//8==0 or board[i]==".":
                break
    #check diagbotright
    if ind//8<6 and ind%8<6 and board[ind+9]==opp:
        for i in range(ind+9,64,9):
            if board[i]==token:
                return True
            if i%8==7 or i//8==7 or board[i]==".":
                break
    #check diagtopright
    if ind//8>1 and ind%8<6 and board[ind-7]==opp:
        for i in range(ind-7,-1,-7):
            if board[i]==token:
                return True
            if i//8==0 or i%8==7 or board[i]==".":
                break
    #check diagbotleft
    if ind//8<6 and ind%8>1 and board[ind+7]==opp:
        for i in range(ind+7,64,7):
            if board[i]==token:
                return True
            if i//8==7 or i%8==0 or board[i]==".":
                break
    return False

def possibleMoves(board,token):
    moves=[]
    for ind in range(64):
        if board[ind]=="." and is_valid(board,token,ind):
            moves.append(ind)
    return moves

def move(board,token,ind):
    newBoard=list(board)
    opp = "xo".replace(token, "")
    # jump from right
    if ind%8<6 and board[ind+1]==opp:
        for i in range(ind+1,(ind//8+1)*8):
            if board[i]==token:
                for i in range(ind+1, (ind // 8 + 1) * 8):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
            elif board[i]==".":
                break
    # jump from left
    if ind%8>1 and board[ind-1]==opp:
        for i in range(ind-1,ind-ind%8-1,-1):
            if token==board[i]:
                for i in range(ind-1, ind - ind % 8-1, -1):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
            elif board[i]==".":
                break

    # jump down
    if ind // 8 < 6 and board[ind + 8] == opp:
        for i in range(ind + 8, 64, 8):
            if board[i] == token:
                for i in range(ind+8, 64, 8):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
            elif board[i] == ".":
                break

    # jump up
    if ind//8>1 and board[ind-8]==opp:
        for i in range(ind-8, -1, -8):
            if board[i]==token:
                for i in range(ind, -1, -8):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
            elif board[i]==".":
                break
    # from diagtopleft
    if ind // 8 > 1 and ind % 8 > 1 and board[ind - 9] == opp:
        for i in range(ind-9, -1, -9):
            if board[i] == token:
                for i in range(ind-9, -1, -9):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
                break
            if i % 8 == 0 or i // 8 == 0 or board[i]==".":
                break
    # check diagbotright
    if ind // 8 < 6 and ind % 8 < 6 and board[ind + 9] == opp:
        for i in range(ind+9, 64, 9):
            if board[i] == token:
                for i in range(ind+9, 64, 9):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
                break
            if i % 8 == 7 or i // 8 == 7 or board[i]==".":
                break
    # check diagtopright
    if ind // 8 > 1 and ind % 8 < 6 and board[ind - 7] == opp:
        for i in range(ind-7, -1, -7):
            if board[i] == token:
                for i in range(ind-7, -1, -7):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
                break
            if i // 8 == 0 or i % 8 == 7 or board[i]==".":
                break
    # check diagbotleft
    if ind // 8 < 6 and ind % 8 > 1 and board[ind + 7] == opp:
        for i in range(ind+7, 64, 7):
            if board[i] == token:
                for i in range(ind+7,64,7):
                    if board[i] == token:
                        break
                    if board[i] == opp:
                        newBoard[i] = token
                break
            if i // 8 == 7 or i % 8 == 0 or board[i]==".":
                break
    newBoard[ind]=token
    return "".join(newBoard)

def max_step(state):
    end=game_over(state)
    if end is not None:
        return end
    results=[]
    for child in possibleMoves(state,"x"):
        results.append(min_step(child))
    return max(results)

def min_step(state):
    end = game_over(state)
    if end is not None:
        return end
    results = []
    for child in possibleMoves(state, "o"):
        results.append(max_step(child))
    return min(results)

def max_move(state):
    maxVal=-2
    maxInd=-1
    for child in possibleMoves(state,"x"):
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
    for child in possibleMoves(state,"o"):
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


# board="...........o.......o.......oo....ooooo...xx.x..................."
# board="....o......o....o.oox....oxoxx....ooo.....xo...................."

# token="x"
board,token=sys.argv[1],sys.argv[2]
#print_puzzle(board)
validMoves=possibleMoves(board,token)
print(validMoves)
#print(board)
for m in validMoves:
    print(move(board,token,m))