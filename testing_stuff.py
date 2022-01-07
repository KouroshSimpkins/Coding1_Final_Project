"""A module for testing functions in a sandbox."""

import copy
import os


BOARD_SIZE = 10
SHIPS = {"Aircraft Carrier": 5,
         "Battleship": 4,
         "Submarine": 3,
         "Destroyer": 3,
         "Patrol Boat": 2}


def cls():
    """Improves readability of Text interfaces by clearing the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def setup_board():
    """Setup an empty board."""

    board = []

    for i in range(BOARD_SIZE): #pylint: disable=unused-variable
        board_row = []
        for j in range(BOARD_SIZE): #pylint: disable=unused-variable
            board_row.append(-1)
        board.append(board_row)

    return board


def print_board(board):
    """Board is an array with 2 positions,
    the first contains the 10*10 board, the second stores the reference to the player."""

    player_num = board[1]
    board = board[0]

    # print horizontal numbers
    print()
    print(player_num + "'s board:")
    print()
    print("   ", end="")
    for i in range(1, BOARD_SIZE + 1):
        print(" " + str(i) + " ", end="")
    print()

    # print board
    for i in range(BOARD_SIZE):

        if i != BOARD_SIZE - 1:
            print(str(i + 1) + "  ", end="")
        else:
            print(str(i + 1) + " ", end="")


        for j in range(BOARD_SIZE):
            if board[i][j] == -1:
                print("[ ]", end="")
            elif board[i][j] == "*":
                print("*", end="")
            elif board[i][j] == "$":
                print("$", end="")

        print()


def player_turns(board):
    """This function aims to show the players board
    and where they have fired on their opponent's board."""




def main():
    """Main function."""

    player1_board = setup_board(), "player1"
    player2_board = setup_board(), "player2"

    # Create targeting boards
    player1_target = copy.deepcopy(player2_board)
    player2_target = copy.deepcopy(player1_board)
    # Add flags to the target boards, to identify them later
    player1_target.append("p2_target")
    player2_target.append("p1_target")


if __name__ == "__main__":
    main()
