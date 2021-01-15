import sys
import random
import time

def print_puzzle(board):
    for i in range(8):
        print(" ".join(list(board[i*8:(i+1)*8])))
    print("Score: " + str(mid_game_score(board)))
    print()

def end_game(board):
    if "." not in board:
        return True
    if possibleMoves(board,"o")+possibleMoves(board,"o")==0:
        return True
    return False
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

def get_children(board,token):
    moves=possibleMoves(board,token)
    states=[]
    for m in moves:
        states.append(move(board,token,m))
    return states

def end_game_score(board):
    score=0
    token="x"
    opponent="o"
    # check corners
    corners=(board[0],board[7],board[56],board[63])
    score=sum([15 if item==token else -15 if item==opponent else 0 for item in corners])
    #check edges
    edges=[1,8,9,6,14,15,48,49,57,54,55,62]
    edge=[board[e] for e in edges]
    score+=2*edge.count("o")
    score-=2*edge.count("x")
    #check mobility
    xmoves=len(possibleMoves(board,token))
    omoves=len(possibleMoves(board,opponent))
    #print("%s  %s" %(lmoves,xmoves))
    if xmoves<2:
        score-=50
    elif xmoves<4:
        score-=35
    if omoves<2:
        score+=50
    elif omoves<4:
        score+=35
    score+=5*(xmoves-omoves)
    #check count of pieces
    score+=3*(board.count(token)-board.count(opponent))
    # check win
    if "." not in board:
        num=board.count(token)
        if num<33:
            score=5000
        elif num>33:
            score+=500
    elif "o" not in board:
        score+=100
    elif "x" not in board:
        score-=100
    return score

def mid_game_score(board):
     token="x"
     opponent="o"
     #corners
     corners = (board[0], board[7], board[56], board[63])
     score=sum([15 if item==token else -15 if item==opponent else 0 for item in corners])
     # check mobility
     xmoves = len(possibleMoves(board, token))
     omoves=len(possibleMoves(board,opponent))
     score+=128/(2**(omoves/2))-128/(2**(xmoves/2))
     # check count of pieces -> more important as there are less spaces open
     score += (board.count(token) - board.count(opponent))*(64-board.count("."))
     # check edges
     edges=[1,8,9,6,14,15,48,49,57,54,55,62]
     edge=[board[e] for e in edges]
     score+=1.5*(edge.count("o")-edge.count("x"))
     # check if game over
     if "." not in board:
         num = board.count(token)
         if num < 33:
             score = 5000 + num
         elif num > 33:
             score += 5000 - num
     return score
#     if board.count(".")<10:
#         return end_game_score(board)
#     score=0
#     token="x"
#     opponent="o"
#     # check corners
#     corners=(board[0],board[7],board[56],board[63])
#     score=sum([15 if item==token else -15 if item==opponent else 0 for item in corners])
#     #check edges
#     edges=[1,8,9,6,14,15,48,49,57,54,55,62]
#     edge=[board[e] for e in edges]
#     score+=1.5*edge.count("o")
#     score-=1.5*edge.count("x")
#     #check mobility
#     xmoves=len(possibleMoves(board,token))
#     omoves=len(possibleMoves(board,opponent))
#     #print("%s  %s" %(lmoves,xmoves))
#     if xmoves < 2:
#         score -= 40
#     elif xmoves < 4:
#         score -= 25
#     if omoves < 2:
#         score += 40
#     elif omoves < 4:
#         score += 25
#     score+=40*(xmoves-omoves)
#     #check count of pieces
#     score += .3*(board.count(token) - board.count(opponent))
#     return score

def max_step(state,depth,alpha,beta):
    #print_puzzle(state)
    if depth==0:
        return mid_game_score(state)
    results=[]
    for child in get_children(state,"o"):
        result=min_step(child,depth-1,alpha,beta)
        if result>=beta:
            return result
        if result > alpha:
            alpha = result
        results.append(result)
        # check if game is over
    if len(results) == 0:
        return mid_game_score(state)
    if max(results)<alpha:
        return max(results)
    return alpha

def min_step(state,depth,alpha,beta):
    #print_puzzle(state)
    if depth==0:
        return mid_game_score(state)
    results = []
    for child in get_children(state, "x"):
        result=max_step(child,depth-1,alpha,beta)
        if alpha>=result:
            return result
        if result < beta:
            beta=result
        results.append(result)
    #check if game is over
    if len(results)==0:
        return mid_game_score(state)
    if min(results)>beta:
        return min(results)
    return beta

def max_move(board,depth):
    max_num=-10000
    max_ind=-1
    for ind in possibleMoves(board,"x"):
        num=max_step(move(board,"x",ind),depth,-10000,10000)
        if num>max_num:
            max_num=num
            max_ind=ind
    return max_ind

def min_move(board,depth):
    min_num=10000
    min_ind=-1
    for ind in possibleMoves(board,"o"):
        num=min_step(move(board,"o",ind),depth,-10000,10000)
        if num<min_num:
            min_num=num
            min_ind=ind
    return min_ind

def find_next_move(board, player, depth):
   # Based on whether player is x or o, start an appropriate version of minimax
   # that is depth-limited to "depth".  Return the best available move.
   if player=="x":
       return max_move(board,depth)#max_step(board,depth,-100000,100000)
   else:
       return min_move(board,depth)#min_step(board,depth,-100000,100000)
# All your other functions


def play_game():
    board="...........................ox......xo............................"
    token="x"
    opponent="o"
    depth = 3
    while not end_game(board):
        print("X's: %s   O's: %s" % (board.count("x"), board.count("o")))
        print_puzzle(board)
        m=find_next_move(board,token,depth)
        board=move(board,token,m)

        print("X's: %s   O's: %s" % (board.count("x"), board.count("o")))
        print_puzzle(board)
        moves=possibleMoves(board,opponent)
        board=move(board,opponent,random.choice(moves))

class Strategy():
   logging = True  # Optional
   def best_strategy(self, board, player, best_move, still_running):
       depth = 1
       while True:
           best_move.value = find_next_move(board, player, depth)
           depth += 1

#play_game()

# board=""
# board+=".x.ooo.."
# board+="..xoo..."
# board+="..oxoo.."
# board+="xxxxxo.."
# board+="..xx..o."
# board+="....x..."
# board+="........"
# board+="........"
#
# token="o"
# print_puzzle(board)
#
# for m in possibleMoves(board,token):
#     new_board=move(board,token,m)
#     print_puzzle(new_board)