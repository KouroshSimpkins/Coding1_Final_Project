"""The code must be run from this script.
This is the code for my game of battleships."""

import copy
import os
import warnings
import sys
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
    player1_ships = [p1_aircraft_carrier, p1_battleship, p1_submarine, p1_destroyer, p1_patrol_boat]

    p2_aircraft_carrier = copy.deepcopy(AIRCRAFT_CARRIER)
    p2_battleship = copy.deepcopy(BATTLESHIP)
    p2_submarine = copy.deepcopy(SUBMARINE)
    p2_destroyer = copy.deepcopy(DESTROYER)
    p2_patrol_boat = copy.deepcopy(PATROL_BOAT)
    player2_ships = [p2_aircraft_carrier, p2_battleship, p2_submarine, p2_destroyer, p2_patrol_boat]

    return player1_ships, player2_ships


def get_coordinates():
    """Get the coordinates of a shot from the player"""
    valid = False
    while not valid:
        print()
        coordinates = input("Enter coordinates: ")
        try:
            x = ord(coordinates[0].upper()) - 65
            y = int(coordinates[1])
        except ValueError:
            warnings.warn("Coordinates must be in the form of A1, B2, etc.")
        except IndexError:
            warnings.warn("Do not leave the coordinates blank.")
        else:
            if x < 0 or x > 9 or y < 0 or y > 9:
                print("Invalid coordinates.")
            else:
                valid = True

    return x, y


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

        x, y = get_coordinates()
        orientation = input("Enter orientation: ")

        if orientation.lower() not in ('v', 'h'):
            print("Invalid orientation.")
        elif orientation == 'v' and x + ship.size > 10:
            print("Ship is too long")
        elif orientation == 'h' and y + ship.size > 10:
            print("Ship is too long")
        else:
            if orientation.lower() == 'v':
                for i in range(ship.size):
                    if board.board[x + i][y] != -1:
                        overlap = True
            elif orientation.lower() == 'h':
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


def game_loop(playerboard, opponentboard, ships, player):
    """Game loop for the game"""
    cls()
    playerboard.print_board(player)

    opponentboard.print_board(player)

    print()
    print("Player " + str(player) + " turn.")
    print("Enter the coordinates for your shot.")
    print("(ex: A1, B2, etc)")
    print()

    valid = False
    while not valid:

        x, y = get_coordinates()

        if opponentboard.board[x][y] == "*" or opponentboard.board[x][y] == "X":
            print("You already shot there.")
        else:
            valid = True

    if opponentboard.board[x][y] == -1:
        print("Miss")
        opponentboard.board[x][y] = "*"
        input()
    else:
        print("Hit")
        for ship in ships:
            if ship.name[0] == opponentboard.board[x][y]:
                opponentboard.board[x][y] = "X"
                ship.hits += 1
                if ship.hits == ship.size:
                    print(ship.name + " sunk!")
                    ships.remove(ship)
                    if len(ships) == 0:
                        print("Player " + str(player) + " wins!")
                        input()
                        return True
                    else:
                        input()
                        return False
                else:
                    input()
                    return False


def main_menu():
    """Main menu for the game"""
    while True:
        cls()
        print("Welcome to Battleship!")
        print("1. Start game")
        print("2. Instructions")
        print("3. Quit")
        print()

        valid = False
        while not valid:
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                warnings.warn("Please enter a number.")
            else:
                if choice < 1 or choice > 3:
                    warnings.warn("Please enter a number between 1 and 3.")
                else:
                    valid = True

        if choice == 1:
            break
        elif choice == 2:
            cls()
            print("Instructions:")
            print("1. Place your ships on the board.")
            print("2. Enter the coordinates of your shot.")
            print("3. If you hit a ship, it will be marked as a hit (X).")
            print("4. If you miss, it will be marked as a miss (*).")
            print("The game is run on an honor system.")
            print("The first player to sink all of the other player's ships wins.")
            input("Press Enter to continue.")
        else:
            # Quit
            sys.exit()


def main():
    """Main function"""

    # Main menu
    main_menu()

    # Game setup
    player1_ships, player2_ships = game_setup()

    # Place ships
    place_ships(p1_board, player1_ships, 1)
    place_ships(p2_board, player2_ships, 2)

    # Game loop
    while True:
        cls()
        input("Ready for player 1's turn. (Press Enter To Go)")
        game_loop(p1_board, p2_board, player1_ships, 1)

        cls()
        input("Ready for player 2's turn. (Press Enter To Go)")
        if game_loop(p2_board, p1_board, player2_ships, 2):
            break

    # Print final boards
    p1_board.print_board(1)
    p2_board.print_board(2)


if __name__ == "__main__":
    main()
