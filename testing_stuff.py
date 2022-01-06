"""A module for testing functions in a sandbox."""

import copy


ships = {"Aircraft Carrier": 5,
         "Battleship": 4,
         "Submarine": 3,
         "Destroyer": 3,
         "Patrol Boat": 2}

board = []
for i in range(10):
    board_row = []
    for j in range(10):
        board_row.append(-1)
    board.append(board_row)

player1_board = copy.deepcopy(board), "player1"
player2_board = copy.deepcopy(board), "player2"

print(ships)
print(player1_board)
print(player2_board)


def print_board(board):
    for i in board[0]:
        print(i)
    print(board[1])

print_board(player1_board)
print_board(player2_board)