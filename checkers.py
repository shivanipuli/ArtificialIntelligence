board=" o o o oo o o o  o o o o"
board+="                "
board+="x x x x  x x x xx x x x "

def print_puzzle(board):
    for i in range(8):
        print(" ".join(list(board[i*8:(i+1)*8])))
    print()

def move(board,index):
    board_states=[]
    token=board[index]
    if token!="o": #x,X,O
        #check diagleftup
        #check diag rightup
    if token!="x": #o,X,O
        # check diagleftdown
        # check diag rightdown


print_puzzle(board)