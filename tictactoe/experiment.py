# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:16:41 2020

@author: jyotm
"""
import copy
from tictactoe import *

board = initial_state()
for i in range(3):
    for j in range(3):
        board[i][j] = EMPTY
board[0][1] = X
board[1][0] = O
board[2][1] = X
board[2][0] = X
board[0][0] = O
board[1][1] = O
#board[0][2] = X
#board[2][0] = X
#board[1][2] = X


#ka = copy.deepcopy(board)
#ka2 = list(zip(*ka))
#print(list(ka2[1]) == [X,X,X])
#acts = actions(ka)
#act = list(acts)[0]
            
print(player(board))
#print(terminal(board))
#res = result(board, act)

print(minimax(board))