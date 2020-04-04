"""
Tic Tac Toe Player
"""

import math
import numpy as np

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

    potential_board = board
    potential_board[action[0]][action[1]] = player(potential_board)

    return potential_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winner = None
    players = [X, O]

    for player in players:
        # check rows
        for row in board:
            if row == [player, player, player]:
                winner = player

        # check cols
        for col in board.T:



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
