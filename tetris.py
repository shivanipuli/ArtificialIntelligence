import sys

board="".join(sys.argv[1:])#200 char string
#board = "          #         #         #      #  #      #  #      #  #     ##  #     ##  #     ## ##     ## #####  ########  ######### ######### ######### ######### ########## #### # # # # ##### ###   ########"
outcomes=[]
pieces={"I":["####5","#5#5#5#5"],"O":["##5##5"],"T":["###5 # 5","# 5##5# 5"," # 5###5"," #5##5 #5"],"S":["## 5 ##5"," #5##5# 5"],"Z":[" ##5## 5","# 5##5 #5"],"J":["###5#  5","# 5# 5##5","  #5###5","##5 #5 #5"],"L":["###5  #5","##5# 5# 5","#  5###5"," #5 #5##5"]}

def print_board(board):
    if board=="GAME OVER":
        print("GAME OVER")
    else:
        print("=======================")
        for count in range(20):
            print(' '.join(list(("|" + board[count * 10: (count + 1) * 10] + "|"))), count)
        print("=======================")
        #print()
        print("  0 1 2 3 4 5 6 7 8 9  ")
        print()

def find_last_row(board,block,col):
    last_row=None
    for row in range(20):
        if last_row is None:
            for c in range(block.index("5")):
                if board[row*10+col+c]=="#" and block[c]=="#":
                    last_row=row-1
    return 19

def eliminate_rows(board):
    for i in range(20):
        if board[i*10:i*10+10]=="#"*10:
            board=(" "*10)+board[:i*10]+board[i*10+10:]
    return board

def place_block_on_row(board,block,col,last_row):
    if col+block.index("5")>10: #if it goes over the edge
        return "GAME OVER"
    #last_row=find_last_row(board,block,col)
    ind=last_row*10+col
    for l in block:
        if last_row<0:
            return "GAME OVER"
        if l=="5": #next row
            last_row-=1
            ind=last_row*10+col
        elif board[ind]=="#" and l=="#": #only case with clashing
            return "GAME OVER"
        else:
            if l=="#":
                board=board[:ind]+"#"+board[ind+1:] #or "R"
            #print_board(board)
            ind+=1
    return eliminate_rows(board)

def place_block(board,block,col):
    possible=True
    best_board="GAME OVER"
    for row in range(block.count("5")-1,20):
        b=place_block_on_row(board,block,col,row)
        if b=="GAME OVER":
            return best_board
        else:
            best_board=b
    return best_board


#print_board(board)
#print_board(place_block(board,pieces["T"][1],5))
f=open("tetrisout.txt","x")
for piece in pieces:
    for orientation in pieces[piece]:
        for col in range(11-orientation.index("5")):
            outcome=place_block(board,orientation,col)
            print_board(outcome)
            outcomes.append(outcome)
            f.write(outcome)
            f.write("\n")
f.close()
# print_board(board)


#Countermeasures in tetris board: how high up the tetris # gets on board