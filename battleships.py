"""Final project for coding 1, a game of battleship that can be played by 2 players.
The aim of this module is to build a proof of concept where I work out the logic of the game.
I will also attempt to outline the steps that I will need to take"""
# Create a game of battleship that can be played by 2 players.
# The aim of this game is to build a proof of concept where I work out the logic of the game.
# I will also attempt to outline the steps that I will need to take.
# The game will be played on a 10x10 grid.
# The players will take turns firing shots at each other.
# The player who has the most ships alive at the end of the game wins.
# The game will be played with 5 ships of varying sizes.
# The ships will be placed randomly on the grid.
# The ships will be represented by a certain character, depending on the size of the ship.
# The player will be prompted to enter a coordinate to fire at.
# The game will check if the coordinate is within the grid.
# The game will check if the coordinate has already been fired at.
# The game will check if the coordinate has a ship on it.
# The game will check if the ship has been hit.
# The game will check if the ship has been sunk.
# The winner of the game will be the player who sinks all their opponent's ships first.


import random


# generate a 10x10 array of empty strings
def grid_generator():
    """Generates a 10x10 grid of empty strings"""
    grid = []
    for i in range(10): # pylint: disable=unused-variable
        grid.append([""] * 10)
    return grid


# A function that prints the grid nicely formatted
def print_grid(grid):
    """Prints the grid in a nice format"""
    for row in grid:
        print("[ ]".join(row))


# A ship class that will be used to create ships
class Ship:
    """A class that creates a ship"""
    def __init__(self, size, name):
        """Initialises the ship"""
        self.size = size
        self.name = name
        self.hit_count = 0

    def hit(self):
        """A function that increments the hit count"""
        self.hit_count += 1

    def sunk(self):
        """A function that checks if the ship has been sunk"""
        if self.hit_count == self.size:
            return True
        return False


# There should be one ship with a length of 5
# There should be one ship with a length of 4
# There should be two ships with a length of 3
# There should be one ship with a length of 2
# Generate a list of ships using the ship class
def ship_generator():
    """Generates a list of ships"""
    ships = []
    ships.append(Ship(5, "Aircraft Carrier"))
    ships.append(Ship(4, "Battleship"))
    ships.append(Ship(3, "Submarine"))
    ships.append(Ship(3, "Destroyer"))
    ships.append(Ship(2, "Patrol Boat"))
    return ships


# A function that places the ships on the grid
def ship_placement(grid, ships):
    """Places the ships on the grid"""
    for ship in ships:
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if grid[x][y] == "":
                grid[x][y] = ship.name
                break
            else:
                continue


# A function that prompts the user to enter a coordinate
def coordinate_prompt():
    """Prompts the user to enter a coordinate"""
    while True:
        try:
            x = int(input("Enter a coordinate to fire at: "))
            y = int(input("Enter a coordinate to fire at: "))
            if x > 9 or y > 9:
                print("Coordinate out of range")
                continue
            else:
                return x, y
        except ValueError:
            print("Please enter a valid coordinate")
            continue
