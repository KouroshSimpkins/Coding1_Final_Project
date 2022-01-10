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

    cls()

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
    for i in range(0, 10):
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

        # Get ship location and orientation
        valid = True
        while valid:
            print()
            overlap = False
            coords = input("Enter coordinates: ")
            orientation = input("Enter orientation: ")

            x = ord(coords[0]) - 65
            y = int(coords[1])
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Invalid coordinates.")
            elif orientation not in ('v', 'h'):
                print("Invalid orientation.")
            elif orientation == "v" and x + ship_length > 10:
                print("ship is too long.")
            elif orientation == "h" and y + ship_length > 10:
                print("Ship is too long.")
            else:
                if orientation == "v":
                    for i in range(ship_length):
                        if temp_board[x + i][y] != -1:
                            print("Ship overlaps.")
                            overlap = True
                elif orientation == "h":
                    for i in range(ship_length):
                        if temp_board[x][y + i] != -1:
                            print("Ship overlaps.")
                            overlap = True
                if not overlap:
                    valid = False


        # Place the ship
        if orientation == 'h':
            for i in range(ship_length):
                temp_board[x][y + i] = ship[0]
        else:
            for i in range(ship_length):
                temp_board[x + i][y] = ship[0]

        board[0] = temp_board

        print_board(board)


def make_move(board):
    """A function for making a move on the board.
    Takes 1 argument, the board array."""

    temp_board = board[0]

    valid = False
    while not valid:
        coords = input("Enter coordinates: ")
        x = ord(coords[0]) - 65
        y = int(coords[1])
        if x < 0 or x > 9 or y < 0 or y > 9:
            print("Invalid coordinates.")
        elif temp_board[x][y] == -1:
            print("miss")
            temp_board[x][y] = "*"
            valid = True
        elif temp_board[x][y] == "*" or temp_board[x][y] == "$":
            # This is technically invalid, so valid remains False
            print("already shot")
        else:
            print("hit")
            temp_board[x][y] = "$"
            valid = True

    board[0] = temp_board
    print_board(board)


def check_sunk(board, ships):
    """A function for checking if a ship has been sunk.
    Takes 2 arguments, the board array and the ships dictionary."""

    temp_board = board[0]

    for ship in ships:
        ship_length = ships[ship]
        if ship[0] in temp_board:
            for i in range(ship_length):
                if temp_board[ship[0]][i] != "*":
                    return False
    return True


def play_game(board):
    """A function for playing the game.
    Takes 1 argument, the board array."""

    temp_board = board[0]

    while True:
        make_move(board)
        if check_win(temp_board):
            print("You win!")
            break
        else:
            print("You lost!")
            break


def check_win(board):
    """A function for checking if the player has won.
    Takes 1 argument, the board array."""

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == -1:
                return False
    return True


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
    make_move(player1_board)

if __name__ == "__main__":
    main()
