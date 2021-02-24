#Turnt Base games
import sys
import random
import time
#Knight (K), Bishop (B), Pawn (P), King (+), Queen (Q), Rook (R)

def print_puzzle(board):
    for i in range(8):
        print(" ".join(list(board[i*8:(i+1)*8])))
    print()



def move_knight(board, ind):
    indexes=[]
    #move