"""The code must be run from this script.
This is the code for my game of battleships."""

import class_ship
import copy

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
BOARD_SIZE = 10

aircraft_carrier = class_ship.Ship("Aircraft Carrier", 5)
battleship = class_ship.Ship("Battleship", 4)
submarine = class_ship.Ship("Submarine", 3)
destroyer = class_ship.Ship("Destroyer", 3)
patrol_boat = class_ship.Ship("Patrol Boat", 2)

print(patrol_boat)