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
    if ind // wid < hei-1:  # if row!=0
        board = is_connected(board, ind + wid)
    if ind>0:
        board=is_connected(board,ind-1)
    if ind<len(board)-1:
        board=is_connected(board,ind+1)
    return board

def is_valid(board,ind):
    if board[ind]!="-":
        return None
    row = ind // wid
    col = ind % wid
    # check top
    if row != 0 and board[(row - 1) * wid + col] != "#":
        if row<3: #row=1 or row=2
            return False
        spaces = [board[i] for i in range((row-2)*wid+col,(row-4)*wid+col,-wid)]
        if "#" in spaces:
            return False
    # check bottom
    if row!=hei-1 and board[(row+1)*wid+col] !="#":
        if row>hei-4:
            return False
        spaces=[board[i] for i in range((row+2)*wid+col,(row+4)*wid+col,wid)]
        if "#" in spaces:
            return False
    # check left
    if col!=0 and board[row*wid+col-1]!="#":
        if col<3:
            return False
        spaces=[board[i] for i in range(row*wid+col-3,row*wid+col-1)]
        if "#" in spaces:
            return False
    # check right
    if col!=wid-1 and board[row*wid+col+1]!="#":
        if col>wid-4:
            return False
        spaces=[board[i] for i in range(row*wid+col+2,row*wid+col+4)]
        if "#" in spaces:
            return False
    return True

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
                board[i]=word[ind]
                ind+=1
            # if col>0 and numblocks>0:
            #     board[row*wid+col-1]="#"
            #     board[-row*wid-col]="#"
            #     numblocks-=2
            # if col+len(word)<wid and numblocks>0:
            #     board[row * wid + col +len(word)] = "#"
            #     board[-row * wid - col - 1-len(word)] = "#"
            #     numblocks -= 2
        else:
            ind=0
            for i in range(row*wid+col,(row+len(word))*wid+col,wid):
                board[i]=word[ind]
                ind+=1
                # if row>0 and numblocks>0:
                #     board[(row-1)*wid+col]="#"
                #     board[(1-row)*wid-col-1]="#"
                #     numblocks-=2
                # if row+len(word)<hei and numblocks>0:
                #     board[(row+len(word))*wid+col]="#"
                #     board[(row+len(word))*-wid-col-1]="#"
                #     numblocks-=2
    if len(board) % 2 == 1 and numblocks % 2 == 1:
        if board[len(board)//2]=="-":
            board[len(board)//2]="#"
    return "".join(board)


def place_blocks(board,numblocks):
    board=list(board)
    if len(board) % 2 == 1 and numblocks % 2 == 1:
        board[len(board)//2]="#"
        numblocks-=1
    #if len(seedstrings)>0:
    #    board=lace_around_words(board,)
    while numblocks>0:
        ind=random.randint(0,len(board)//2)
        if board[ind]=="-" and board[-ind-1]=="-":
            board[ind] = "#"
            board[-ind-1] = "#"
            numblocks-=2
        ind+=1
    return "".join(board)

def conflict(board,ind):
    row=ind//wid
    col=ind%wid
    count=0
    #check top
    if row==0:
        count+=0
    elif 0<row<3:
        if board[(row-1)*wid+col]!="#":
            count+=1

    spaces=[board[i] for i in range(ind-wid)]
    if row>0 and board[(row-1)*wid+col]!="#":
        i=2
        while i<4:
            if row+1<i:
                count+=1
    #check bottom
    #check left
    #check right
    return count

def collisions(board):
    conflicts=[]
    for i in range(len(board)):
        if board[i]=="#":
            conflicts.append(conflict(board,i)+1)
        elif board[i]=="-":
            conflicts.append(-conflict(board,i)-1)
        else:
            conflicts.append(0)
    return conflicts


def find_options(board,ind,numblocks):
    options=set()
    if ind==-1:
        if len(board) % 2 == 1 and numblocks % 2 == 1:
            board.append(len(board)//2)

        if wid==7:
            options.append(3)
    return options

def get_sorted_values(board):
    mylist=[]
    for i in range(len(board)):
        if board[i]=="-":
            mylist.append(i)
    random.shuffle(mylist)
    return mylist

def backtracking(board):
    #print_puzzle(board)
    if board.count("#")==numblocks:
        return board
    elif board.count("#")>numblocks:
        return None
    #check connected
    if "-" in board and "-" in is_connected(board,board.index("-")):
        return None
    #if is_valid(board):
    for ind in get_sorted_values(board):
        temp_board=place_block(board,ind)
        if temp_board is not None:
            temp_board=backtracking(temp_board)
            if temp_board is not None:
                return temp_board
    return None




board="-"*hei*wid
board=place_words(board,seedstrings)
print_puzzle(board)


board=backtracking(board)
if board is not None:
    print_puzzle(board)
else:
    print(board)
