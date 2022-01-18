"""The code must be run from this script.
This is the code for my game of battleships."""

import copy
import os
from class_ship import Ship
from class_board import Board

BOARD_SIZE = 10
SHIPS = ["A", "B", "S", "D", "P"]
# use array for if value in position not in array/not -1 etc.
AIRCRAFT_CARRIER = Ship("Aircraft Carrier", 5)
BATTLESHIP = Ship("Battleship", 4)
SUBMARINE = Ship("Submarine", 3)
DESTROYER = Ship("Destroyer", 3)
PATROL_BOAT = Ship("Patrol Boat", 2)

p1_board = Board(1, BOARD_SIZE)
p2_board = Board(2, BOARD_SIZE)


def cls():
    """Improves readability of Text interfaces by clearing the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def game_setup():
    """This should run once right at the start of main"""
    p1_aircraft_carrier = copy.deepcopy(AIRCRAFT_CARRIER)
    p1_battleship = copy.deepcopy(BATTLESHIP)
    p1_submarine = copy.deepcopy(SUBMARINE)
    p1_destroyer = copy.deepcopy(DESTROYER)
    p1_patrol_boat = copy.deepcopy(PATROL_BOAT)
    global player1_ships
    player1_ships = [p1_aircraft_carrier, p1_battleship, p1_submarine, p1_destroyer, p1_patrol_boat]

    p2_aircraft_carrier = copy.deepcopy(AIRCRAFT_CARRIER)
    p2_battleship = copy.deepcopy(BATTLESHIP)
    p2_submarine = copy.deepcopy(SUBMARINE)
    p2_destroyer = copy.deepcopy(DESTROYER)
    p2_patrol_boat = copy.deepcopy(PATROL_BOAT)
    global player2_ships
    player2_ships = [p2_aircraft_carrier, p2_battleship, p2_submarine, p2_destroyer, p2_patrol_boat]


def place_ship(board, ship, player):
    """Place a ship on the board"""
    cls()
    board.print_board(player)
    print("Place " + ship.name + " on the board.")
    print("Enter the coordinates for the front of the ship.")
    print("(ex: A1, B2, etc)")
    print("Then enter the orientation of the ship (v or h)")

    valid = False
    while not valid:
        print()
        overlap = False
        coordinates = input("Enter coordinates: ")
        orientation = input("Enter orientation: ")

        x = ord(coordinates[0].upper()) - 65
        y = int(coordinates[1])

        if x < 0 or x > 9 or y < 0 or y > 9:
            print("Invalid coordinates.")
        elif orientation.lower() not in ('v', 'h'):
            print("Invalid orientation.")
        elif orientation == 'v' and x + ship.size > 10:
            print("Ship is too long")
        elif orientation == 'h' and y + ship.size > 10:
            print("Ship is too long")
        else:
            if orientation == 'v':
                for i in range(ship.size):
                    if board.board[x + i][y] != -1:
                        overlap = True
            elif orientation == 'h':
                for i in range(ship.size):
                    if board.board[x][y + i] != -1:
                        overlap = True

            if overlap:
                print("Overlap with another ship.")
            else:
                valid = True


    # Place the ship
    if orientation == 'h':
        for i in range(ship.size):
            board.board[x][y + i] = ship.name[0]
    else:
        for i in range(ship.size):
            board.board[x + i][y] = ship.name[0]

    board.print_board(player)


def place_ships(board, ships, player):
    """Place the ships using the place_ship function, takes an array of ships."""
    for ship in ships:
        place_ship(board, ship, player)


def main():
    """Main function"""
    # Game setup
    game_setup()

    # Place ships
    place_ships(p1_board, player1_ships, 1)
    place_ships(p2_board, player2_ships, 2)

    # Game loop
    while True:
        # Player 1 turn
        print("Player 1 turn")
        p1_board.print_board(1)
        print("Enter the coordinates of the shot.")
        print("(ex: A1, B2, etc)")
        shot = input("Enter coordinates: ")
        x = ord(shot[0].upper()) - 65
        y = int(shot[1])
        if p2_board.board[x][y] == -1:
            print("You missed!")
        else:
            print("You hit!")
            p2_board.board[x][y] = '$'
        p2_board.print_board(1)

        # Player 2 turn
        print("Player 2 turn")
        p2_board.print_board(2)
        print("Enter the coordinates of the shot.")
        print("(ex: A1, B2, etc)")
        shot = input("Enter coordinates: ")
        x = ord(shot[0].upper()) - 65
        y = int(shot[1])
        if p1_board.board[x][y] == -1:
            print("You missed!")
        else:
            print("You hit!")
            p1_board.board[x][y] = '$'
        p1_board.print_board(2)


if __name__ == "__main__":
    main()
