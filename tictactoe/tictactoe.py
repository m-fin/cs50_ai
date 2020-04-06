"""
Tic Tac Toe Player
"""

import math
import numpy as np
from copy import deepcopy

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
    num_x = 0
    num_o = 0

    for row in board:
        for elem in row:
            if elem == X:
                num_x += 1
            elif elem == O:
                num_o += 1

    if num_x == num_o:
        return X
    else:
        return O

def not_player(board):
    """
    Returns player who doesn't have the next turn on a board.
    """
    if player(board) == X:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # if action not in actions(board):
    #     raise Exception('yeet')

    potential_board = deepcopy(board)
    potential_board[action[0]][action[1]] = player(potential_board)

    return potential_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    players = [X, O]

    for player in players:
        # check rows
        for row in board:
            if row == [player, player, player]:
                return player

        # check cols
        for col in np.transpose(board).tolist():
            if col == [player, player, player]:
                return player

        # check diag
        if list(np.diagonal(board)) == [player, player, player]:
            return player

        # check reverse diag
        if list(np.flipud(board).diagonal()) == [player, player, player]:
            return player

    return None


def full(board):
    for row in board:
        for elem in row:
            if elem == None:
                return False

    return True


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or full(board):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # only called on terminal board (full board)

    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the board is a terminal board, the minimax function should return None.
    if board == terminal(board):
        return None

    # The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    # If multiple moves are equally optimal, any of those moves is acceptable.

    is_maximizing = False
    depth = 0
    best_score = float('inf')
    best_move = None

    for elem in actions(board):
        potential_board = result(board, elem)
        score = minimax_alg(potential_board, is_maximizing, depth + 1)

        # ai is trying to get loweset score b/c O is -1
        if score < best_score:
            best_score = score
            best_move = elem

    return best_move
    
def minimax_alg(potential_board, is_maximizing, depth):
    if terminal(potential_board):
        return utility(potential_board)

    if is_maximizing:
        best_score = float('-inf')

        for elem in actions(potential_board):
            next_potential_board = result(potential_board, elem)
            score = minimax_alg(next_potential_board, False, depth + 1)

            best_score = max(score, best_score)

        return best_score

    else:
        best_score = float('inf')

        for elem in actions(potential_board):
            next_potential_board = result(potential_board, elem)
            score = minimax_alg(next_potential_board, True, depth + 1)

            best_score = min(score, best_score)

        return best_score