import sys; args=sys.argv[1:]
import random

size = args[0].split("x")
hei,wid=int(size[0]),int(size[1])
numblocks = int(args[1])
wordfile = args[2]
seedstrings=[]
if len(args)>3:
    seedstrings=args[3:]

def print_puzzle(board):
    if board is None:
        print("None")
    else:
        for row in range(hei):
            print(" ".join(board[:wid]))
            board=board[wid:]
        print()

def is_connected(board,ind):
    if board[ind]!="-" and not board[ind].isalpha():
        return board
    board=board[:ind]+"5"+board[ind+1:]
    #spread up
    if ind//wid>0:#if row!=0
        board=is_connected(board,ind-wid)
    # spread down
    if ind // wid < hei-1:  # if row!=hei-1
        board = is_connected(board, ind + wid)
    if ind%wid>0:
        board=is_connected(board,ind-1)
    if ind%wid<wid-1:
        board=is_connected(board,ind+1)
    return board

def place_block(board,ind):
    if board[ind].isalpha():
        return None
    board = board[:ind] + "#" + board[ind + 1:]
    row = ind // wid
    col = ind % wid
    # check top
    if row != 0 and board[(row - 1) * wid + col] != "#":
        if row<3: #row=1 or row=2
            board= place_block(board,(row - 1) * wid + col)
            if board is None:
                return None
        else:
            spaces = [board[i] for i in range((row-2)*wid+col,(row-4)*wid+col,-wid)]
            if "#" in spaces:
                board = place_block(board, (row - 1) * wid + col)
                if board is None:
                    return None
    # check bottom
    if row!=hei-1 and board[(row+1)*wid+col] !="#":
        if row>hei-4:
            board = place_block(board, (row + 1) * wid + col)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range((row+2)*wid+col,(row+4)*wid+col,wid)]
            if "#" in spaces:
                board = place_block(board, (row + 1) * wid + col)
                if board is None:
                    return None
    # check left
    if col!=0 and board[row*wid+col-1]!="#":
        if col<3:
            board = place_block(board, row * wid + col-1)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range(row*wid+col-3,row*wid+col-1)]
            if "#" in spaces:
                board = place_block(board, row * wid + col - 1)
                if board is None:
                    return None
    # check right
    if col!=wid-1 and board[row*wid+col+1]!="#":
        if col>wid-4:
            board = place_block(board, row * wid + col+1)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range(row*wid+col+2,row*wid+col+4)]
            if "#" in spaces:
                board = place_block(board, row * wid + col + 1)
                if board is None:
                    return None

    #NOW CHECK FOR OPPOSITE SIDE#
    ind = len(board)-ind-1
    if board[ind].isalpha():
        return None
    board = board[:ind] + "#" + board[ind + 1:]
    row = ind // wid
    col = ind % wid
    # check top
    if row != 0 and board[(row - 1) * wid + col] != "#":
        if row<3: #row=1 or row=2
            board= place_block(board,(row - 1) * wid + col)
            if board is None:
                return None
        else:
            spaces = [board[i] for i in range((row-2)*wid+col,(row-4)*wid+col,-wid)]
            if "#" in spaces:
                board = place_block(board, (row - 1) * wid + col)
                if board is None:
                    return None
    # check bottom
    if row!=hei-1 and board[(row+1)*wid+col] !="#":
        if row>hei-4:
            board = place_block(board, (row + 1) * wid + col)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range((row+2)*wid+col,(row+4)*wid+col,wid)]
            if "#" in spaces:
                board = place_block(board, (row + 1) * wid + col)
                if board is None:
                    return None
    # check left
    if col!=0 and board[row*wid+col-1]!="#":
        if col<3:
            board = place_block(board, row * wid + col-1)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range(row*wid+col-3,row*wid+col-1)]
            if "#" in spaces:
                board = place_block(board, row * wid + col - 1)
                if board is None:
                    return None
    # check right
    if col!=wid-1 and board[row*wid+col+1]!="#":
        if col>wid-4:
            board = place_block(board, row * wid + col+1)
            if board is None:
                return None
        else:
            spaces=[board[i] for i in range(row*wid+col+2,row*wid+col+4)]
            if "#" in spaces:
                board = place_block(board, row * wid + col + 1)
                if board is None:
                    return None
    return board
    #NOW CHECK CONNECTED
    # if "-" not in board:
    #     return board
    # temp= is_connected(board,board.index("-"))
    # if "-" not in temp:
    #     #print_puzzle(temp)
    #     return board
    # return None

def place_words(board,seedstrings):
    board=list(board)
    for code in seedstrings:
        xInd=code.index("x")
        row=int(code[1:xInd])
        colInd=xInd+1
        col=code[colInd]
        if code[colInd+1].isdigit():
            colInd+=1
            col+=code[colInd]
        col=int(col)
        word=code[colInd+1:]
        if code[0]=="H":
            ind=0
            for i in range(row*wid+col,row*wid+col+len(word)):
                board[i]=word[ind].capitalize()
                ind+=1
        else:
            ind=0
            for i in range(row*wid+col,(row+len(word))*wid+col,wid):
                board[i]=word[ind].capitalize()
                ind+=1

    if len(board) % 2 == 1 and numblocks % 2 == 1:
        if board[len(board)//2]=="-":
            board[len(board)//2]="#"
    print_puzzle(board)
    #now make symmetrical
    board="".join(board)
    for i in range(len(board)):
        if board[i]=="#":
            board=place_block(board,i)
    return board


def get_sorted_values(board):
    mylist=[]
    for i in range(len(board)):
        if board[i]=="-":
            mylist.append(i)
    random.shuffle(mylist)
    return mylist

def backtracking(board):
    # check connected
    if "-" in board and "-" in is_connected(board, board.index("-")):
        return None
    #print_puzzle(board)
    if board.count("#")==numblocks:
        return board
    elif board.count("#")>numblocks:
        return None
    #if is_valid(board):
    for ind in get_sorted_values(board):
        temp_board=place_block(board,ind)
        if temp_board is not None:
            temp_board=backtracking(temp_board)
            if temp_board is not None:
                return temp_board
    return None

def backtrackings(boards):
    board=boards[-1]
    # check connected
    if "-" in board and "-" in is_connected(board, board.index("-")):
        return []
    #print_puzzle(board)
    if board.count("#")==numblocks:
        return board
    elif board.count("#")>numblocks:
        return []
    #if is_valid(board):
    for ind in get_sorted_values(board):
        temp_board=place_block(board,ind)
        if len(temp_board)>0:
            temp_board=backtracking(boards+[temp_board])
            if len(temp_board)>0:
                return boards+[temp_board]
    return []

board="-"*hei*wid
board=place_words(board,seedstrings)
#print_puzzle(board)


board=backtracking(board)
#for item in board:
print_puzzle(board)
