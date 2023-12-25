import os
import numpy

board=numpy.array([['_','_','_'],['_','_','_'],['_','_','_']])
p1s='X'
p2s='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print('------------------------',symbol,' Won------------------------')
            return True
    return False
def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
               count=count+1
        if count==3:
            print('------------------------',symbol,' Won------------------------\n')
            return True
    return False
def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and (board[1][1]==symbol):
        print('------------------------',symbol,' Won------------------------')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and (board[1][1]==symbol):
        print('------------------------',symbol,' Won------------------------\n')
        return True
    return False

        
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)


def place(symbol):
    print(numpy.matrix(board))
    while(True):

        row=int(input('Enter row- 1 or 2 or 3 :'))
        col=int(input('Enter col- 1 or 2 or 3 :'))
        os.system('cls')


        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='_':
            #print(board[row-1][col-1])
            break
        else:
            print('Invalid Input. Please enter again!!')       
    board[row-1][col-1]=symbol
k=False
r=False
def play():
    for turn in range(9):
        if turn%2 == 0:
            print('------------------------',p1s,' Turn------------------------\n')
            place(p1s)
            k=won(p1s)
            if k:
                break
            
        else:
            print('------------------------',p2s,' Turn------------------------\n')
            place(p2s)
            r=won(p2s)
            if r:
                break
    print(board)
    
    if not(k) and not(r):
        print('------------------------Draw------------------------\n')
    
os.system('cls')
play()
