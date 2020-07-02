"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    for row in board:
        for element in row:
            value = element
            if value == X and not EMPTY:
                numX+=1
            elif value == O and not EMPTY:
                numO+=1
    if numX == 0 and numO == 0:
        return X
    if numX == numO:
        return X
    elif numO < numX:
        return O
     
           
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                available.add((i,j))
    return available

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board2 = copy.deepcopy(board)
    
    acts = actions(board2)
    if action not in acts:
        raise IOError('invalid action')

    board2[action[0]][action[1]] = player(board)
    return board2

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        
        
        
    ka = copy.deepcopy(board)
    ka = list(zip(*ka))
    maxX = 0
    maxO = 0
    diagX = 0
    diagO = 0
    for i in range(3):
        row = board[i]
        if row == [X,X,X]:
            return X
        elif row == [O,O,O]:
            return O
        elif list(ka[i]) == [X,X,X]:
            return X
        elif list(ka[i]) == [O,O,O]:
            return O
        if board[i][i] == X:
            maxX+=1
        elif board[i][i] == O:
            maxO+=1
        if board[2-i][i] == X:
            diagX+=1
        elif board[2-i][i] == O:
            diagO+=1       
    if maxX == 3:
        return X
    elif maxO == 3:
        return O
    if diagX == 3:
        return X
    elif diagO == 3:
        return O
    else:
        return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) or len(actions(board)) == 0:
        return True
    else:
        return False
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    return None   
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
   
    def MAX_VALUE(state):
        if terminal(state):
            return utility(state)
        v = -10000
        for action in actions(state):
            minval =  MIN_VALUE(result(state, action))
           # print(v , " and ", minval, " at action", action)
            v = max(v,minval)
            #print(v , " and ", minval, " at action after max", action)
        return v
    def MIN_VALUE(state):
        if terminal(state):
            return utility(state)
        v2 = 10000
        for action in actions(state):
            #print(action, "from min")
            maxval = MAX_VALUE(result(state, action))
            v2 = min(v2, maxval)
            #print(v2, maxval, "it is from min")
        return v2

    if player(board) == X:
        maxv = MAX_VALUE(board)
        for act in actions(board):
            val = MIN_VALUE(result(board, act))
            #print(val, maxv)
            if maxv == val:
                return act
        
    else:
        minv = MIN_VALUE(board)
        for act in actions(board):
            if minv == MAX_VALUE(result(board, act)):
                return act
    
    raise NotImplementedError
