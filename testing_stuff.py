"""A module for testing functions in a sandbox."""

import copy
import os

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
BOARD_SIZE = 10
SHIPS = {"Aircraft Carrier": 5, # A
         "Battleship": 4, # B
         "Submarine": 3, # S
         "Destroyer": 3, # D
         "Patrol Boat": 2} # P


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

    targetting_board = False
    player_num = board[1]
    if "targetting" in player_num:
        targetting_board = True
    board = board[0]

    # print horizontal numbers
    print()
    print(player_num + "'s board:")
    print()
    print("  ", end="")
    for i in range(1, BOARD_SIZE + 1):
        print(" " + str(i) + " ", end="")
    print()

    # print board
    for i in range(BOARD_SIZE):

        print(str(LETTERS[i]) + " ", end="")

        for j in range(BOARD_SIZE):
            if board[i][j] == -1:
                print("[ ]", end="")
            elif board[i][j] == "*":
                print("[*]", end="")
            elif board[i][j] != -1 and targetting_board:
                print("[$]", end="")
            elif board[i][j] == "$":
                print("[$]", end="")
            else:
                print("[" + board[i][j].strip() + "]", end="")

        print()


def place_ships(board,ships):
    """A function for placing the ships onto the board.
    Takes 2 arguments, the board array and the ships dictionary."""

    temp_board = board[0]

    # the coordinates of the ship should be the "front" of the ship
    # so we need to know the orientation of the ship

    for ship in ships:
        ship_length = ships[ship]
        print("Place " + ship)
        print("Enter the coordinates for the " + ship)
        print("(ex: A1, B2, etc)")
        print("Enter the orientation of the ship (v or h)")
        print()

        # Get ship location and orientation
        while True:
            coords = input("Enter coordinates: ")
            orientation = input("Enter orientation: ")

            x = ord(coords[0]) - 65
            y = int(coords[1]) - 1
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Invalid coordinates.")
            elif orientation not in ('v', 'h'):
                print("Invalid orientation.")
            elif x + ship_length > 10 or y + ship_length > 10:
                print("Ship is too long.")
            elif temp_board[x][y] != -1:
                print("That spot is already taken.")
            else:
                break

        # Place the ship
        if orientation == 'h':
            for i in range(ship_length):
                temp_board[x][y + i] = ship[0]
        else:
            for i in range(ship_length):
                temp_board[x + i][y] = ship[0]

        board[0] = temp_board

        print_board(board)



def main():
    """Main function."""

    # This entire section of code is absolutely hacky.
    # I dislike it, however it works.

    player1_board = []
    player1_board.append(setup_board())
    player1_board.append("Player 1")

    player2_board = []
    player2_board.append(setup_board())
    player2_board.append("Player 2")

    # Create targeting boards
    player1_target = copy.deepcopy(player2_board)
    player2_target = copy.deepcopy(player1_board)

    player1_target[1] = "targetting player 2"
    player2_target[1] = "targetting player 1"

    # The absolutely atrocious board setup above.
    # It has created 4 identical boards, two for each player.
    # A targetting board and a regular board.

    print_board(player1_board)
    place_ships(player1_board, SHIPS)
    print_board(player1_board)

if __name__ == "__main__":
    main()
