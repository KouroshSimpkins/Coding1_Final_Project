"""A module for testing functions in a sandbox."""

import copy


ships = {"Aircraft Carrier": 5,
         "Battleship": 4,
         "Submarine": 3,
         "Destroyer": 3,
         "Patrol Boat": 2}

board = []


def setup_board():
    for i in range(10):
        board_row = []
        for j in range(10):
            board_row.append(-1)
        board.append(board_row)

    return board

player1_board = setup_board(), "player1"
player2_board = setup_board(), "player2"

def print_board(board):
    """Board is a 3 dimensional array"""

    # print horizontal numbers
    print("   ", end="")
    for i in range(1, 11):
        print(" " + str(i) + " ", end="")
    print()

    # print board
    for i in range(10):

        if i != 9:
            print(str(i + 1) + "  ", end=" ")
        else:
            print(str(i + 1) + " ", end=" ")


        for j in range(10):
            print(board[0][i][j], end=" ")
        print()

print_board(player1_board)
